# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'travelMenupt3.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1001, 604)
        MainWindow.setStyleSheet("background-image: url(:/desktop/resources/bg.jpg);\n"
"border: 0;\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(240, 130, 511, 261))
        self.frame.setStyleSheet("background-color: rgba(253, 255, 255, 99);\n"
"border-style: outset;\n"
"border-color: black;\n"
"border-width: 2px;\n"
"border-radius: 7px;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(450, 60, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: rgb(158, 160, 160);")
        self.pushButton.setObjectName("pushButton")
        self.textEdit_3 = QtWidgets.QTextEdit(self.frame)
        self.textEdit_3.setGeometry(QtCore.QRect(20, 160, 81, 41))
        self.textEdit_3.setStyleSheet("border: false;\n"
"background-color: rgba(255, 255, 255, 0);")
        self.textEdit_3.setObjectName("textEdit_3")
        self.textEdit_4 = QtWidgets.QTextEdit(self.frame)
        self.textEdit_4.setGeometry(QtCore.QRect(250, 200, 41, 31))
        self.textEdit_4.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"border:false")
        self.textEdit_4.setObjectName("textEdit_4")
        self.textEdit_6 = QtWidgets.QTextEdit(self.frame)
        self.textEdit_6.setGeometry(QtCore.QRect(0, 20, 191, 41))
        self.textEdit_6.setStyleSheet("background-color: rgba(253, 250, 255, 0);\n"
"border: false")
        self.textEdit_6.setObjectName("textEdit_6")
        self.textEdit_5 = QtWidgets.QTextEdit(self.frame)
        self.textEdit_5.setGeometry(QtCore.QRect(20, 200, 81, 31))
        self.textEdit_5.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"border: false")
        self.textEdit_5.setObjectName("textEdit_5")
        self.textEdit_2 = QtWidgets.QTextEdit(self.frame)
        self.textEdit_2.setGeometry(QtCore.QRect(20, 60, 211, 31))
        self.textEdit_2.setStyleSheet("background-color: rgba(255, 255, 255, 191);")
        self.textEdit_2.setObjectName("textEdit_2")
        self.comboBox = QtWidgets.QComboBox(self.frame)
        self.comboBox.setGeometry(QtCore.QRect(250, 60, 161, 31))
        self.comboBox.setStyleSheet("background-color: rgba(255, 255, 255, 194);")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.frame_3 = QtWidgets.QFrame(self.frame)
        self.frame_3.setGeometry(QtCore.QRect(20, 100, 201, 21))
        self.frame_3.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"border-style: outset;\n"
"border-color: black;\n"
"border-width: 1px;\n"
"border-radius: 4px;")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.pushButton_3 = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_3.setGeometry(QtCore.QRect(180, 0, 21, 21))
        self.pushButton_3.setStyleSheet("border: false")
        self.pushButton_3.setObjectName("pushButton_3")
        self.textEdit_7 = QtWidgets.QTextEdit(self.frame_3)
        self.textEdit_7.setGeometry(QtCore.QRect(0, 0, 171, 31))
        self.textEdit_7.setStyleSheet("border:false")
        self.textEdit_7.setObjectName("textEdit_7")
        self.frame_4 = QtWidgets.QFrame(self.frame_3)
        self.frame_4.setGeometry(QtCore.QRect(180, 20, 201, 21))
        self.frame_4.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"border-style: outset;\n"
"border-color: black;\n"
"border-width: 1px;\n"
"border-radius: 4px;")
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.textEdit_10 = QtWidgets.QTextEdit(self.frame_4)
        self.textEdit_10.setGeometry(QtCore.QRect(0, 0, 171, 31))
        self.textEdit_10.setStyleSheet("border:false")
        self.textEdit_10.setObjectName("textEdit_10")
        self.frame_5 = QtWidgets.QFrame(self.frame)
        self.frame_5.setGeometry(QtCore.QRect(20, 130, 201, 21))
        self.frame_5.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"border-style: outset;\n"
"border-color: black;\n"
"border-width: 1px;\n"
"border-radius: 4px;")
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.frame_6 = QtWidgets.QFrame(self.frame_5)
        self.frame_6.setGeometry(QtCore.QRect(180, 20, 201, 21))
        self.frame_6.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"border-style: outset;\n"
"border-color: black;\n"
"border-width: 1px;\n"
"border-radius: 4px;")
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.textEdit_12 = QtWidgets.QTextEdit(self.frame_6)
        self.textEdit_12.setGeometry(QtCore.QRect(0, 0, 171, 31))
        self.textEdit_12.setStyleSheet("border:false")
        self.textEdit_12.setObjectName("textEdit_12")
        self.pushButton_7 = QtWidgets.QPushButton(self.frame_5)
        self.pushButton_7.setGeometry(QtCore.QRect(180, 0, 21, 21))
        self.pushButton_7.setStyleSheet("border: false")
        self.pushButton_7.setObjectName("pushButton_7")
        self.frame_7 = QtWidgets.QFrame(self.frame)
        self.frame_7.setGeometry(QtCore.QRect(250, 100, 201, 21))
        self.frame_7.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"border-style: outset;\n"
"border-color: black;\n"
"border-width: 1px;\n"
"border-radius: 4px;")
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.frame_8 = QtWidgets.QFrame(self.frame_7)
        self.frame_8.setGeometry(QtCore.QRect(180, 20, 201, 21))
        self.frame_8.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"border-style: outset;\n"
"border-color: black;\n"
"border-width: 1px;\n"
"border-radius: 4px;")
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.textEdit_14 = QtWidgets.QTextEdit(self.frame_8)
        self.textEdit_14.setGeometry(QtCore.QRect(0, 0, 171, 31))
        self.textEdit_14.setStyleSheet("border:false")
        self.textEdit_14.setObjectName("textEdit_14")
        self.pushButton_6 = QtWidgets.QPushButton(self.frame_7)
        self.pushButton_6.setGeometry(QtCore.QRect(180, 0, 21, 21))
        self.pushButton_6.setStyleSheet("border: false")
        self.pushButton_6.setObjectName("pushButton_6")
        self.textEdit_11 = QtWidgets.QTextEdit(self.frame_7)
        self.textEdit_11.setGeometry(QtCore.QRect(0, 0, 171, 31))
        self.textEdit_11.setStyleSheet("border:false")
        self.textEdit_11.setObjectName("textEdit_11")
        self.frame_9 = QtWidgets.QFrame(self.frame)
        self.frame_9.setGeometry(QtCore.QRect(250, 130, 201, 21))
        self.frame_9.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"border-style: outset;\n"
"border-color: black;\n"
"border-width: 1px;\n"
"border-radius: 4px;")
        self.frame_9.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_9.setObjectName("frame_9")
        self.textEdit_15 = QtWidgets.QTextEdit(self.frame_9)
        self.textEdit_15.setGeometry(QtCore.QRect(0, 0, 171, 31))
        self.textEdit_15.setStyleSheet("border:false")
        self.textEdit_15.setObjectName("textEdit_15")
        self.frame_10 = QtWidgets.QFrame(self.frame_9)
        self.frame_10.setGeometry(QtCore.QRect(180, 20, 201, 21))
        self.frame_10.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"border-style: outset;\n"
"border-color: black;\n"
"border-width: 1px;\n"
"border-radius: 4px;")
        self.frame_10.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_10.setObjectName("frame_10")
        self.textEdit_16 = QtWidgets.QTextEdit(self.frame_10)
        self.textEdit_16.setGeometry(QtCore.QRect(0, 0, 171, 31))
        self.textEdit_16.setStyleSheet("border:false")
        self.textEdit_16.setObjectName("textEdit_16")
        self.pushButton_8 = QtWidgets.QPushButton(self.frame_9)
        self.pushButton_8.setGeometry(QtCore.QRect(180, 0, 21, 21))
        self.pushButton_8.setStyleSheet("border: false")
        self.pushButton_8.setObjectName("pushButton_8")
        self.textEdit_13 = QtWidgets.QTextEdit(self.frame)
        self.textEdit_13.setGeometry(QtCore.QRect(20, 130, 171, 31))
        self.textEdit_13.setStyleSheet("border:false;\n"
"background-color: rgba(254, 252, 255, 0);")
        self.textEdit_13.setObjectName("textEdit_13")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(240, 40, 511, 61))
        self.textEdit.setStyleSheet("background-color: rgba(253, 250, 255, 0);\n"
"border: false;")
        self.textEdit.setObjectName("textEdit")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(210, 290, 571, 251))
        self.frame_2.setStyleSheet("border:0;")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_2.setGeometry(QtCore.QRect(170, 130, 241, 51))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("background-color: rgba(255, 255, 255, 189);\n"
"border-radius: 15px;\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-color: black;\n"
"padding: 4px;")
        self.pushButton_2.setAutoExclusive(False)
        self.pushButton_2.setAutoDefault(False)
        self.pushButton_2.setDefault(False)
        self.pushButton_2.setFlat(False)
        self.pushButton_2.setObjectName("pushButton_2")
        self.dateEdit = QtWidgets.QDateEdit(self.frame_2)
        self.dateEdit.setGeometry(QtCore.QRect(130, 40, 131, 31))
        self.dateEdit.setStyleSheet("")
        self.dateEdit.setMaximumDateTime(QtCore.QDateTime(QtCore.QDate(7999, 9, 30), QtCore.QTime(23, 59, 59)))
        self.dateEdit.setMaximumTime(QtCore.QTime(23, 59, 59))
        self.dateEdit.setCalendarPopup(True)
        self.dateEdit.setDate(QtCore.QDate(2019, 4, 7))
        self.dateEdit.setObjectName("dateEdit")
        self.dateEdit_2 = QtWidgets.QDateEdit(self.frame_2)
        self.dateEdit_2.setGeometry(QtCore.QRect(330, 40, 131, 31))
        self.dateEdit_2.setStyleSheet("")
        self.dateEdit_2.setCalendarPopup(True)
        self.dateEdit_2.setDate(QtCore.QDate(2019, 4, 9))
        self.dateEdit_2.setObjectName("dateEdit_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 1001, 561))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("ASD_Fotor.png"))
        self.label.setObjectName("label")
        self.label.raise_()
        self.frame.raise_()
        self.textEdit.raise_()
        self.frame_2.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1001, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "+"))
        self.textEdit_3.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.SF NS Text\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24pt; font-weight:600; color:#102d9e;\">Dates</span></p></body></html>"))
        self.textEdit_4.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.SF NS Text\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt;\">TO</span></p></body></html>"))
        self.textEdit_6.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.SF NS Text\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24pt; font-weight:600; color:#1847ab;\">Destinations</span></p></body></html>"))
        self.textEdit_5.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.SF NS Text\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt;\">FROM</span></p></body></html>"))
        self.textEdit_2.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.SF NS Text\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#6c6c6c;\">City</span></p></body></html>"))
        self.comboBox.setItemText(0, _translate("MainWindow", "State"))
        self.pushButton_3.setText(_translate("MainWindow", "➖"))
        self.pushButton_7.setText(_translate("MainWindow", "➖"))
        self.pushButton_6.setText(_translate("MainWindow", "➖"))
        self.textEdit_11.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.SF NS Text\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.pushButton_8.setText(_translate("MainWindow", "➖"))
        self.textEdit.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.SF NS Text\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:36pt; font-weight:600; color:#2360b7;\">Travel Planner</span></p></body></html>"))
        self.pushButton_2.setText(_translate("MainWindow", "Search"))
        self.dateEdit.setDisplayFormat(_translate("MainWindow", "MM/dd/yyyy"))
        self.dateEdit_2.setDisplayFormat(_translate("MainWindow", "MM/dd/yyyy"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
