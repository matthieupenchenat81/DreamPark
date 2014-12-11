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
        self.ui.setupUi(self.view, self)

        #signaux
        #
        self.ui.btn_subscriber.clicked.connect(lambda : self.ui.controler.chooseInterface(0))
        self.ui.btn_guest.clicked.connect(lambda : self.ui.controler.chooseInterface(1))

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
            print(self.currentUser)
            self.ui.label_name.text = "Bonjour " + self.currentUser.prenom + ","
            self.ui.subscribed.raise_()