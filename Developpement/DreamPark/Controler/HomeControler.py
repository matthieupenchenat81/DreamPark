from Developpement.DreamPark.View.home import *
from Developpement.DreamPark.View.test import *
from Developpement.DreamPark.Model.Abonnement.Client import *
import sys

class HomeControler:

    def __init__(self):
        QtGui.QApplication.setStyle(QtGui.QStyleFactory.create('Cleanlooks'))
        app = QtGui.QApplication(sys.argv)
        self.view = QtGui.QMainWindow()
        self.ui = Ui_consumer_home()
        self.ui.setupUi(self.view)
        self.view.setWindowIcon(QtGui.QIcon("icon.png"));
        #signaux
        #
        self.ui.btn_subscriber.clicked.connect(lambda : self.chooseInterface(0))
        self.ui.btn_guest.clicked.connect(lambda : self.chooseInterface(1))
        self.ui.pushButton.clicked.connect(self.trySubscribe)
        #regex
        #firstname

        validatorName = QtGui.QRegExpValidator(QtCore.QRegExp('^([a-zA-Z\'àâéèêôùûçñãõÀÂÉÈÔÙÛÑÃÕÇ\s-]{2,30})$'))
        validatorCB = QtGui.QRegExpValidator(QtCore.QRegExp('^([4]{1})([0-9]{12,15})$'))
        self.ui.input_firstName.setValidator(validatorName)
        self.ui.input_lastName.setValidator(validatorName)
        self.ui.numeroDeCarteLineEdit.setValidator(validatorCB)

        #show main
        self.ui.home.raise_()
        self.view.show()
        sys.exit(app.exec_())

    def chooseInterface(self, type):
        if type==0:
            self.Dialog = QtGui.QDialog()
            u = Ui_consumer_connexion()
            u.setupUi(self.Dialog)
            self.Dialog.accepted.connect(lambda: self.tryLogin(u.idCard.text()))
            self.Dialog.exec_()
        if type==1:
            self.ui.guest.raise_()

    def tryLogin(self, val):
        self.currentUser = Client.get(val)
        if self.currentUser != None:
            if self.currentUser.hasParkedCar() :
                self.ui.tabWidget.removeTab(0)
            else:
                self.ui.tabWidget.removeTab(1)

            self.ui.label_name.setText("Bonjour " + self.currentUser.prenom + ",")

            self.ui.subscribed.raise_()

    def trySubscribe(self):

        failed = False

        if not self.ui.input_lastName.hasAcceptableInput() :
            self.ui.nomLabel.setStyleSheet("QLabel { color : red; }")
            failed = True
        else:
            self.ui.nomLabel.setStyleSheet("QLabel { color : green; }")

        if not self.ui.input_firstName.hasAcceptableInput() :
            self.ui.prenomLabel.setStyleSheet("QLabel { color : red; }")
            failed = True
        else:
            self.ui.prenomLabel.setStyleSheet("QLabel { color : green; }")
