from plugins.con_err import ErrorConnection
from bs4 import BeautifulSoup as bs
from datetime import datetime
import os.path as path
import sqlite3
import json

class FindTag:

    fpath: str = r'plugins\opm_parser.db'
    con: sqlite3.Connection
    cur: sqlite3.Cursor

    def __init__(self, signal):
        self.signal = signal
        self.__connect()
        self.data = self.get_fpath()

    def get_atr(self, data):
        tag, atr = data
        self.signal.emit([0, f'Сбор значений атрибута {atr!r} в теге <{tag}>'])
        rez = dict()
        count = 0
        for _, url, fpath in self.data:
            self.signal.emit([1, f'{count}/{len(self.data)}\n{url}'])
            count += 1
            temp = list()
            with open(fpath, encoding='utf-8') as f:
                tags = bs(f.read(), 'html.parser').findAll(tag)
            for select_tag in tags:
                atr_val = select_tag.get(atr)
                if atr_val is None: continue
                temp.append(atr_val)
            if len(temp) > 0: rez.update({url: temp})
        date = datetime.now().strftime('%d-%m-%y')
        with open(fr'rezult\{date}_get_atr.json', 'w', encoding='utf-8') as f:
            json.dump(rez, f, indent=4, ensure_ascii=False)

    def find_content(self, tag):
        self.signal.emit([0, f'поиск одиннакового содержимого в теге <{tag}>'])
        rez = dict()
        temp = dict()
        count = 0
        for _, url, fpath in self.data:
            self.signal.emit([1, f'{count}/{len(self.data)}\n{url}'])
            count += 1
            with open(fpath, encoding='utf-8') as f:
                content = bs(f.read(), 'html.parser').find(tag)
            if content == None: continue
            content = content.text
            if content not in temp:
                temp.update({content: [url]})
            else:
                temp.get(content).append(url)
        for i in temp:
            if len(temp.get(i)) > 1:
                rez.update({i: temp.get(i)})
        date = datetime.now().strftime('%d-%m-%y')
        with open(fr'rezult\{date}_content_{tag}.json', 'w', encoding='utf-8') as f:
            json.dump(rez, f, indent=4, ensure_ascii=False)

    def find_tags(self, tags):
        tags = tags.split('\n')
        self.signal.emit([0, 'Поиск ссылок на файл в странице'])
        rez = dict()
        count = 0
        for _, url, fpath in self.data:
            self.signal.emit([1, f'{count}/{len(self.data)}\n{url}'])
            str_tags = ''
            with open(fpath, encoding='utf-8') as f:
                urls = bs(f.read(), 'html.parser')
            for tag in tags:
                if len(urls.findAll(tag)) > 0:
                    str_tags += f'{tag}  '
            if str_tags != '':
                rez.update({url: str_tags})
            count += 1
        date = datetime.now().strftime('%d-%m-%y')
        with open(fr'rezult\{date}_find_tags.json', 'w', encoding='utf-8') as f:
            json.dump(rez, f, indent=4, ensure_ascii=False)

    def get_fpath(self):
        self.signal.emit([0, 'Получениие ссылок на файлы страниц'])
        self.signal.emit([1, 'Ожидание'])
        self.cur.execute('SELECT * FROM html_content')
        return list(filter(lambda x: x[2] is not None, self.cur.fetchall()))

    def __connect(self):
        if not path.exists(self.fpath):
            raise ErrorConnection('file opm_parser.db is not defined')
        self.con = sqlite3.connect(self.fpath)
        self.cur = self.con.cursor()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.cur.close()
        self.con.close()