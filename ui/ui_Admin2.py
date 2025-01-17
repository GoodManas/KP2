# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_Admin2.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDialog, QHeaderView, QLabel,
    QPushButton, QSizePolicy, QTableView, QWidget)
import ui.res_admin

class Ui_Admin(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(548, 538)
        Dialog.setMaximumSize(QSize(548, 538))
        Dialog.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0 rgba(	255, 0, 0, 255), stop:0.427447 rgba(139, 0, 0, 125), stop:1 rgba(155, 79, 165, 255));\n"
"font-famaly: Roboto Flex;")
        self.widget = QWidget(Dialog)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(-50, -70, 641, 721))
        self.widget.setMaximumSize(QSize(641, 721))
        self.widget.setStyleSheet(u"background-color:rgba(225,255,255,100);\n"
"border: 1px  solid rgba(225,255,255,40);\n"
"border-radius: 7px;")
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(60, 80, 171, 41))
        self.tableView = QTableView(self.widget)
        self.tableView.setObjectName(u"tableView")
        self.tableView.setGeometry(QRect(60, 190, 521, 371))
        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(60, 130, 521, 20))
        self.btn_otchet = QPushButton(self.widget)
        self.btn_otchet.setObjectName(u"btn_otchet")
        self.btn_otchet.setGeometry(QRect(60, 160, 75, 24))
        self.btn_otchet.setStyleSheet(u"QPushButton:hover{\n"
"background-color:rgba(255,255,255,40)\n"
"}\n"
"QPushButton:pressed{\n"
"background-color:rgba(255,255,255,60)\n"
"}")
        icon = QIcon()
        icon.addFile(u":/icon/D:/games/\u0432\u043e\u0440\u043a/KP2/icon/lab_profile_24dp_E8EAED_FILL0_wght400_GRAD0_opsz24.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_otchet.setIcon(icon)
        self.btn_Exel = QPushButton(self.widget)
        self.btn_Exel.setObjectName(u"btn_Exel")
        self.btn_Exel.setGeometry(QRect(150, 160, 75, 24))
        self.btn_Exel.setStyleSheet(u"QPushButton:hover{\n"
"background-color:rgba(255,255,255,40)\n"
"}\n"
"QPushButton:pressed{\n"
"background-color:rgba(255,255,255,60)\n"
"}")
        self.btn_Exel.setIcon(icon)
        self.btn_start_day = QPushButton(self.widget)
        self.btn_start_day.setObjectName(u"btn_start_day")
        self.btn_start_day.setGeometry(QRect(390, 160, 75, 24))
        self.btn_start_day.setStyleSheet(u"QPushButton:hover{\n"
"background-color:rgba(255,255,255,40)\n"
"}\n"
"QPushButton:pressed{\n"
"background-color:rgba(255,255,255,60)\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/icon/D:/games/\u0432\u043e\u0440\u043a/KP2/icon/start_24dp_E8EAED_FILL0_wght400_GRAD0_opsz24.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_start_day.setIcon(icon1)
        self.btn_end = QPushButton(self.widget)
        self.btn_end.setObjectName(u"btn_end")
        self.btn_end.setGeometry(QRect(510, 570, 75, 24))
        self.btn_end.setStyleSheet(u"QPushButton:hover{\n"
"background-color:rgba(255,255,255,40)\n"
"}\n"
"QPushButton:pressed{\n"
"background-color:rgba(255,255,255,60)\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u":/icon/D:/games/\u0432\u043e\u0440\u043a/KP2/icon/exit_to_app_24dp_E8EAED_FILL0_wght400_GRAD0_opsz24.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_end.setIcon(icon2)
        self.btn_end_day = QPushButton(self.widget)
        self.btn_end_day.setObjectName(u"btn_end_day")
        self.btn_end_day.setGeometry(QRect(470, 160, 111, 24))
        self.btn_end_day.setStyleSheet(u"QPushButton:hover{\n"
"background-color:rgba(255,255,255,40)\n"
"}\n"
"QPushButton:pressed{\n"
"background-color:rgba(255,255,255,60)\n"
"}")
        icon3 = QIcon()
        icon3.addFile(u":/icon/D:/games/\u0432\u043e\u0440\u043a/KP2/icon/pin_end_24dp_E8EAED_FILL0_wght400_GRAD0_opsz24.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_end_day.setIcon(icon3)
        self.btn_save = QPushButton(self.widget)
        self.btn_save.setObjectName(u"btn_save")
        self.btn_save.setGeometry(QRect(70, 570, 75, 24))
        self.btn_save.setStyleSheet(u"QPushButton:hover{\n"
"background-color:rgba(255,255,255,40)\n"
"}\n"
"QPushButton:pressed{\n"
"background-color:rgba(255,255,255,60)\n"
"}")
        self.btn_delete = QPushButton(self.widget)
        self.btn_delete.setObjectName(u"btn_delete")
        self.btn_delete.setGeometry(QRect(150, 570, 75, 24))
        self.btn_delete.setStyleSheet(u"QPushButton:hover{\n"
"background-color:rgba(255,255,255,40)\n"
"}\n"
"QPushButton:pressed{\n"
"background-color:rgba(255,255,255,60)\n"
"}")

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"\u0414\u043e\u0431\u0440\u044b\u0439 \u0434\u0435\u043d\u044c \u0410\u0434\u043c\u0438\u043d\u0438\u0441\u0442\u0440\u0430\u0442\u043e\u0440", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"                                                                \u0412\u0430\u0448 \u0444\u0443\u043d\u043a\u0446\u0438\u043e\u043d\u0430\u043b ", None))
        self.btn_otchet.setText(QCoreApplication.translate("Dialog", u"\u043e\u0442\u0447\u0435\u0442 ", None))
        self.btn_Exel.setText(QCoreApplication.translate("Dialog", u"\u0415\u0445\u0435\u043b\u044c", None))
        self.btn_start_day.setText(QCoreApplication.translate("Dialog", u"\u041d\u0430\u0447\u0430\u0442\u044c ", None))
        self.btn_end.setText(QCoreApplication.translate("Dialog", u"\u0412\u044b\u0445\u043e\u0434", None))
        self.btn_end_day.setText(QCoreApplication.translate("Dialog", u"\u0417\u0430\u043a\u043e\u043d\u0447\u0438\u0442\u044c ", None))
        self.btn_save.setText(QCoreApplication.translate("Dialog", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
        self.btn_delete.setText(QCoreApplication.translate("Dialog", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c", None))
    # retranslateUi

