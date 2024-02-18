from plugins.con_err import ErrorConnection
from datetime import datetime
from time import sleep
import requests as req
import os.path as path
import threading
import sqlite3
import re
import json


class Search404:

    fpath: str = r'plugins\opm_parser.db'
    con: sqlite3.Connection
    cur: sqlite3.Cursor
    main_url: str = 'https://opm.ru'

    def __init__(self, signal):
        self.signal = signal
        self.bad_links = dict()
        self.rez = dict()
        self.__connect()

    def analys(self):
        timer = datetime.now()
        data = self.parser_urls()
        self.signal.emit([0, 'Анализ ссылок'])
        self.cur.execute('SELECT url FROM html_content')
        self.reference = list(map(lambda x: x[0], self.cur.fetchall()))
        for url in data:
            self.signal.emit([1, f'{list(data).index(url)}/{len(data)}\n{url}'])
            links = data.get(url)
            self.temp = dict()
            while len(links) > 0:
                threads = []
                for _ in range(110):
                    if len(links) == 0: break
                    t = threading.Thread(target=self.th_analys, args=(links.pop(0),))
                    threads.append(t)
                    t.start()
                for i in threads:
                    i.join()
                if len(links) > 10:
                    sleep(5)
            if len(self.temp) > 0:
                self.rez.update({url: self.temp})
        date = datetime.now().strftime('%d-%m-%y')
        with open(fr'rezult\{date}_error404.json', 'w', encoding='utf-8') as f:
            json.dump(self.rez, f, indent=4, ensure_ascii=False)

        timer = datetime.now() - timer
        self.signal.emit([0, 'Загрузка завершена'])
        self.signal.emit([1, f'Время выполнения: {str(timer).split(".")[0]}'])
        self.signal.emit([2])

    def th_analys(self, link):
        full_link = self.main_url + link
        if full_link in self.reference: return
        if full_link in self.bad_links:
            self.temp.update({link: self.bad_links.get(link)})
            return
        while True:
            status = req.head(full_link).status_code
            if status != 502:
                break
            sleep(2)
        if status != 200:
            self.temp.update({link: status})
            self.bad_links.update({link: status})
            return
        self.reference.append(full_link)

    def parser_urls(self):
        data = self.get_html()
        self.signal.emit([0, 'Сбор ссылок с тегов <a> и <img>'])
        db = dict()
        for _, url, fpath in data:
            self.signal.emit([1, f'{len(db)+1}/{len(data)}\n{url}'])
            with open(fpath, encoding='utf-8') as f:
                html = f.read()
            urls = self.get_url(html)
            db.update({url: list(urls)})
        return db

    def get_url(self, data):
        tags = re.findall(r'<a.+?>|<img.+?>', data)
        temp_urls = list(map(lambda i: re.findall(r'(?<=src=\").+?(?=\")|(?<=href=\").+?(?=\")', i), tags))
        urls = []
        for url in temp_urls:
            if len(url) == 0: continue
            url = url[0]
            if len(re.findall(r'^http|\.svg$', url)): continue
            if '/' not in url: continue
            if '?' in url:
                url = url[:url.index('?')]
            urls.append(url)
        urls = set(urls)
        return urls

    def get_html(self):
        self.signal.emit([0, "Загрузка HTML контента"])
        self.signal.emit([1, "Загрузка HTML контента"])
        self.cur.execute('SELECT * FROM html_content')
        return list(filter(lambda x: x[2] is not None, self.cur.fetchall()))

    def __connect(self):
        if not path.exists(self.fpath):
            self.signal.emit([0, 'Подключение к Базе Данных'])
            self.signal.emit([1, 'Базы Данных нет. Произведите генерацию'])
            raise ErrorConnection('file opm_parser.db is not defined')
        self.con = sqlite3.connect(self.fpath)
        self.cur = self.con.cursor()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.cur.close()
        self.con.close()
