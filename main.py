from PyQt5 import QtWidgets, QtCore, Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog
from db_operation import *
from interface import *
import dialog
import sys
import os


class Dialog(dialog.Ui_Dialog, QDialog):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

    def setupUi(self, Dialog):
        super().setupUi(self)
        self.setWindowFlag(QtCore.Qt.WindowType.FramelessWindowHint)
        self.d_btn_close.setDisabled(True)
        self.d_btn_close.clicked.connect(self.close_dialog)

    def change_text(self, data):
        match data[0]:
            case 0:
                self.title.setText(data[1])
            case 1:
                self.procces.setText(data[1])
            case 2:
                self.open_btn()

    def open_btn(self):
        self.d_btn_close.setDisabled(False)

    def close_dialog(self):
        self.hide()


class App(Ui_MainWindow, QMainWindow):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.mk_rez()
        self.stackedWidget.setCurrentWidget(self.pgen)
        self.stackedWidget_2.setCurrentWidget(self.p404)
        self.tab_search.setCurrentWidget(self.tab_find_file)
        self.grp_find_tag.setEnabled(False)
        self.grp_content_tag.setEnabled(False)
        self.grp_get_atr.setEnabled(False)

    def setupUi(self, MainWindow):
        super().setupUi(self)

        self.chk_find_tag.clicked.connect(lambda: self.grp_find_tag.setEnabled(self.chk_find_tag.isChecked()))
        self.chk_content_tag.clicked.connect(lambda: self.grp_content_tag.setEnabled(self.chk_content_tag.isChecked()))
        self.chk_get_atr.clicked.connect(lambda: self.grp_get_atr.setEnabled(self.chk_get_atr.isChecked()))
        self.btn_fing_tag.clicked.connect(self.find_tags)

        self.btn_pgen.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.pgen))
        self.btn_prazdel.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.prazdel))

        self.btn_404.clicked.connect(lambda: self.stackedWidget_2.setCurrentWidget(self.p404))
        self.btn_search.clicked.connect(lambda: self.stackedWidget_2.setCurrentWidget(self.psearch))

        self.btn_gen.clicked.connect(self.generation_db)
        self.btn_analys.clicked.connect(self.analys)
        self.btn_find_file.clicked.connect(self.find_files)

        self.msg = Dialog(self)

    def find_tags(self):
        send: dict = dict()
        if self.edit_find_tag.isEnabled():
            send.update({'find_tags': self.edit_find_tag.toPlainText()})
        if self.edit_content_tag.isEnabled():
            send.update({'find_content': self.edit_content_tag.text()})
        if self.grp_get_atr.isEnabled():
            send.update({'get_atr': [
                self.edit_get_tag.text(),
                self.edit_get_atr.text()
            ]})
        self.ft = DBoperation('find_tags', **send)
        self.msg.setWindowTitle('Поиск тегов')
        self.ft.mysig.connect(self.msg.change_text)
        self.ft.started.connect(self.msg.show)
        self.ft.start()

    def find_files(self):
        types = self.edit_ftypes.toPlainText()
        self.ff = DBoperation('find_files', ftypes=types)
        self.msg.setWindowTitle('Поиск файлов')
        self.ff.mysig.connect(self.msg.change_text)
        self.ff.started.connect(self.msg.show)
        self.ff.start()

    def analys(self):
        self.analys = DBoperation('search')
        self.msg.setWindowTitle("Анализ ссылок")
        self.analys.mysig.connect(self.msg.change_text)
        self.analys.started.connect(self.msg.show)
        self.analys.start()

    def generation_db(self):
        self.msg.setWindowTitle("Генерация Базы Данных")
        self.gen = DBoperation(
            'generation', bl=self.bl_edit.toPlainText(), wl=self.wl_edit.toPlainText())
        self.gen.mysig.connect(self.msg.change_text)
        self.gen.started.connect(self.msg.show)
        self.gen.start()

    def mk_rez(self):
        if not os.path.exists('rezult'):
            os.mkdir('rezult')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = App()
    win.show()
    sys.exit(app.exec_())