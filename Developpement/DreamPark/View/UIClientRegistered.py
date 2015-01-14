# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/malibu/Git/DreamPark/UI/pop_Im_subscribed.ui'
#
# Created: Wed Jan 14 11:52:26 2015
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
        ClientRegistered.resize(398, 179)
        self.centralwidget = QtGui.QWidget(ClientRegistered)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 20, 361, 111))
        self.label.setObjectName(_fromUtf8("label"))
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(290, 140, 92, 27))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(40, 130, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(19)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))

        self.retranslateUi(ClientRegistered)
        QtCore.QMetaObject.connectSlotsByName(ClientRegistered)

    def retranslateUi(self, ClientRegistered):
        ClientRegistered.setWindowTitle(_translate("ClientRegistered", "MainWindow", None))
        self.label.setText(_translate("ClientRegistered", "Félicitation Alexandre,\n"
"Vous êtes dorénavant membre du DreamPark parking!\n"
"\n"
"Votre numéro d\'abonné est le suivant: ", None))
        self.pushButton.setText(_translate("ClientRegistered", "Ok", None))
        self.label_2.setText(_translate("ClientRegistered", "TextLabel", None))

