from Developpement.DreamPark.View.UIHome import *
from Developpement.DreamPark.View.UIClientConnection import *
from Developpement.DreamPark.View.UIClientRegistered import *
from Developpement.DreamPark.Model.Abonnement.Client import *
from Developpement.DreamPark.Model.Abonnement.Type import *
from Developpement.DreamPark.Model.Parking.Placement import *
from Developpement.DreamPark.Model.Parking.Voiture import *
from Developpement.DreamPark.Model.Parking.Place import *
import sys

class HomeControler:

    def __init__(self):
        QtGui.QApplication.setStyle(QtGui.QStyleFactory.create('Cleanlooks'))
        app = QtGui.QApplication(sys.argv)
        app.aboutToQuit.connect(self.exitProgram)
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
        validatorCrypto = QtGui.QRegExpValidator(QtCore.QRegExp('^([0-9]{3})$'))
        self.ui.input_firstName.setValidator(validatorName)
        self.ui.input_lastName.setValidator(validatorName)
        self.ui.numeroDeCarteLineEdit.setValidator(validatorCB)
        self.ui.input_crypto.setValidator(validatorCrypto)
        #show main
        self.ui.home.raise_()
        self.view.show()
        sys.exit(app.exec_())

    def chooseInterface(self, type):
        if type==0:
            self.Dialog = QtGui.QDialog()
            u = Ui_Connection()
            u.setupUi(self.Dialog)
            self.Dialog.accepted.connect(lambda: self.tryLogin(u.idCard.text()))
            self.Dialog.exec_()
        if type==1:
            self.guestVoiture = Voiture()
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

        if not self.ui.numeroDeCarteLineEdit.hasAcceptableInput() :
            self.ui.numeroDeCarteLabel.setStyleSheet("QLabel { color : red; }")
            failed = True
        else:
            self.ui.numeroDeCarteLabel.setStyleSheet("QLabel { color : green; }")

        if not self.ui.input_date.hasAcceptableInput() :
            self.ui.dateDExpirationLabel.setStyleSheet("QLabel { color : red; }")
            failed = True
        else:
            self.ui.dateDExpirationLabel.setStyleSheet("QLabel { color : green; }")

        if not self.ui.input_crypto.hasAcceptableInput() :
            self.ui.cryptogrammeVisuelLabel.setStyleSheet("QLabel { color : red; }")
            failed = True
        else:
            self.ui.cryptogrammeVisuelLabel.setStyleSheet("QLabel { color : green; }")

        if not failed :
            self.Dialog = QtGui.QDialog()
            u = Ui_ClientRegistered()
            u.setupUi(self.Dialog)
            if self.ui.check_packGaranti.isChecked():
                c = Client(self.ui.input_lastName.text(), self.ui.input_firstName.text(), self.ui.input_adresseI.text(),
                           Type.SUPER_ABONNE, self.guestVoiture, self.ui.numeroDeCarteLineEdit.text(), self.ui.input_crypto.text())
            else:
                c = Client(self.ui.input_lastName.text(), self.ui.input_firstName.text(), self.ui.input_adresseI.text(), Type.ABONNE
                           , self.guestVoiture, self.ui.numeroDeCarteLineEdit.text(), self.ui.input_crypto.text(), '12/01/2016')

            u.label.setText("Félicitation " + c.prenom +",\nVous êtes dorénavant membre du DreamPark parking!\n\nVotre numéro d'abonné est le suivant: ")
            u.label_2.setText(c.num)
            self.Dialog.accepted.connect(lambda: self.tryLogin(c.num))
            self.Dialog.exec_()


    def exitProgram(self):
        Client.saveAll()
        Voiture.saveAll()
        Place.saveAll()
        Placement.saveAll()

    def seGarerEnAnonyme(self):
        if not Place.hasSpace(self.guestVoiture):
            self.ui.label_name_2.setText("Bonjour,\nNous sommes désolé mais le parking est actuellement plein.")
