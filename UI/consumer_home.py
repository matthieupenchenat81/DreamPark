# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/malibu/Documents/Cours/MIASHS/Python/Project/consumer_home.ui'
#
# Created: Fri Nov 21 15:21:20 2014
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(500, 279)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 30, 161, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(30, 110, 221, 31))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.btn_subscriber = QtGui.QPushButton(self.centralwidget)
        self.btn_subscriber.setGeometry(QtCore.QRect(30, 150, 201, 111))
        self.btn_subscriber.setObjectName(_fromUtf8("btn_subscriber"))
        self.btn_guest = QtGui.QPushButton(self.centralwidget)
        self.btn_guest.setGeometry(QtCore.QRect(270, 150, 201, 111))
        self.btn_guest.setObjectName(_fromUtf8("btn_guest"))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.label.setText(_translate("MainWindow", "Bienvenue!", None))
        self.label_2.setText(_translate("MainWindow", "Veuillez choisir votre status:", None))
        self.btn_subscriber.setText(_translate("MainWindow", "Abonné", None))
        self.btn_guest.setText(_translate("MainWindow", "Non abonné", None))

