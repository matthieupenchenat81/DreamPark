# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pop_consumer_connexion.ui'
#
# Created: Thu Dec 11 09:51:18 2014
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

class Ui_consumer_connexion(object):
    def setupUi(self, consumer_connexion):
        consumer_connexion.setObjectName(_fromUtf8("consumer_connexion"))
        consumer_connexion.resize(381, 158)
        self.buttonBox = QtGui.QDialogButtonBox(consumer_connexion)
        self.buttonBox.setGeometry(QtCore.QRect(20, 110, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.idCard = QtGui.QLineEdit(consumer_connexion)
        self.idCard.setGeometry(QtCore.QRect(20, 60, 341, 33))
        self.idCard.setObjectName(_fromUtf8("idCard"))
        self.label = QtGui.QLabel(consumer_connexion)
        self.label.setGeometry(QtCore.QRect(20, 20, 301, 21))
        self.label.setObjectName(_fromUtf8("label"))

        self.retranslateUi(consumer_connexion)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), consumer_connexion.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), consumer_connexion.reject)
        QtCore.QMetaObject.connectSlotsByName(consumer_connexion)

    def retranslateUi(self, consumer_connexion):
        consumer_connexion.setWindowTitle(_translate("consumer_connexion", "Dialog", None))
        self.label.setText(_translate("consumer_connexion", "Veuillez saisir votre numéro de carte :", None))

