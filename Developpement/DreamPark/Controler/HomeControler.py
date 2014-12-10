from Developpement.DreamPark.View.home import *
import sys

class HomeControler:

    def __init__(self):
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
            self.ui.subscribed.raise_()
        if type==1:
            self.ui.guest.raise_()