import os.path as path
import threading
import requests
import sqlite3
import glob
import time
import re
import os
from bs4 import BeautifulSoup as bs
from datetime import datetime


class Generation:

    con: sqlite3.Connection
    cur: sqlite3.Cursor
    MAIN_URL: str = 'https://opm.ru/sitemap.xml'
    cmd: list = []

    def __init__(self, signal, bl: str = ' ', wl: str = ''):
        self.bl = bl.replace('\n', '|')
        self.wl = wl.replace('\n', '|')
        self.con = sqlite3.connect('plugins/opm_parser.db', check_same_thread=False)
        self.cur = self.con.cursor()
        self.signal = signal
        self.__create_db()

    def load_html(self) -> None:
        timer = datetime.now()
        self.update_url()
        self.signal.emit([0, 'Загрузка HTML контента'])
        self.cur.execute('SELECT * FROM html_content')
        urls = list(filter(self.cus_filter, self.cur.fetchall()))
        threads = []
        count_url = len(urls)
        while urls != []:
            for _ in range(110):
                self.signal.emit([1, f'{count_url-len(urls)}/{count_url}'])
                if urls == []: break
                t = threading.Thread(target=self.th_load, args=(urls.pop(0), ))
                threads.append(t)
                t.start()
            while threads != []:
                threads.pop(0).join()
            while self.cmd != []:
                self.cur.execute(self.cmd.pop(0))
            self.con.commit()
            if urls == []: break
            time.sleep(10)
        timer = datetime.now() - timer
        self.signal.emit([0, 'Загрузка завершена'])
        self.signal.emit([1, f'Время выполнения: {str(timer).split(".")[0]}'])
        self.signal.emit([2])

    def th_load(self, url: tuple) -> None:
        """
        Поток для скачивания html кода из страницы с записью в отдельный файл и в БД
        :param url: Строка из БД с ссылкой на страницу сайта
        """
        th_url = url[1]
        while True:
            r = requests.get(th_url)
            if r.status_code != 503:
                break
            time.sleep(2)
        html = bs(r.content, 'html.parser')
        for x in html.select('script'):
            x.decompose()
        html = re.sub(r'<!--.*?-->', '', str(html).replace('\n', ''))
        fpath = path.abspath(fr'source\content\{url[0]}.txt')
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(str(html))
        self.cmd.append(fr'''UPDATE html_content 
            SET path_content = {fpath!r} WHERE url = {r.url!r};''')


    def cus_filter(self, url: str) -> bool:
        if len(re.findall(self.bl, url[1])) != 0: return False
        if len(re.findall(self.wl, url[1])) != 0: return True

    def update_url(self) -> None:

        def update(url):
            html = requests.get(url).content
            links = bs(html, features='xml').findAll('loc')
            for link in list(map(lambda x: x.text, links)):
                self.signal.emit([1, link])
                if link[-4::] == '.xml':
                    update(link)
                    continue
                self.cur.execute(f'INSERT OR IGNORE INTO html_content(url) VALUES({link!r})')

        self.signal.emit([0, 'Загрузка ссылок в Базу Данных'])
        update(self.MAIN_URL)
        self.con.commit()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.cur.close()
        self.con.close()

    def __create_db(self):
        if path.exists('source\content'):
            for file in glob.glob(r'source\content\*.txt'):
                os.remove(file)
        else:
            os.mkdir(r'source\content')
        self.cur.execute('DROP TABLE IF EXISTS html_content;')
        self.cur.execute('''
        CREATE TABLE IF NOT EXISTS html_content(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            url TEXT UNIQUE,
            path_content TEXT
        );
        ''')
        self.con.commit()
