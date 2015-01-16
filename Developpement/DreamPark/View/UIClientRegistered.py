# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/malibu/Git/DreamPark/UI/UIClientRegistered.ui'
#
# Created: Fri Jan 16 16:52:11 2015
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

class Ui_ClientRegistered(object):
    def setupUi(self, ClientRegistered):
        ClientRegistered.setObjectName(_fromUtf8("ClientRegistered"))
        ClientRegistered.resize(390, 166)
        self.label = QtGui.QLabel(ClientRegistered)
        self.label.setGeometry(QtCore.QRect(10, 10, 361, 111))
        self.label.setObjectName(_fromUtf8("label"))
        self.buttonBox = QtGui.QDialogButtonBox(ClientRegistered)
        self.buttonBox.setGeometry(QtCore.QRect(295, 130, 81, 23))
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.label_2 = QtGui.QLabel(ClientRegistered)
        self.label_2.setGeometry(QtCore.QRect(30, 120, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(19)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))

        self.retranslateUi(ClientRegistered)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), ClientRegistered.accept)
        QtCore.QMetaObject.connectSlotsByName(ClientRegistered)

    def retranslateUi(self, ClientRegistered):
        ClientRegistered.setWindowTitle(_translate("ClientRegistered", "Dialog", None))
        self.label.setText(_translate("ClientRegistered", "Félicitation Alexandre,\n"
"Vous êtes dorénavant membre du DreamPark parking!\n"
"\n"
"Votre numéro d\'abonné est le suivant: ", None))
        self.label_2.setText(_translate("ClientRegistered", "TextLabel", None))

