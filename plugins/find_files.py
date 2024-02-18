from plugins.con_err import ErrorConnection
from datetime import datetime
import os.path as path
import sqlite3
import json
import re


class Find_file:

    fpath: str = r'plugins\opm_parser.db'
    con: sqlite3.Connection
    cur: sqlite3.Cursor

    def __init__(self, signal, ftypes):
        self.signal = signal
        self.ftypes = ftypes.split('\n')
        self.__connect()

    def search_file(self):
        timer = datetime.now()
        self.signal.emit([0, 'Поиск ссылок на файл в странице'])
        rez = dict()
        data = self.get_fpath()
        count = 0
        for _, url, fpath in data:
            self.signal.emit([1, f'{count}/{len(data)}\n{url}'])
            temp = list()
            with open(fpath, encoding='utf-8') as f:
                urls = re.findall(r'(?<=src=).+?\"|(?<=href=).+?\"', f.read())
            urls = list(map(lambda x: x.replace('"', ''), urls))
            urls = list(filter(lambda x: x != '', urls))
            for link in urls:
                if link.split('.')[-1] in self.ftypes:
                    temp.append(link)
            if len(temp) > 0:
                rez.update({url: temp})
            count += 1
        date = datetime.now().strftime('%d-%m-%y')
        with open(fr'rezult\{date}_find_files.json', 'w', encoding='utf-8') as f:
            json.dump(rez, f, indent=4, ensure_ascii=False)
        timer = datetime.now() - timer
        self.signal.emit([0, 'Загрузка завершена'])
        self.signal.emit([1, f'Время выполнения: {str(timer).split(".")[0]}'])
        self.signal.emit([2])

    def get_fpath(self):
        self.signal.emit([0, 'Получениие ссылок на файлы страниц'])
        self.signal.emit([1, 'Ожидание'])
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
