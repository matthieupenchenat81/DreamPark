from View.consumer_home import *
from Model.Abonnement import Client
import sys
import shelve

class HomeControler:

    def __init__(self):
        self.clients = shelve.open('Database/clients.bin')

        self.clients['12312312032103012'] = Client("Alexandre", "PEREIRA", "1313-1231-3131-1313")


        app = QtGui.QApplication(sys.argv)
        self.view = QtGui.QMainWindow()
        ui = Ui_consumer_home()
        ui.setupUi(view, self)
        self.view.show()
        sys.exit(app.exec_())

    def choose_interface(self, type):
        if type==0:
            consumer_home = QtGui.QMainWindow()
            ui = Ui_consumer_home()
            ui.setupUi(consumer_home, self)
            consumer_home.show()