# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_delete_emp.ui'
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

class Ui_delete(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(400, 300)
        Dialog.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0 rgba(	255, 0, 0, 255), stop:0.427447 rgba(139, 0, 0, 125), stop:1 rgba(155, 79, 165, 255));\n"
"font-famaly: Roboto Flex;")
        self.widget_2 = QWidget(Dialog)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setGeometry(QRect(-410, -170, 961, 571))
        self.widget_2.setStyleSheet(u"background-color:rgba(225,255,255,100);\n"
"border: 1px  solid rgba(225,255,255,40);\n"
"border-radius: 7px;")
        self.lineID = QLineEdit(self.widget_2)
        self.lineID.setObjectName(u"lineID")
        self.lineID.setGeometry(QRect(440, 300, 81, 22))
        self.label_3 = QLabel(self.widget_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(430, 210, 371, 21))
        self.btn_end = QPushButton(self.widget_2)
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
        self.btn_delete = QPushButton(self.widget_2)
        self.btn_delete.setObjectName(u"btn_delete")
        self.btn_delete.setGeometry(QRect(630, 420, 75, 24))
        self.btn_delete.setStyleSheet(u"QPushButton{\n"
"color:black;\n"
"background-color:rgba(255,255,255,0);\n"
"}\n"
"QPushButton:hover{\n"
"background-color:rgba(255,255,255,40)\n"
"}\n"
"QPushButton:pressed{\n"
"background-color:rgba(255,255,255,60)\n"
"}")
        self.label_4 = QLabel(self.widget_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(430, 240, 361, 21))

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.lineID.setText("")
        self.label_3.setText(QCoreApplication.translate("Dialog", u"\u041f\u043e\u0436\u0430\u043b\u0443\u0439\u0441\u0442\u0430 \u0432\u0432\u0435\u0434\u0438\u0442\u0435 ID \u041f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044f \u043a\u043e\u0442\u043e\u0440\u043e\u0433\u043e \u0445\u043e\u0442\u0438\u0442\u0435 \u0443\u0434\u0430\u043b\u0438\u0442\u044c", None))
        self.btn_end.setText(QCoreApplication.translate("Dialog", u"\u041e\u0442\u043c\u0435\u043d\u0430", None))
        self.btn_delete.setText(QCoreApplication.translate("Dialog", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"ID", None))
    # retranslateUi

