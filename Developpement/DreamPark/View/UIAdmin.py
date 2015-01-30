# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UIAdmin.ui'
#
# Created: Fri Jan 30 11:45:15 2015
# by: PyQt4 UI code generator 4.11.3
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


class Ui_Admin(object):
    def setupUi(self, Admin):
        Admin.setObjectName(_fromUtf8("Admin"))
        Admin.resize(283, 354)
        self.centralwidget = QtGui.QWidget(Admin)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 10, 261, 221))
        self.gridLayoutWidget.setObjectName(_fromUtf8("gridLayoutWidget"))
        self.gridLayout = QtGui.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setMargin(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label_2 = QtGui.QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.lcdNumber_2 = QtGui.QLCDNumber(self.gridLayoutWidget)
        self.lcdNumber_2.setObjectName(_fromUtf8("lcdNumber_2"))
        self.gridLayout.addWidget(self.lcdNumber_2, 1, 1, 1, 1)
        self.label = QtGui.QLabel(self.gridLayoutWidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 2, 0, 1, 1)
        self.label_3 = QtGui.QLabel(self.gridLayoutWidget)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 3, 0, 1, 1)
        self.lcdNumber_3 = QtGui.QLCDNumber(self.gridLayoutWidget)
        self.lcdNumber_3.setObjectName(_fromUtf8("lcdNumber_3"))
        self.gridLayout.addWidget(self.lcdNumber_3, 2, 1, 1, 1)
        self.lcdNumber = QtGui.QLCDNumber(self.gridLayoutWidget)
        self.lcdNumber.setObjectName(_fromUtf8("lcdNumber"))
        self.gridLayout.addWidget(self.lcdNumber, 0, 1, 1, 1)
        self.nbPlaceTotale = QtGui.QLabel(self.gridLayoutWidget)
        self.nbPlaceTotale.setObjectName(_fromUtf8("nbPlaceTotale"))
        self.gridLayout.addWidget(self.nbPlaceTotale, 0, 0, 1, 1)
        self.lcdNumber_4 = QtGui.QLCDNumber(self.gridLayoutWidget)
        self.lcdNumber_4.setObjectName(_fromUtf8("lcdNumber_4"))
        self.gridLayout.addWidget(self.lcdNumber_4, 3, 1, 1, 1)
        self.lcdNumber_5 = QtGui.QLCDNumber(self.gridLayoutWidget)
        self.lcdNumber_5.setObjectName(_fromUtf8("lcdNumber_5"))
        self.gridLayout.addWidget(self.lcdNumber_5, 4, 1, 1, 1)
        self.label_4 = QtGui.QLabel(self.gridLayoutWidget)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout.addWidget(self.label_4, 4, 0, 1, 1)
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(80, 250, 121, 41))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton_2 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(80, 300, 121, 41))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        Admin.setCentralWidget(self.centralwidget)

        self.retranslateUi(Admin)
        QtCore.QMetaObject.connectSlotsByName(Admin)

    def retranslateUi(self, Admin):
        Admin.setWindowTitle(_translate("Admin", "Espace Admin", None))
        self.label_2.setText(_translate("Admin", "Nombre de places occupées:", None))
        self.label.setText(_translate("Admin", "Nombre de clients :", None))
        self.label_3.setText(_translate("Admin", "Nombre de super abonnés :", None))
        self.nbPlaceTotale.setText(_translate("Admin", "Nombre de places :", None))
        self.label_4.setText(_translate("Admin", "Nombre d\'abonnés :", None))
        self.pushButton.setText(_translate("Admin", "Effectuer des services", None))
        self.pushButton_2.setText(_translate("Admin", "Tout remettre à zéro", None))

