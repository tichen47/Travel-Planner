# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialog.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(990, 562)
        Dialog.setMinimumSize(QtCore.QSize(804, 562))
        self.frame = QtWidgets.QFrame(Dialog)
        self.frame.setGeometry(QtCore.QRect(0, 0, 991, 561))
        self.frame.setStyleSheet("background-color: rgb(130, 237, 111);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.frame_12 = QtWidgets.QFrame(self.frame)
        self.frame_12.setGeometry(QtCore.QRect(0, 40, 171, 521))
        self.frame_12.setStyleSheet("background-color: rgba(108, 107, 108, 205);\n"
"border-radius: 8px;")
        self.frame_12.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_12.setObjectName("frame_12")
        self.frame_13 = QtWidgets.QFrame(self.frame_12)
        self.frame_13.setGeometry(QtCore.QRect(10, 50, 191, 171))
        self.frame_13.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.frame_13.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_13.setObjectName("frame_13")
        self.textEdit_13 = QtWidgets.QTextEdit(self.frame_13)
        self.textEdit_13.setGeometry(QtCore.QRect(0, 10, 191, 31))
        self.textEdit_13.setStyleSheet("border:0;")
        self.textEdit_13.setObjectName("textEdit_13")
        self.checkBox_30 = QtWidgets.QCheckBox(self.frame_13)
        self.checkBox_30.setGeometry(QtCore.QRect(10, 40, 161, 20))
        self.checkBox_30.setObjectName("checkBox_30")
        self.checkBox_31 = QtWidgets.QCheckBox(self.frame_13)
        self.checkBox_31.setGeometry(QtCore.QRect(10, 60, 161, 20))
        self.checkBox_31.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.checkBox_31.setObjectName("checkBox_31")
        self.checkBox_32 = QtWidgets.QCheckBox(self.frame_13)
        self.checkBox_32.setGeometry(QtCore.QRect(10, 80, 161, 20))
        self.checkBox_32.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.checkBox_32.setObjectName("checkBox_32")
        self.checkBox_33 = QtWidgets.QCheckBox(self.frame_13)
        self.checkBox_33.setGeometry(QtCore.QRect(10, 100, 171, 20))
        self.checkBox_33.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.checkBox_33.setObjectName("checkBox_33")
        self.checkBox_34 = QtWidgets.QCheckBox(self.frame_13)
        self.checkBox_34.setGeometry(QtCore.QRect(10, 120, 171, 20))
        self.checkBox_34.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.checkBox_34.setObjectName("checkBox_34")
        self.checkBox_35 = QtWidgets.QCheckBox(self.frame_13)
        self.checkBox_35.setGeometry(QtCore.QRect(10, 140, 161, 20))
        self.checkBox_35.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.checkBox_35.setObjectName("checkBox_35")
        self.frame_14 = QtWidgets.QFrame(self.frame_12)
        self.frame_14.setGeometry(QtCore.QRect(10, 230, 191, 141))
        self.frame_14.setStyleSheet("border: false;\n"
"background-color: rgba(255, 255, 255, 0);")
        self.frame_14.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_14.setObjectName("frame_14")
        self.textEdit_14 = QtWidgets.QTextEdit(self.frame_14)
        self.textEdit_14.setGeometry(QtCore.QRect(0, 10, 191, 31))
        self.textEdit_14.setStyleSheet("border:0;")
        self.textEdit_14.setObjectName("textEdit_14")
        self.checkBox_36 = QtWidgets.QCheckBox(self.frame_14)
        self.checkBox_36.setGeometry(QtCore.QRect(10, 40, 121, 20))
        self.checkBox_36.setObjectName("checkBox_36")
        self.checkBox_37 = QtWidgets.QCheckBox(self.frame_14)
        self.checkBox_37.setGeometry(QtCore.QRect(10, 60, 121, 20))
        self.checkBox_37.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.checkBox_37.setObjectName("checkBox_37")
        self.checkBox_38 = QtWidgets.QCheckBox(self.frame_14)
        self.checkBox_38.setGeometry(QtCore.QRect(10, 80, 111, 20))
        self.checkBox_38.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.checkBox_38.setObjectName("checkBox_38")
        self.checkBox_39 = QtWidgets.QCheckBox(self.frame_14)
        self.checkBox_39.setGeometry(QtCore.QRect(10, 100, 111, 20))
        self.checkBox_39.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.checkBox_39.setObjectName("checkBox_39")
        self.checkBox_40 = QtWidgets.QCheckBox(self.frame_14)
        self.checkBox_40.setGeometry(QtCore.QRect(10, 120, 111, 20))
        self.checkBox_40.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.checkBox_40.setObjectName("checkBox_40")
        self.textEdit_15 = QtWidgets.QTextEdit(self.frame_12)
        self.textEdit_15.setGeometry(QtCore.QRect(10, 0, 161, 41))
        self.textEdit_15.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"border-color: rgb(0, 0, 0);")
        self.textEdit_15.setObjectName("textEdit_15")
        self.pushButton_3 = QtWidgets.QPushButton(self.frame_12)
        self.pushButton_3.setGeometry(QtCore.QRect(30, 410, 113, 32))
        self.pushButton_3.setStyleSheet("background-color: rgb(184, 182, 185);")
        self.pushButton_3.setObjectName("pushButton_3")
        self.textEdit_18 = QtWidgets.QTextEdit(self.frame)
        self.textEdit_18.setGeometry(QtCore.QRect(390, -10, 291, 61))
        self.textEdit_18.setStyleSheet("background-color: rgba(254, 252, 255, 0);")
        self.textEdit_18.setObjectName("textEdit_18")
        self.textEdit_16 = QtWidgets.QTextEdit(self.frame)
        self.textEdit_16.setGeometry(QtCore.QRect(170, 40, 561, 41))
        self.textEdit_16.setStyleSheet("border-style: outset;\n"
"background-color: rgba(128, 0, 0, 218);\n"
"border-color: black;\n"
"border-width: 2px;\n"
"border-radius: 7px;")
        self.textEdit_16.setObjectName("textEdit_16")
        self.textEdit_19 = QtWidgets.QTextEdit(self.frame)
        self.textEdit_19.setGeometry(QtCore.QRect(730, 40, 261, 41))
        self.textEdit_19.setStyleSheet("border-style: outset;\n"
"background-color: rgba(128, 0, 0, 218);\n"
"border-color: black;\n"
"border-width: 2px;\n"
"border-radius: 7px;")
        self.textEdit_19.setObjectName("textEdit_19")
        self.textEdit = QtWidgets.QTextEdit(self.frame)
        self.textEdit.setGeometry(QtCore.QRect(170, 80, 561, 451))
        self.textEdit.setStyleSheet("background-color: rgba(255, 255, 255, 99);\n"
"border-style: outset;\n"
"border-color: black;\n"
"border-width: 2px;\n"
"border-radius: 8px;")
        self.textEdit.setObjectName("textEdit")
        self.textEdit_2 = QtWidgets.QTextEdit(self.frame)
        self.textEdit_2.setGeometry(QtCore.QRect(730, 80, 261, 481))
        self.textEdit_2.setStyleSheet("background-color: rgba(255, 255, 255, 99);\n"
"border-style: outset;\n"
"border-color: black;\n"
"border-width: 2px;\n"
"border-radius: 8px;")
        self.textEdit_2.setObjectName("textEdit_2")
        self.widget = QtWidgets.QWidget(self.frame)
        self.widget.setGeometry(QtCore.QRect(730, 80, 261, 91))
        self.widget.setStyleSheet("background-color: rgba(255, 255, 255, 99);\n"
"border-style: outset;\n"
"border-color: black;\n"
"border-width: 2px;\n"
"border-radius: 5px;")
        self.widget.setObjectName("widget")
        self.textEdit_4 = QtWidgets.QTextEdit(self.widget)
        self.textEdit_4.setGeometry(QtCore.QRect(200, 30, 61, 31))
        self.textEdit_4.setStyleSheet("background-color: rgba(255, 255, 255, 0);border-style: outset;\n"
"border-color: black;\n"
"border-width: 1px;\n"
"border-radius: 3px;")
        self.textEdit_4.setObjectName("textEdit_4")
        self.textEdit_5 = QtWidgets.QTextEdit(self.widget)
        self.textEdit_5.setGeometry(QtCore.QRect(200, 0, 61, 31))
        self.textEdit_5.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"border-style: outset;\n"
"border-color: black;\n"
"border-width: 1px;\n"
"border-radius: 3px;")
        self.textEdit_5.setObjectName("textEdit_5")
        self.textEdit_3 = QtWidgets.QTextEdit(self.widget)
        self.textEdit_3.setGeometry(QtCore.QRect(0, 60, 261, 31))
        self.textEdit_3.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"border-style: outset;\n"
"border-color: black;\n"
"border-width: 1px;\n"
"border-radius: 3px;")
        self.textEdit_3.setObjectName("textEdit_3")
        self.textBrowser = QtWidgets.QTextBrowser(self.widget)
        self.textBrowser.setGeometry(QtCore.QRect(0, 0, 201, 61))
        self.textBrowser.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"border-style: outset;\n"
"border-color: black;\n"
"border-width: 1px;\n"
"border-radius: 5px;")
        self.textBrowser.setObjectName("textBrowser")
        self.widget_2 = QtWidgets.QWidget(self.frame)
        self.widget_2.setGeometry(QtCore.QRect(730, 170, 261, 91))
        self.widget_2.setStyleSheet("background-color: rgba(255, 255, 255, 99);\n"
"border-style: outset;\n"
"border-color: black;\n"
"border-width: 2px;\n"
"border-radius: 3px;")
        self.widget_2.setObjectName("widget_2")
        self.textBrowser_7 = QtWidgets.QTextBrowser(self.widget_2)
        self.textBrowser_7.setGeometry(QtCore.QRect(0, 0, 201, 61))
        self.textBrowser_7.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"border-style: outset;\n"
"border-color: black;\n"
"border-width: 1px;\n"
"border-radius: 3px;")
        self.textBrowser_7.setObjectName("textBrowser_7")
        self.textEdit_27 = QtWidgets.QTextEdit(self.widget_2)
        self.textEdit_27.setGeometry(QtCore.QRect(200, 30, 61, 31))
        self.textEdit_27.setStyleSheet("background-color: rgba(255, 255, 255, 0);border-style: outset;\n"
"border-color: black;\n"
"border-width: 1px;\n"
"border-radius: 3px;")
        self.textEdit_27.setObjectName("textEdit_27")
        self.textEdit_28 = QtWidgets.QTextEdit(self.widget_2)
        self.textEdit_28.setGeometry(QtCore.QRect(200, 0, 61, 31))
        self.textEdit_28.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"border-style: outset;\n"
"border-color: black;\n"
"border-width: 1px;\n"
"border-radius: 3px;")
        self.textEdit_28.setObjectName("textEdit_28")
        self.textEdit_29 = QtWidgets.QTextEdit(self.widget_2)
        self.textEdit_29.setGeometry(QtCore.QRect(0, 60, 261, 31))
        self.textEdit_29.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"border-style: outset;\n"
"border-color: black;\n"
"border-width: 1px;\n"
"border-radius: 3px;")
        self.textEdit_29.setObjectName("textEdit_29")
        self.textEdit_27.raise_()
        self.textEdit_28.raise_()
        self.textEdit_29.raise_()
        self.textBrowser_7.raise_()
        self.widget_3 = QtWidgets.QWidget(self.frame)
        self.widget_3.setGeometry(QtCore.QRect(730, 260, 261, 101))
        self.widget_3.setStyleSheet("background-color: rgba(255, 255, 255, 99);\n"
"border-style: outset;\n"
"border-color: black;\n"
"border-width: 2px;\n"
"border-radius: 3px;")
        self.widget_3.setObjectName("widget_3")
        self.textBrowser_8 = QtWidgets.QTextBrowser(self.widget_3)
        self.textBrowser_8.setGeometry(QtCore.QRect(0, 0, 201, 71))
        self.textBrowser_8.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"border-style: outset;\n"
"border-color: black;\n"
"border-width: 1px;\n"
"border-radius: 3px;")
        self.textBrowser_8.setObjectName("textBrowser_8")
        self.textEdit_30 = QtWidgets.QTextEdit(self.widget_3)
        self.textEdit_30.setGeometry(QtCore.QRect(200, 30, 61, 41))
        self.textEdit_30.setStyleSheet("background-color: rgba(255, 255, 255, 0);border-style: outset;\n"
"border-color: black;\n"
"border-width: 1px;\n"
"border-radius: 3px;")
        self.textEdit_30.setObjectName("textEdit_30")
        self.textEdit_31 = QtWidgets.QTextEdit(self.widget_3)
        self.textEdit_31.setGeometry(QtCore.QRect(200, 0, 61, 31))
        self.textEdit_31.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"border-style: outset;\n"
"border-color: black;\n"
"border-width: 1px;\n"
"border-radius: 3px;")
        self.textEdit_31.setObjectName("textEdit_31")
        self.textEdit_32 = QtWidgets.QTextEdit(self.widget_3)
        self.textEdit_32.setGeometry(QtCore.QRect(0, 70, 261, 31))
        self.textEdit_32.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"border-style: outset;\n"
"border-color: black;\n"
"border-width: 1px;\n"
"border-radius: 3px;")
        self.textEdit_32.setObjectName("textEdit_32")
        self.textEdit_30.raise_()
        self.textEdit_31.raise_()
        self.textEdit_32.raise_()
        self.textBrowser_8.raise_()
        self.widget_4 = QtWidgets.QWidget(self.frame)
        self.widget_4.setGeometry(QtCore.QRect(730, 360, 261, 101))
        self.widget_4.setStyleSheet("background-color: rgba(255, 255, 255, 99);\n"
"border-style: outset;\n"
"border-color: black;\n"
"border-width: 2px;\n"
"border-radius: 3px;")
        self.widget_4.setObjectName("widget_4")
        self.textBrowser_10 = QtWidgets.QTextBrowser(self.widget_4)
        self.textBrowser_10.setGeometry(QtCore.QRect(0, 0, 201, 71))
        self.textBrowser_10.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"border-style: outset;\n"
"border-color: black;\n"
"border-width: 1px;\n"
"border-radius: 3px;")
        self.textBrowser_10.setObjectName("textBrowser_10")
        self.textEdit_36 = QtWidgets.QTextEdit(self.widget_4)
        self.textEdit_36.setGeometry(QtCore.QRect(200, 30, 61, 41))
        self.textEdit_36.setStyleSheet("background-color: rgba(255, 255, 255, 0);border-style: outset;\n"
"border-color: black;\n"
"border-width: 1px;\n"
"border-radius: 3px;")
        self.textEdit_36.setObjectName("textEdit_36")
        self.textEdit_37 = QtWidgets.QTextEdit(self.widget_4)
        self.textEdit_37.setGeometry(QtCore.QRect(200, 0, 61, 31))
        self.textEdit_37.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"border-style: outset;\n"
"border-color: black;\n"
"border-width: 1px;\n"
"border-radius: 3px;")
        self.textEdit_37.setObjectName("textEdit_37")
        self.textEdit_38 = QtWidgets.QTextEdit(self.widget_4)
        self.textEdit_38.setGeometry(QtCore.QRect(0, 70, 261, 31))
        self.textEdit_38.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"border-style: outset;\n"
"border-color: black;\n"
"border-width: 1px;\n"
"border-radius: 3px;")
        self.textEdit_38.setObjectName("textEdit_38")
        self.textEdit_36.raise_()
        self.textEdit_37.raise_()
        self.textEdit_38.raise_()
        self.textBrowser_10.raise_()
        self.widget_5 = QtWidgets.QWidget(self.frame)
        self.widget_5.setGeometry(QtCore.QRect(730, 460, 261, 101))
        self.widget_5.setStyleSheet("background-color: rgba(255, 255, 255, 99);\n"
"border-style: outset;\n"
"border-color: black;\n"
"border-width: 2px;\n"
"border-radius: 3px;")
        self.widget_5.setObjectName("widget_5")
        self.textBrowser_12 = QtWidgets.QTextBrowser(self.widget_5)
        self.textBrowser_12.setGeometry(QtCore.QRect(0, 0, 201, 71))
        self.textBrowser_12.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"border-style: outset;\n"
"border-color: black;\n"
"border-width: 1px;\n"
"border-radius: 3px;")
        self.textBrowser_12.setObjectName("textBrowser_12")
        self.textEdit_42 = QtWidgets.QTextEdit(self.widget_5)
        self.textEdit_42.setGeometry(QtCore.QRect(200, 30, 61, 41))
        self.textEdit_42.setStyleSheet("background-color: rgba(255, 255, 255, 0);border-style: outset;\n"
"border-color: black;\n"
"border-width: 1px;\n"
"border-radius: 3px;")
        self.textEdit_42.setObjectName("textEdit_42")
        self.textEdit_43 = QtWidgets.QTextEdit(self.widget_5)
        self.textEdit_43.setGeometry(QtCore.QRect(200, 0, 61, 31))
        self.textEdit_43.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"border-style: outset;\n"
"border-color: black;\n"
"border-width: 1px;\n"
"border-radius: 3px;")
        self.textEdit_43.setObjectName("textEdit_43")
        self.textEdit_44 = QtWidgets.QTextEdit(self.widget_5)
        self.textEdit_44.setGeometry(QtCore.QRect(0, 70, 261, 31))
        self.textEdit_44.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"border-style: outset;\n"
"border-color: black;\n"
"border-width: 1px;\n"
"border-radius: 3px;")
        self.textEdit_44.setObjectName("textEdit_44")
        self.textEdit_42.raise_()
        self.textEdit_43.raise_()
        self.textEdit_44.raise_()
        self.textBrowser_12.raise_()
        self.frame_7 = QtWidgets.QFrame(self.frame)
        self.frame_7.setGeometry(QtCore.QRect(170, 80, 561, 121))
        self.frame_7.setStyleSheet("background-color: rgba(255, 255, 255, 102);\n"
"border-style: outset;\n"
"border-color: black;\n"
"border-width: 2px;\n"
"border-radius: 8px;")
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.textEdit_65 = QtWidgets.QTextEdit(self.frame_7)
        self.textEdit_65.setGeometry(QtCore.QRect(0, 0, 71, 31))
        self.textEdit_65.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"border:false;")
        self.textEdit_65.setObjectName("textEdit_65")
        self.textEdit_66 = QtWidgets.QTextEdit(self.frame_7)
        self.textEdit_66.setGeometry(QtCore.QRect(220, 60, 211, 31))
        self.textEdit_66.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"border:false;")
        self.textEdit_66.setObjectName("textEdit_66")
        self.textEdit_67 = QtWidgets.QTextEdit(self.frame_7)
        self.textEdit_67.setGeometry(QtCore.QRect(0, 60, 221, 31))
        self.textEdit_67.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"border:false;")
        self.textEdit_67.setObjectName("textEdit_67")
        self.textEdit_68 = QtWidgets.QTextEdit(self.frame_7)
        self.textEdit_68.setGeometry(QtCore.QRect(220, 0, 211, 31))
        self.textEdit_68.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"border:false;")
        self.textEdit_68.setObjectName("textEdit_68")
        self.pushButton_7 = QtWidgets.QPushButton(self.frame_7)
        self.pushButton_7.setGeometry(QtCore.QRect(530, 0, 31, 32))
        self.pushButton_7.setStyleSheet("background-color: rgba(105, 156, 213, 217);")
        self.pushButton_7.setObjectName("pushButton_7")
        self.textEdit_69 = QtWidgets.QTextEdit(self.frame_7)
        self.textEdit_69.setGeometry(QtCore.QRect(0, 80, 561, 41))
        self.textEdit_69.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"border:false;")
        self.textEdit_69.setObjectName("textEdit_69")
        self.textBrowser_17 = QtWidgets.QTextBrowser(self.frame_7)
        self.textBrowser_17.setGeometry(QtCore.QRect(0, 20, 561, 41))
        self.textBrowser_17.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"border:false;")
        self.textBrowser_17.setObjectName("textBrowser_17")
        self.label_6 = QtWidgets.QLabel(self.frame_7)
        self.label_6.setGeometry(QtCore.QRect(430, 0, 131, 121))
        self.label_6.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"border-radius: 8px;\n"
"border:false;")
        self.label_6.setObjectName("label_6")
        self.label_6.raise_()
        self.textEdit_65.raise_()
        self.textEdit_66.raise_()
        self.textEdit_67.raise_()
        self.textEdit_68.raise_()
        self.textEdit_69.raise_()
        self.textBrowser_17.raise_()
        self.pushButton_7.raise_()
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(170, 530, 113, 32))
        self.pushButton.setStyleSheet("border-style: outset;\n"
"background-color: rgba(212, 171, 0, 230);\n"
"border-color: black;\n"
"border-width: 2px;\n"
"border-radius: 7px;")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame)
        self.pushButton_2.setGeometry(QtCore.QRect(620, 530, 111, 31))
        self.pushButton_2.setStyleSheet("border-style: outset;\n"
"background-color: rgba(212, 171, 0, 230);\n"
"border-color: black;\n"
"border-width: 2px;\n"
"border-radius: 7px;")
        self.pushButton_2.setObjectName("pushButton_2")
        self.frame_8 = QtWidgets.QFrame(self.frame)
        self.frame_8.setGeometry(QtCore.QRect(170, 200, 561, 111))
        self.frame_8.setStyleSheet("background-color: rgba(255, 255, 255, 102);\n"
"border-style: outset;\n"
"border-color: black;\n"
"border-width: 2px;\n"
"border-radius: 8px;")
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.textEdit_70 = QtWidgets.QTextEdit(self.frame_8)
        self.textEdit_70.setGeometry(QtCore.QRect(0, 0, 71, 31))
        self.textEdit_70.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"border:false;")
        self.textEdit_70.setObjectName("textEdit_70")
        self.textEdit_71 = QtWidgets.QTextEdit(self.frame_8)
        self.textEdit_71.setGeometry(QtCore.QRect(220, 50, 211, 31))
        self.textEdit_71.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"border:false;")
        self.textEdit_71.setObjectName("textEdit_71")
        self.textEdit_72 = QtWidgets.QTextEdit(self.frame_8)
        self.textEdit_72.setGeometry(QtCore.QRect(0, 50, 221, 31))
        self.textEdit_72.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"border:false;")
        self.textEdit_72.setObjectName("textEdit_72")
        self.textEdit_73 = QtWidgets.QTextEdit(self.frame_8)
        self.textEdit_73.setGeometry(QtCore.QRect(220, 0, 211, 31))
        self.textEdit_73.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"border:false;")
        self.textEdit_73.setObjectName("textEdit_73")
        self.pushButton_8 = QtWidgets.QPushButton(self.frame_8)
        self.pushButton_8.setGeometry(QtCore.QRect(530, 0, 31, 32))
        self.pushButton_8.setStyleSheet("background-color: rgba(105, 156, 213, 217);")
        self.pushButton_8.setObjectName("pushButton_8")
        self.textEdit_74 = QtWidgets.QTextEdit(self.frame_8)
        self.textEdit_74.setGeometry(QtCore.QRect(0, 70, 561, 41))
        self.textEdit_74.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"border:false;")
        self.textEdit_74.setObjectName("textEdit_74")
        self.textBrowser_18 = QtWidgets.QTextBrowser(self.frame_8)
        self.textBrowser_18.setGeometry(QtCore.QRect(0, 20, 561, 41))
        self.textBrowser_18.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"border:false;")
        self.textBrowser_18.setObjectName("textBrowser_18")
        self.label_7 = QtWidgets.QLabel(self.frame_8)
        self.label_7.setGeometry(QtCore.QRect(430, 0, 131, 111))
        self.label_7.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"border-radius: 8px;\n"
"border:false;")
        self.label_7.setObjectName("label_7")
        self.label_7.raise_()
        self.textEdit_70.raise_()
        self.textEdit_71.raise_()
        self.textEdit_72.raise_()
        self.textEdit_73.raise_()
        self.textEdit_74.raise_()
        self.textBrowser_18.raise_()
        self.pushButton_8.raise_()
        self.frame_9 = QtWidgets.QFrame(self.frame)
        self.frame_9.setGeometry(QtCore.QRect(170, 310, 561, 111))
        self.frame_9.setStyleSheet("background-color: rgba(255, 255, 255, 102);\n"
"border-style: outset;\n"
"border-color: black;\n"
"border-width: 2px;\n"
"border-radius: 8px;")
        self.frame_9.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_9.setObjectName("frame_9")
        self.textEdit_75 = QtWidgets.QTextEdit(self.frame_9)
        self.textEdit_75.setGeometry(QtCore.QRect(0, 0, 71, 31))
        self.textEdit_75.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"border:false;")
        self.textEdit_75.setObjectName("textEdit_75")
        self.textEdit_76 = QtWidgets.QTextEdit(self.frame_9)
        self.textEdit_76.setGeometry(QtCore.QRect(220, 50, 211, 31))
        self.textEdit_76.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"border:false;")
        self.textEdit_76.setObjectName("textEdit_76")
        self.textEdit_77 = QtWidgets.QTextEdit(self.frame_9)
        self.textEdit_77.setGeometry(QtCore.QRect(0, 50, 221, 31))
        self.textEdit_77.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"border:false;")
        self.textEdit_77.setObjectName("textEdit_77")
        self.textEdit_78 = QtWidgets.QTextEdit(self.frame_9)
        self.textEdit_78.setGeometry(QtCore.QRect(220, 0, 211, 31))
        self.textEdit_78.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"border:false;")
        self.textEdit_78.setObjectName("textEdit_78")
        self.pushButton_9 = QtWidgets.QPushButton(self.frame_9)
        self.pushButton_9.setGeometry(QtCore.QRect(530, 0, 31, 32))
        self.pushButton_9.setStyleSheet("background-color: rgba(105, 156, 213, 217);")
        self.pushButton_9.setObjectName("pushButton_9")
        self.textEdit_79 = QtWidgets.QTextEdit(self.frame_9)
        self.textEdit_79.setGeometry(QtCore.QRect(0, 70, 561, 41))
        self.textEdit_79.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"border:false;")
        self.textEdit_79.setObjectName("textEdit_79")
        self.textBrowser_19 = QtWidgets.QTextBrowser(self.frame_9)
        self.textBrowser_19.setGeometry(QtCore.QRect(0, 20, 561, 41))
        self.textBrowser_19.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"border:false;")
        self.textBrowser_19.setObjectName("textBrowser_19")
        self.label_8 = QtWidgets.QLabel(self.frame_9)
        self.label_8.setGeometry(QtCore.QRect(430, 0, 131, 111))
        self.label_8.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"border-radius: 8px;\n"
"border:false;")
        self.label_8.setObjectName("label_8")
        self.label_8.raise_()
        self.textEdit_75.raise_()
        self.textEdit_76.raise_()
        self.textEdit_77.raise_()
        self.textEdit_78.raise_()
        self.textEdit_79.raise_()
        self.textBrowser_19.raise_()
        self.pushButton_9.raise_()
        self.frame_10 = QtWidgets.QFrame(self.frame)
        self.frame_10.setGeometry(QtCore.QRect(170, 420, 561, 111))
        self.frame_10.setStyleSheet("background-color: rgba(255, 255, 255, 102);\n"
"border-style: outset;\n"
"border-color: black;\n"
"border-width: 2px;\n"
"border-radius: 8px;")
        self.frame_10.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_10.setObjectName("frame_10")
        self.textEdit_80 = QtWidgets.QTextEdit(self.frame_10)
        self.textEdit_80.setGeometry(QtCore.QRect(0, 0, 71, 31))
        self.textEdit_80.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"border:false;")
        self.textEdit_80.setObjectName("textEdit_80")
        self.textEdit_81 = QtWidgets.QTextEdit(self.frame_10)
        self.textEdit_81.setGeometry(QtCore.QRect(220, 50, 211, 31))
        self.textEdit_81.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"border:false;")
        self.textEdit_81.setObjectName("textEdit_81")
        self.textEdit_82 = QtWidgets.QTextEdit(self.frame_10)
        self.textEdit_82.setGeometry(QtCore.QRect(0, 50, 221, 31))
        self.textEdit_82.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"border:false;")
        self.textEdit_82.setObjectName("textEdit_82")
        self.textEdit_83 = QtWidgets.QTextEdit(self.frame_10)
        self.textEdit_83.setGeometry(QtCore.QRect(220, 0, 211, 31))
        self.textEdit_83.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"border:false;")
        self.textEdit_83.setObjectName("textEdit_83")
        self.pushButton_10 = QtWidgets.QPushButton(self.frame_10)
        self.pushButton_10.setGeometry(QtCore.QRect(530, 0, 31, 32))
        self.pushButton_10.setStyleSheet("background-color: rgba(105, 156, 213, 217);")
        self.pushButton_10.setObjectName("pushButton_10")
        self.textEdit_84 = QtWidgets.QTextEdit(self.frame_10)
        self.textEdit_84.setGeometry(QtCore.QRect(0, 70, 561, 41))
        self.textEdit_84.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"border:false;")
        self.textEdit_84.setObjectName("textEdit_84")
        self.textBrowser_20 = QtWidgets.QTextBrowser(self.frame_10)
        self.textBrowser_20.setGeometry(QtCore.QRect(0, 20, 561, 41))
        self.textBrowser_20.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"border:false;")
        self.textBrowser_20.setObjectName("textBrowser_20")
        self.label_9 = QtWidgets.QLabel(self.frame_10)
        self.label_9.setGeometry(QtCore.QRect(430, 0, 131, 111))
        self.label_9.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"border-radius: 8px;\n"
"border:false;")
        self.label_9.setObjectName("label_9")
        self.label_9.raise_()
        self.textEdit_80.raise_()
        self.textEdit_81.raise_()
        self.textEdit_82.raise_()
        self.textEdit_83.raise_()
        self.textEdit_84.raise_()
        self.textBrowser_20.raise_()
        self.pushButton_10.raise_()
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(0, -10, 991, 581))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("ASD_Fotor.png"))
        self.label.setObjectName("label")
        self.label.raise_()
        self.frame_12.raise_()
        self.textEdit_18.raise_()
        self.textEdit_16.raise_()
        self.textEdit_19.raise_()
        self.textEdit.raise_()
        self.textEdit_2.raise_()
        self.widget.raise_()
        self.widget_2.raise_()
        self.widget_3.raise_()
        self.widget_4.raise_()
        self.widget_5.raise_()
        self.frame_7.raise_()
        self.frame_8.raise_()
        self.frame_9.raise_()
        self.frame_10.raise_()
        self.pushButton.raise_()
        self.pushButton_2.raise_()

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.textEdit_13.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.SF NS Text\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; font-weight:600; color:#000000;\">  Activity：</span></p></body></html>"))
        self.checkBox_30.setText(_translate("Dialog", "     Nature"))
        self.checkBox_31.setText(_translate("Dialog", "     Religious"))
        self.checkBox_32.setText(_translate("Dialog", "     Theatre"))
        self.checkBox_33.setText(_translate("Dialog", "     Shopping"))
        self.checkBox_34.setText(_translate("Dialog", "     Picnic"))
        self.checkBox_35.setText(_translate("Dialog", "     Sports"))
        self.textEdit_14.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.SF NS Text\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; font-weight:600; color:#6c6c6c;\">  </span><span style=\" font-size:14pt; font-weight:600; color:#000000;\">Rating：</span></p></body></html>"))
        self.checkBox_36.setText(_translate("Dialog", "     above 4.5"))
        self.checkBox_37.setText(_translate("Dialog", "     above 4.0"))
        self.checkBox_38.setText(_translate("Dialog", "     above 3.5"))
        self.checkBox_39.setText(_translate("Dialog", "     above 3.0"))
        self.checkBox_40.setText(_translate("Dialog", "     above 2.5"))
        self.textEdit_15.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.SF NS Text\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24pt; color:#000000;\">  Filter  :</span></p></body></html>"))
        self.pushButton_3.setText(_translate("Dialog", "Search"))
        self.textEdit_18.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.SF NS Text\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:36pt; font-weight:600;\">Travel Planner</span></p></body></html>"))
        self.textEdit_16.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.SF NS Text\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24pt; color:#fdfdff;\">Best-fit Plan</span></p></body></html>"))
        self.textEdit_19.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.SF NS Text\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24pt; color:#fdfdff;\">Restaurants</span></p></body></html>"))
        self.textEdit_4.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.SF NS Text\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"right\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">4.7/5.0</p></body></html>"))
        self.textEdit_5.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.SF NS Text\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"right\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\">$$$$</span></p></body></html>"))
        self.textEdit_3.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.SF NS Text\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\">Tel:</span></p></body></html>"))
        self.textBrowser.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.SF NS Text\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; text-decoration: underline; color:#4275ad;\">Name</span></p></body></html>"))
        self.textBrowser_7.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.SF NS Text\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; text-decoration: underline; color:#4275ad;\">Name</span></p></body></html>"))
        self.textEdit_27.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.SF NS Text\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"right\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">4.7/5.0</p></body></html>"))
        self.textEdit_28.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.SF NS Text\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"right\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\">$$$$</span></p></body></html>"))
        self.textEdit_29.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.SF NS Text\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\">Tel:</span></p></body></html>"))
        self.textBrowser_8.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.SF NS Text\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; text-decoration: underline; color:#4275ad;\">Name</span></p></body></html>"))
        self.textEdit_30.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.SF NS Text\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"right\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">4.7/5.0</p></body></html>"))
        self.textEdit_31.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.SF NS Text\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"right\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\">$$$$</span></p></body></html>"))
        self.textEdit_32.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.SF NS Text\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\">Tel:</span></p></body></html>"))
        self.textBrowser_10.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.SF NS Text\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; text-decoration: underline; color:#4275ad;\">Name</span></p></body></html>"))
        self.textEdit_36.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.SF NS Text\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"right\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">4.7/5.0</p></body></html>"))
        self.textEdit_37.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.SF NS Text\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"right\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\">$$$$</span></p></body></html>"))
        self.textEdit_38.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.SF NS Text\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\">Tel:</span></p></body></html>"))
        self.textBrowser_12.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.SF NS Text\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; text-decoration: underline; color:#4275ad;\">Name</span></p></body></html>"))
        self.textEdit_42.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.SF NS Text\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"right\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">4.7/5.0</p></body></html>"))
        self.textEdit_43.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.SF NS Text\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"right\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\">$$$$</span></p></body></html>"))
        self.textEdit_44.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.SF NS Text\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\">Tel:</span></p></body></html>"))
        self.textEdit_65.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.SF NS Text\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; color:#191819;\">Day</span></p></body></html>"))
        self.textEdit_66.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.SF NS Text\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; color:#000000;\">Rating</span></p></body></html>"))
        self.textEdit_67.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.SF NS Text\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; color:#000000;\">Phone</span></p></body></html>"))
        self.textEdit_68.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.SF NS Text\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; color:#000000;\">Type</span></p></body></html>"))
        self.pushButton_7.setText(_translate("Dialog", "->"))
        self.textEdit_69.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.SF NS Text\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; color:#000000;\">Address</span></p></body></html>"))
        self.textBrowser_17.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.SF NS Text\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" text-decoration: underline; color:#405aae;\">Name</span></p></body></html>"))
        self.label_6.setText(_translate("Dialog", "  Photo"))
        self.pushButton.setText(_translate("Dialog", "< Previous"))
        self.pushButton_2.setText(_translate("Dialog", "Next >"))
        self.textEdit_70.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.SF NS Text\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; color:#191819;\">Day</span></p></body></html>"))
        self.textEdit_71.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.SF NS Text\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; color:#000000;\">Rating</span></p></body></html>"))
        self.textEdit_72.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.SF NS Text\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; color:#000000;\">Phone</span></p></body></html>"))
        self.textEdit_73.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.SF NS Text\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; color:#000000;\">Type</span></p></body></html>"))
        self.pushButton_8.setText(_translate("Dialog", "->"))
        self.textEdit_74.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.SF NS Text\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; color:#000000;\">Address</span></p></body></html>"))
        self.textBrowser_18.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.SF NS Text\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" text-decoration: underline; color:#405aae;\">Name</span></p></body></html>"))
        self.label_7.setText(_translate("Dialog", "  Photo"))
        self.textEdit_75.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.SF NS Text\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; color:#191819;\">Day</span></p></body></html>"))
        self.textEdit_76.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.SF NS Text\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; color:#000000;\">Rating</span></p></body></html>"))
        self.textEdit_77.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.SF NS Text\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; color:#000000;\">Phone</span></p></body></html>"))
        self.textEdit_78.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.SF NS Text\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; color:#000000;\">Type</span></p></body></html>"))
        self.pushButton_9.setText(_translate("Dialog", "->"))
        self.textEdit_79.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.SF NS Text\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; color:#000000;\">Address</span></p></body></html>"))
        self.textBrowser_19.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.SF NS Text\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" text-decoration: underline; color:#405aae;\">Name</span></p></body></html>"))
        self.label_8.setText(_translate("Dialog", "  Photo"))
        self.textEdit_80.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.SF NS Text\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; color:#191819;\">Day</span></p></body></html>"))
        self.textEdit_81.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.SF NS Text\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; color:#000000;\">Rating</span></p></body></html>"))
        self.textEdit_82.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.SF NS Text\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; color:#000000;\">Phone</span></p></body></html>"))
        self.textEdit_83.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.SF NS Text\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; color:#000000;\">Type</span></p></body></html>"))
        self.pushButton_10.setText(_translate("Dialog", "->"))
        self.textEdit_84.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.SF NS Text\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; color:#000000;\">Address</span></p></body></html>"))
        self.textBrowser_20.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.SF NS Text\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" text-decoration: underline; color:#405aae;\">Name</span></p></body></html>"))
        self.label_9.setText(_translate("Dialog", "  Photo"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
