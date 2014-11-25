# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'consumer_home.ui'
#
# Created: Mon Nov 24 17:02:40 2014
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

class Ui_consumer_home(object):
    def setupUi(self, consumer_home, controler):
        consumer_home.setObjectName(_fromUtf8("consumer_home"))
        consumer_home.resize(500, 279)
        self.centralwidget = QtGui.QWidget(consumer_home)
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
        consumer_home.setCentralWidget(self.centralwidget)
        #signals
        self.__controler = controler
        self.btn_guest.connect(self.btn_guest, QtCore.SIGNAL("clicked()"),  lambda: self.__controler.choose_interface(0))
        #end signals
        self.retranslateUi(consumer_home)
        QtCore.QMetaObject.connectSlotsByName(consumer_home)

    def retranslateUi(self, consumer_home):
        consumer_home.setWindowTitle(_translate("consumer_home", "MainWindow", None))
        self.label.setText(_translate("consumer_home", "Bienvenue !", None))
        self.label_2.setText(_translate("consumer_home", "Veuillez choisir votre statut :", None))
        self.btn_subscriber.setText(_translate("consumer_home", "Abonné", None))
        self.btn_guest.setText(_translate("consumer_home", "Non abonné", None))



