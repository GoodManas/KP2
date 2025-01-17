# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_add_emploer.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QWidget)

class Ui_add(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(402, 287)
        Dialog.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0 rgba(	255, 0, 0, 255), stop:0.427447 rgba(139, 0, 0, 125), stop:1 rgba(155, 79, 165, 255));\n"
"font-famaly: Roboto Flex;")
        self.widget = QWidget(Dialog)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(-410, -180, 961, 571))
        self.widget.setStyleSheet(u"background-color:rgba(225,255,255,100);\n"
"border: 1px  solid rgba(225,255,255,40);\n"
"border-radius: 7px;")
        self.lineLogin = QLineEdit(self.widget)
        self.lineLogin.setObjectName(u"lineLogin")
        self.lineLogin.setGeometry(QRect(440, 300, 81, 22))
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(430, 210, 361, 21))
        self.btn_end = QPushButton(self.widget)
        self.btn_end.setObjectName(u"btn_end")
        self.btn_end.setGeometry(QRect(710, 420, 75, 24))
        self.btn_end.setStyleSheet(u"QPushButton{\n"
"color:black;\n"
"background-color:rgba(255,255,255,0);\n"
"}\n"
"QPushButton:hover{\n"
"background-color:rgba(255,255,255,40)\n"
"}\n"
"QPushButton:pressed{\n"
"background-color:rgba(255,255,255,60)\n"
"}")
        self.btn_save = QPushButton(self.widget)
        self.btn_save.setObjectName(u"btn_save")
        self.btn_save.setGeometry(QRect(630, 420, 75, 24))
        self.btn_save.setStyleSheet(u"QPushButton{\n"
"color:black;\n"
"background-color:rgba(255,255,255,0);\n"
"}\n"
"QPushButton:hover{\n"
"background-color:rgba(255,255,255,40)\n"
"}\n"
"QPushButton:pressed{\n"
"background-color:rgba(255,255,255,60)\n"
"}")
        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(430, 240, 361, 21))
        self.linePassword = QLineEdit(self.widget)
        self.linePassword.setObjectName(u"linePassword")
        self.linePassword.setGeometry(QRect(440, 330, 81, 22))
        self.lineDol = QLineEdit(self.widget)
        self.lineDol.setObjectName(u"lineDol")
        self.lineDol.setGeometry(QRect(440, 360, 81, 22))

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.lineLogin.setText("")
        self.label.setText(QCoreApplication.translate("Dialog", u"\u041f\u043e\u0436\u0430\u043b\u0443\u0439\u0441\u0442\u0430 \u0432\u0432\u0435\u0434\u0438\u0442\u0435 \u0434\u0430\u043d\u043d\u044b\u0435 \u043d\u043e\u0432\u043e\u0433\u043e \u0441\u043e\u0442\u0440\u0443\u0434\u043d\u0438\u043a\u0430 \u0447\u0435\u0440\u0435\u0437 \u0437\u0430\u043f\u044f\u0442\u0443\u044e", None))
        self.btn_end.setText(QCoreApplication.translate("Dialog", u"\u041e\u0442\u043c\u0435\u043d\u0430", None))
        self.btn_save.setText(QCoreApplication.translate("Dialog", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Login, password, dol", None))
        self.linePassword.setText("")
        self.lineDol.setText("")
    # retranslateUi

