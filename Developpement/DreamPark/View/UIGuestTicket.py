# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/malibu/Git/DreamPark/UI/UIGuestTicket.ui'
#
# Created: Fri Jan 16 15:58:32 2015
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

class Ui_GuestTicket(object):
    def setupUi(self, GuestTicket):
        GuestTicket.setObjectName(_fromUtf8("GuestTicket"))
        GuestTicket.setWindowModality(QtCore.Qt.ApplicationModal)
        GuestTicket.resize(400, 186)
        self.buttonBox = QtGui.QDialogButtonBox(GuestTicket)
        self.buttonBox.setGeometry(QtCore.QRect(20, 140, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.label_2 = QtGui.QLabel(GuestTicket)
        self.label_2.setGeometry(QtCore.QRect(20, 70, 281, 71))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_numTicket = QtGui.QLabel(GuestTicket)
        self.label_numTicket.setGeometry(QtCore.QRect(20, 20, 251, 41))
        self.label_numTicket.setObjectName(_fromUtf8("label_numTicket"))

        self.retranslateUi(GuestTicket)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), GuestTicket.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), GuestTicket.reject)
        QtCore.QMetaObject.connectSlotsByName(GuestTicket)

    def retranslateUi(self, GuestTicket):
        GuestTicket.setWindowTitle(_translate("GuestTicket", "Dialog", None))
        self.label_2.setText(_translate("GuestTicket", "Veillez à ne pas perdre le ticket\n"
"et à le présenter au moment de vouloir\n"
"récupérer votre véhicule.", None))
        self.label_numTicket.setText(_translate("GuestTicket", "Votre numéro de ticket est le :\n"
"0165F32", None))

