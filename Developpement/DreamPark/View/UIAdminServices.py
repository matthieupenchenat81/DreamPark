# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UIAdminServices.ui'
#
# Created: Sun Feb  1 21:41:01 2015
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


class Ui_Services(object):
    def setupUi(self, Services):
        Services.setObjectName(_fromUtf8("Services"))
        Services.resize(433, 249)
        self.tableWidget = QtGui.QTableWidget(Services)
        self.tableWidget.setGeometry(QtCore.QRect(10, 10, 411, 171))
        self.tableWidget.setObjectName(_fromUtf8("tableWidget"))
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        self.pushButton = QtGui.QPushButton(Services)
        self.pushButton.setGeometry(QtCore.QRect(10, 200, 411, 41))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))

        self.retranslateUi(Services)
        QtCore.QMetaObject.connectSlotsByName(Services)

    def retranslateUi(self, Services):
        Services.setWindowTitle(_translate("Services", "Services", None))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Services", "Type de service", None))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Services", "Demandé le", None))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Services", "Voiture", None))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Services", "Niveau", None))
        self.pushButton.setText(_translate("Services", "Effectuer", None))

