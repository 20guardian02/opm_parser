from PyQt5 import QtWidgets, QtCore, QtGui
from plugins.con_err import ErrorConnection
from datetime import datetime
from plugins.generation import *
from plugins.search404 import *
from plugins.find_files import *
from plugins.find_tag import *


class DBoperation(QtCore.QThread):

    mysig = QtCore.pyqtSignal(list)

    def __init__(self, opt: str, *, parent=None, **kwargs):
        super().__init__(parent)
        self.operation = opt
        self.kwargs = kwargs

    def generation(self):
        with Generation(self.mysig, **self.kwargs) as gen:
            gen.load_html()

    def search(self):
        with Search404(self.mysig) as search:
            search.analys()

    def find_files(self):
        with Find_file(self.mysig, **self.kwargs) as ff:
            ff.search_file()

    def find_tags(self):
        timer = datetime.now()
        with FindTag(self.mysig) as ft:
            if 'find_tags' in self.kwargs:
                ft.find_tags(self.kwargs.get('find_tags'))
            if 'find_content' in self.kwargs:
                ft.find_content(self.kwargs.get('find_content'))
            if 'get_atr' in self.kwargs:
                ft.get_atr(self.kwargs.get('get_atr'))
        timer = datetime.now() - timer
        self.mysig.emit([0, 'Загрузка завершена'])
        self.mysig.emit([1, f'Время выполнения: {str(timer).split(".")[0]}'])
        self.mysig.emit([2])

    def run(self):
        dict_fun: dict = {
            'generation': self.generation,
            'search': self.search,
            'find_files': self.find_files,
            'find_tags': self.find_tags
        }
        try:
            dict_fun.get(self.operation)()
        except ErrorConnection as e:
            self.mysig.emit([0, 'Ошибка подключения базы данных'])
            self.mysig.emit([1, 'Файл базы данных не обнаружено.\nПроведите генерация страниц для создания базы данных'])


