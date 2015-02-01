import sys
from datetime import datetime

from Developpement.DreamPark.View.UIHome import *
from Developpement.DreamPark.View.UIClientConnection import *
from Developpement.DreamPark.View.UIClientRegistered import *
from Developpement.DreamPark.View.UIConfirmRecuperer import *
from Developpement.DreamPark.View.UIGuestTicket import *
from Developpement.DreamPark.Model.Parking.Placement import *
from Developpement.DreamPark.Model.Parking.Voiture import *
from Developpement.DreamPark.Model.Parking.Place import *
from Developpement.DreamPark.Model.Services.Service import Service


class HomeControler:

    def __init__(self):

        QtGui.QApplication.setStyle(QtGui.QStyleFactory.create("Cleanlooks"))
        self.app = QtGui.QApplication(sys.argv)
        self.app.aboutToQuit.connect(self.exitProgram)
        self.view = QtGui.QMainWindow()
        self.ui = Ui_consumer_home()
        self.ui.setupUi(self.view)
        self.view.setWindowIcon(QtGui.QIcon("icon.png"))

        # Variables

        #signaux
        #
        self.ui.btn_subscriber.clicked.connect(lambda : self.chooseInterface(0))
        self.ui.btn_guest.clicked.connect(lambda : self.chooseInterface(1))

        #regex
        #firstname

        validatorName = QtGui.QRegExpValidator(QtCore.QRegExp('^([a-zA-Z\'àâéèêôùûçñãõÀÂÉÈÔÙÛÑÃÕÇ\s-]{2,30})$'))
        validatorCB = QtGui.QRegExpValidator(QtCore.QRegExp('^([4]{1})([0-9]{12,15})$'))
        validatorCrypto = QtGui.QRegExpValidator(QtCore.QRegExp('^([0-9]{3})$'))
        self.ui.input_firstName.setValidator(validatorName)
        self.ui.input_lastName.setValidator(validatorName)
        self.ui.numeroDeCarteLineEdit.setValidator(validatorCB)
        self.ui.input_crypto.setValidator(validatorCrypto)

        self.ui.input_numCarte.setValidator(validatorCB)
        self.ui.input_cryptogrammeVisuel.setValidator(validatorCrypto)

        #show main
        self.ui.home.raise_()
        self.view.show()
        sys.exit(self.app.exec_())

    def chooseInterface(self, type):
        if type==0:
            self.Dialog = QtGui.QDialog()
            u = Ui_Connection()
            u.setupUi(self.Dialog)
            self.Dialog.accepted.connect(lambda: self.tryLogin(u.idCard.text()))
            self.Dialog.exec_()
        if type==1:
            self.guestVoiture = Voiture()
            self.ui.pushButton.clicked.connect(self.trySubscribe)
            self.ui.btn_teleport_2.clicked.connect(self.seGarerEnAnonyme)
            self.ui.btn_getCar_2.clicked.connect(lambda: self.recupererVehicule(self.ui.input_numTicket.text()))
            self.ui.guest.raise_()

    def tryLogin(self, val):
        self.currentUser = Client.get(val)
        if self.currentUser != None and self.currentUser.estAbonne:
            self.ui.btn_teleport.clicked.connect(self.seGarerClient)
            if self.currentUser.hasParkedCar():
                self.ui.tabWidget.removeTab(0)
                self.ui.label_immat.setText(
                    "Votre véhicule immatriculé " + self.currentUser.voiture.immatriculation + " est actuellement dans notre parking.")
            else:
                self.ui.tabWidget.removeTab(1)
            self.ui.label_name.setText("Bonjour " + self.currentUser.prenom + ",")
            self.ui.btn_getCar.clicked.connect(lambda: self.recupererVehicule(self.currentUser.num))
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
                p = Place(3, self.guestVoiture.hauteur + 1, self.guestVoiture.longueur + 1,
                          self.guestVoiture.largeur + 1)
                c = Client(self.ui.input_lastName.text(), self.ui.input_firstName.text(), self.ui.input_adresse.text(),
                           True, self.guestVoiture, self.ui.numeroDeCarteLineEdit.text(), self.ui.input_crypto.text(),
                           datetime.today().strftime("%d/%m/%Y %H:%M:%S"), p)
            else:
                c = Client(self.ui.input_lastName.text(), self.ui.input_firstName.text(), self.ui.input_adresse.text(),
                           True, self.guestVoiture, self.ui.numeroDeCarteLineEdit.text(), self.ui.input_crypto.text(),
                           datetime.today().strftime("%d/%m/%Y %H:%M:%S"), None)

            u.label.setText("Félicitation " + c.prenom +",\nVous êtes dorénavant membre du DreamPark parking!\n\nVotre numéro d'abonné est le suivant: ")
            u.label_2.setText(c.num)
            self.Dialog.accepted.connect(lambda: self.tryLogin(c.num))
            self.Dialog.exec_()

    def exitProgram(self):
        Voiture.saveAll()
        Client.saveAll()
        Place.saveAll()
        Placement.saveAll()
        print("Goodbye !")
    def seGarerEnAnonyme(self):

        c = Client(None, None, None, False, self.guestVoiture, self.ui.input_numCarte.text(),
                   self.ui.input_cryptogrammeVisuel.text(),
                   self.ui.input_dateExpiration.text(), None)


        print(Place.getAvailablePlace(self.guestVoiture))
        Placement(None, Place.getAvailablePlace(self.guestVoiture), c, datetime.today().strftime("%d/%m/%Y %H:%M:%S"),
                  None)
        self.Dialog = QtGui.QDialog()
        u = Ui_GuestTicket()
        u.setupUi(self.Dialog)
        self.Dialog.finished.connect(self.goBackHome)
        u.label_numTicket.setText("Votre numéro de ticket est le :\n" + c.num)
        self.Dialog.exec_()

    def seGarerClient(self):

        dateD = datetime.today().strftime("%d/%m/%Y %H:%M:%S")

        if self.currentUser.placeReserve != None:
            p = Placement(None, self.currentUser.placeReserve, self.currentUser, dateD, None)
        else:
            p = Placement(None, Place.getAvailablePlace(self.currentUser.voiture), self.currentUser, dateD, None)


        # groupBox
        #input_adrLivaison + "; " + input_timeLivraison
        if self.ui.check_Entretien.isChecked():
            Service(p, None, Service.TypeService.ENTRETIEN)
        if self.ui.check_Maintenir.isChecked():
            Service(p, None, Service.TypeService.MAINTENANCE)

        self.Dialog = QtGui.QDialog()
        u = Ui_Dialog()
        u.setupUi(self.Dialog)
        self.Dialog.finished.connect(self.goBackHome)
        u.label.setText("Votre véhicule va être garré automatiquement.")
        self.Dialog.exec_()

    def recupererVehicule(self, numClient):
        c = Client.get(numClient)
        if c != None:
            if (c.recupererVehicule()):
                self.Dialog = QtGui.QDialog()
                u = Ui_Dialog()
                u.setupUi(self.Dialog)
                self.Dialog.finished.connect(self.goBackHome)
                u.label.setText("Votre véhicule va sortir...")
                self.Dialog.exec_()


    def goBackHome(self):
        self.exitProgram()
        import subprocess

        self.view.close()
        python = sys.executable
        subprocess.call(python + " app.py", shell=True)

    def enleverPackGarentie(self):
        Place.tous.remove(self.currentUser.placeReserve)
        self.currentUser.placeReserve = None