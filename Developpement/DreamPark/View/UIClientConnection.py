# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/malibu/Git/DreamPark/UI/UIConnection.ui'
#
# Created: Fri Jan 16 15:55:03 2015
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

class Ui_Connection(object):
    def setupUi(self, Connection):
        Connection.setObjectName(_fromUtf8("Connection"))
        Connection.setWindowModality(QtCore.Qt.ApplicationModal)
        Connection.resize(381, 158)
        self.buttonBox = QtGui.QDialogButtonBox(Connection)
        self.buttonBox.setGeometry(QtCore.QRect(20, 110, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.idCard = QtGui.QLineEdit(Connection)
        self.idCard.setGeometry(QtCore.QRect(20, 60, 341, 33))
        self.idCard.setObjectName(_fromUtf8("idCard"))
        self.label = QtGui.QLabel(Connection)
        self.label.setGeometry(QtCore.QRect(20, 20, 301, 21))
        self.label.setObjectName(_fromUtf8("label"))

        self.retranslateUi(Connection)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), Connection.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), Connection.reject)
        QtCore.QMetaObject.connectSlotsByName(Connection)

    def retranslateUi(self, Connection):
        Connection.setWindowTitle(_translate("Connection", "Identification", None))
        self.label.setText(_translate("Connection", "Veuillez saisir votre numéro de carte :", None))

