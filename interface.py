# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'interface.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.ApplicationModal)
        MainWindow.resize(560, 430)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.fmenu = QtWidgets.QFrame(self.centralwidget)
        self.fmenu.setGeometry(QtCore.QRect(0, 0, 40, 430))
        self.fmenu.setStyleSheet("QFrame {\n"
"    background-color: #008B8B;\n"
"}\n"
"QPushButton{\n"
"    background-color: transparent;\n"
"    background-position: center;\n"
"    background-repeat: no-repeat;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgba(0,0,0,50);\n"
"}")
        self.fmenu.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.fmenu.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fmenu.setObjectName("fmenu")
        self.btn_pgen = QtWidgets.QPushButton(self.fmenu)
        self.btn_pgen.setGeometry(QtCore.QRect(0, 0, 40, 40))
        self.btn_pgen.setStyleSheet("QPushButton{\n"
"    background-image: url(source/upload.png);\n"
"}\n"
"")
        self.btn_pgen.setIconSize(QtCore.QSize(50, 50))
        self.btn_pgen.setObjectName("btn_pgen")
        self.btn_prazdel = QtWidgets.QPushButton(self.fmenu)
        self.btn_prazdel.setGeometry(QtCore.QRect(0, 40, 40, 40))
        self.btn_prazdel.setStyleSheet("QPushButton{\n"
"    background-image: url(source/razdel.png);\n"
"}\n"
"")
        self.btn_prazdel.setText("")
        self.btn_prazdel.setObjectName("btn_prazdel")
        self.content = QtWidgets.QFrame(self.centralwidget)
        self.content.setGeometry(QtCore.QRect(40, 0, 520, 430))
        self.content.setStyleSheet("QFrame{\n"
"    background-color: #5F9EA0;\n"
"}\n"
"")
        self.content.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.content.setFrameShadow(QtWidgets.QFrame.Raised)
        self.content.setObjectName("content")
        self.stackedWidget = QtWidgets.QStackedWidget(self.content)
        self.stackedWidget.setGeometry(QtCore.QRect(0, 0, 520, 430))
        self.stackedWidget.setStyleSheet("QWidget{\n"
"    background-color:transparent;\n"
"}\n"
"QPushButton{\n"
"    height: 60px;\n"
"    border: 2px groove rgb(47,79,79);\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgba(0,0,0,50);\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: rgba(0,0,0,70);\n"
"}")
        self.stackedWidget.setObjectName("stackedWidget")
        self.pgen = QtWidgets.QWidget()
        self.pgen.setStyleSheet("QTextEdit{\n"
"    background-color: white;\n"
"}")
        self.pgen.setObjectName("pgen")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.pgen)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(20, 340, 488, 70))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(362, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.btn_gen = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.btn_gen.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_gen.sizePolicy().hasHeightForWidth())
        self.btn_gen.setSizePolicy(sizePolicy)
        self.btn_gen.setMinimumSize(QtCore.QSize(50, 0))
        self.btn_gen.setSizeIncrement(QtCore.QSize(0, 0))
        self.btn_gen.setBaseSize(QtCore.QSize(0, 0))
        self.btn_gen.setObjectName("btn_gen")
        self.horizontalLayout.addWidget(self.btn_gen)
        self.label_6 = QtWidgets.QLabel(self.pgen)
        self.label_6.setGeometry(QtCore.QRect(110, 70, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.pgen)
        self.label_7.setGeometry(QtCore.QRect(310, 70, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.pgen)
        self.label_8.setGeometry(QtCore.QRect(141, 0, 241, 41))
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.bl_edit = QtWidgets.QTextEdit(self.pgen)
        self.bl_edit.setGeometry(QtCore.QRect(273, 115, 180, 180))
        self.bl_edit.setObjectName("bl_edit")
        self.wl_edit = QtWidgets.QTextEdit(self.pgen)
        self.wl_edit.setGeometry(QtCore.QRect(68, 115, 180, 180))
        self.wl_edit.setObjectName("wl_edit")
        self.stackedWidget.addWidget(self.pgen)
        self.prazdel = QtWidgets.QWidget()
        self.prazdel.setStyleSheet("QLineEdit{\n"
"    background-color: white;\n"
"}")
        self.prazdel.setObjectName("prazdel")
        self.f_razdel_menu = QtWidgets.QFrame(self.prazdel)
        self.f_razdel_menu.setGeometry(QtCore.QRect(0, 40, 40, 390))
        self.f_razdel_menu.setStyleSheet("QFrame{\n"
"    background-color: #f0e68c;\n"
"}\n"
"QPushButton{\n"
"    background-color: transparent;\n"
"    background-position: center;\n"
"    background-repeat: no-repeat;\n"
"    border: inherit;\n"
"    \n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgba(0,0,0,50);\n"
"}")
        self.f_razdel_menu.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.f_razdel_menu.setFrameShadow(QtWidgets.QFrame.Raised)
        self.f_razdel_menu.setObjectName("f_razdel_menu")
        self.btn_404 = QtWidgets.QPushButton(self.f_razdel_menu)
        self.btn_404.setGeometry(QtCore.QRect(0, 0, 40, 40))
        self.btn_404.setStyleSheet("QPushButton{\n"
"    background-image: url(source/404.png);\n"
"}\n"
"")
        self.btn_404.setText("")
        self.btn_404.setObjectName("btn_404")
        self.btn_search = QtWidgets.QPushButton(self.f_razdel_menu)
        self.btn_search.setGeometry(QtCore.QRect(0, 40, 40, 40))
        self.btn_search.setStyleSheet("QPushButton{\n"
"    background-image: url(source/search.png);\n"
"}\n"
"")
        self.btn_search.setText("")
        self.btn_search.setObjectName("btn_search")
        self.stackedWidget_2 = QtWidgets.QStackedWidget(self.prazdel)
        self.stackedWidget_2.setGeometry(QtCore.QRect(40, 0, 480, 430))
        self.stackedWidget_2.setObjectName("stackedWidget_2")
        self.p404 = QtWidgets.QWidget()
        self.p404.setObjectName("p404")
        self.btn_analys = QtWidgets.QPushButton(self.p404)
        self.btn_analys.setGeometry(QtCore.QRect(150, 330, 181, 71))
        self.btn_analys.setObjectName("btn_analys")
        self.label = QtWidgets.QLabel(self.p404)
        self.label.setGeometry(QtCore.QRect(70, 0, 331, 81))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setScaledContents(False)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setWordWrap(False)
        self.label.setOpenExternalLinks(False)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.p404)
        self.label_2.setGeometry(QtCore.QRect(40, 120, 421, 151))
        self.label_2.setLineWidth(1)
        self.label_2.setTextFormat(QtCore.Qt.AutoText)
        self.label_2.setScaledContents(False)
        self.label_2.setWordWrap(True)
        self.label_2.setIndent(0)
        self.label_2.setObjectName("label_2")
        self.stackedWidget_2.addWidget(self.p404)
        self.psearch = QtWidgets.QWidget()
        self.psearch.setObjectName("psearch")
        self.tab_search = QtWidgets.QTabWidget(self.psearch)
        self.tab_search.setGeometry(QtCore.QRect(0, 19, 480, 411))
        self.tab_search.setStyleSheet("QTabWidget::pane{\n"
"    border-top: 2px solid #ff9e00;\n"
"    \n"
"}\n"
"QTabBar::tab{\n"
"    top: 2px;\n"
"    background: #d3d3d3;\n"
"     border: 2px solid #FF9e00;\n"
"     border-bottom-color: #000;\n"
"     min-width: 15ex;\n"
"     padding: 2px 10px;\n"
"}\n"
"QTabBar::tab:selected, QTabBar::tab:hover {\n"
"     background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                 stop: 0 #fafafa, stop: 0.4 #f4f4f4,\n"
"                                 stop: 0.5 #e7e7e7, stop: 1.0 #fafafa);\n"
" }\n"
"QTabBar::tab:!selected{\n"
"    margin-top: 4px;\n"
"}")
        self.tab_search.setObjectName("tab_search")
        self.tab_find_file = QtWidgets.QWidget()
        self.tab_find_file.setObjectName("tab_find_file")
        self.label_3 = QtWidgets.QLabel(self.tab_find_file)
        self.label_3.setGeometry(QtCore.QRect(70, 10, 361, 41))
        self.label_3.setTextFormat(QtCore.Qt.RichText)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.tab_find_file)
        self.label_4.setGeometry(QtCore.QRect(20, 70, 151, 21))
        self.label_4.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_4.setObjectName("label_4")
        self.edit_ftypes = QtWidgets.QTextEdit(self.tab_find_file)
        self.edit_ftypes.setGeometry(QtCore.QRect(180, 70, 191, 61))
        self.edit_ftypes.setStyleSheet("QTextEdit{\n"
"    background-color: white;\n"
"}")
        self.edit_ftypes.setObjectName("edit_ftypes")
        self.btn_find_file = QtWidgets.QPushButton(self.tab_find_file)
        self.btn_find_file.setGeometry(QtCore.QRect(20, 150, 121, 31))
        self.btn_find_file.setObjectName("btn_find_file")
        self.tab_search.addTab(self.tab_find_file, "")
        self.tab_find_tag = QtWidgets.QWidget()
        self.tab_find_tag.setObjectName("tab_find_tag")
        self.grp_find_tag = QtWidgets.QGroupBox(self.tab_find_tag)
        self.grp_find_tag.setEnabled(True)
        self.grp_find_tag.setGeometry(QtCore.QRect(20, 35, 181, 70))
        self.grp_find_tag.setTitle("")
        self.grp_find_tag.setObjectName("grp_find_tag")
        self.label_5 = QtWidgets.QLabel(self.grp_find_tag)
        self.label_5.setGeometry(QtCore.QRect(10, 10, 91, 16))
        self.label_5.setTextFormat(QtCore.Qt.RichText)
        self.label_5.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_5.setObjectName("label_5")
        self.edit_find_tag = QtWidgets.QTextEdit(self.grp_find_tag)
        self.edit_find_tag.setGeometry(QtCore.QRect(90, 10, 71, 41))
        self.edit_find_tag.setStyleSheet("QTextEdit{\n"
"    background-color: #fff;\n"
"}")
        self.edit_find_tag.setObjectName("edit_find_tag")
        self.chk_find_tag = QtWidgets.QCheckBox(self.tab_find_tag)
        self.chk_find_tag.setGeometry(QtCore.QRect(20, 10, 161, 17))
        self.chk_find_tag.setObjectName("chk_find_tag")
        self.btn_fing_tag = QtWidgets.QPushButton(self.tab_find_tag)
        self.btn_fing_tag.setGeometry(QtCore.QRect(360, 330, 111, 41))
        self.btn_fing_tag.setObjectName("btn_fing_tag")
        self.chk_content_tag = QtWidgets.QCheckBox(self.tab_find_tag)
        self.chk_content_tag.setGeometry(QtCore.QRect(220, 10, 211, 17))
        self.chk_content_tag.setObjectName("chk_content_tag")
        self.grp_content_tag = QtWidgets.QGroupBox(self.tab_find_tag)
        self.grp_content_tag.setGeometry(QtCore.QRect(220, 35, 211, 70))
        self.grp_content_tag.setTitle("")
        self.grp_content_tag.setObjectName("grp_content_tag")
        self.label_9 = QtWidgets.QLabel(self.grp_content_tag)
        self.label_9.setGeometry(QtCore.QRect(10, 10, 21, 16))
        self.label_9.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_9.setObjectName("label_9")
        self.edit_content_tag = QtWidgets.QLineEdit(self.grp_content_tag)
        self.edit_content_tag.setGeometry(QtCore.QRect(39, 10, 161, 20))
        self.edit_content_tag.setObjectName("edit_content_tag")
        self.label_10 = QtWidgets.QLabel(self.grp_content_tag)
        self.label_10.setGeometry(QtCore.QRect(10, 50, 91, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_10.setFont(font)
        self.label_10.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_10.setObjectName("label_10")
        self.chk_get_atr = QtWidgets.QCheckBox(self.tab_find_tag)
        self.chk_get_atr.setGeometry(QtCore.QRect(20, 123, 211, 17))
        self.chk_get_atr.setObjectName("chk_get_atr")
        self.grp_get_atr = QtWidgets.QGroupBox(self.tab_find_tag)
        self.grp_get_atr.setGeometry(QtCore.QRect(20, 145, 231, 71))
        self.grp_get_atr.setTitle("")
        self.grp_get_atr.setObjectName("grp_get_atr")
        self.label_11 = QtWidgets.QLabel(self.grp_get_atr)
        self.label_11.setGeometry(QtCore.QRect(10, 8, 47, 13))
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.grp_get_atr)
        self.label_12.setGeometry(QtCore.QRect(10, 40, 47, 13))
        self.label_12.setObjectName("label_12")
        self.edit_get_tag = QtWidgets.QLineEdit(self.grp_get_atr)
        self.edit_get_tag.setGeometry(QtCore.QRect(65, 7, 113, 20))
        self.edit_get_tag.setObjectName("edit_get_tag")
        self.edit_get_atr = QtWidgets.QLineEdit(self.grp_get_atr)
        self.edit_get_atr.setGeometry(QtCore.QRect(65, 37, 113, 20))
        self.edit_get_atr.setObjectName("edit_get_atr")
        self.tab_search.addTab(self.tab_find_tag, "")
        self.stackedWidget_2.addWidget(self.psearch)
        self.stackedWidget.addWidget(self.prazdel)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(1)
        self.tab_search.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.wl_edit, self.btn_pgen)
        MainWindow.setTabOrder(self.btn_pgen, self.btn_gen)
        MainWindow.setTabOrder(self.btn_gen, self.bl_edit)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "ОПМ парсер"))
        self.btn_pgen.setToolTip(_translate("MainWindow", "<html><head/><body><p>Генерация</p></body></html>"))
        self.btn_pgen.setWhatsThis(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.btn_prazdel.setToolTip(_translate("MainWindow", "<html><head/><body><p>Анализ страниц</p></body></html>"))
        self.btn_gen.setText(_translate("MainWindow", "Генерация"))
        self.label_6.setText(_translate("MainWindow", "Белый список"))
        self.label_7.setText(_translate("MainWindow", "Черный список"))
        self.label_8.setText(_translate("MainWindow", "Генерация страниц"))
        self.btn_404.setToolTip(_translate("MainWindow", "<html><head/><body><p>Поиск битых ссылок</p></body></html>"))
        self.btn_search.setToolTip(_translate("MainWindow", "<html><head/><body><p>Поиск совпадений</p></body></html>"))
        self.btn_analys.setText(_translate("MainWindow", "Анализ"))
        self.label.setText(_translate("MainWindow", "Проверка ссылок на 404 ошибку"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p>Данная функция проверяет ссылки на 404 ошибку.</p><p>Так же данная функция проверяет и 301 статус (редирект), однако есть шанс того, что результат проверки для 302 статуса будет искажён связи с тем, что данная функция не проверяет ссылки из sitemap.xml.</p><p>Среднее время проверки ссылок для 2500 страниц: 1 час</p><p>Нажам на кнопку &quot;Анализ&quot; вы подверждаете, что ознакомились с данной функцией.</p></body></html>"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt;\">Поиск ссылок на файл(ов) на странице.</span></p></body></html>"))
        self.label_4.setText(_translate("MainWindow", "Расширения искомых фалов:"))
        self.btn_find_file.setText(_translate("MainWindow", "Поиск"))
        self.tab_search.setTabText(self.tab_search.indexOf(self.tab_find_file), _translate("MainWindow", "Поиск файлов"))
        self.label_5.setText(_translate("MainWindow", "<html><head/><body><p>Искомые теги:</p></body></html>"))
        self.chk_find_tag.setText(_translate("MainWindow", "Поиск определённых тегов"))
        self.btn_fing_tag.setText(_translate("MainWindow", "Поиск"))
        self.chk_content_tag.setText(_translate("MainWindow", "Наличие одиннакового содержимого"))
        self.label_9.setText(_translate("MainWindow", "Тег:"))
        self.label_10.setText(_translate("MainWindow", "*Только один тег"))
        self.chk_get_atr.setText(_translate("MainWindow", "Получение значения атрибута в теге "))
        self.label_11.setText(_translate("MainWindow", "Тег:"))
        self.label_12.setText(_translate("MainWindow", "Атрибут:"))
        self.tab_search.setTabText(self.tab_search.indexOf(self.tab_find_tag), _translate("MainWindow", "Поиск по тегам"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
