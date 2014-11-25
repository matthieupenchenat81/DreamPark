from View.consumer_home import *
import sys
import shelve

class HomeControler:

    def __init__(self):
        #self.clients = shelve.open('Database/clients.bin')

        #self.clients['12131'] = Client(12131, "Alexandre", "PEREIRA")





        app = QtGui.QApplication(sys.argv)
        self.view = QtGui.QMainWindow()
        ui = Ui_consumer_home()
        ui.setupUi(self.view, self)
        self.view.show()
        sys.exit(app.exec_())

    def choose_interface(self, type):
        if type==0:
            consumer_home = QtGui.QMainWindow()
            ui = Ui_consumer_home()
            ui.setupUi(consumer_home, self)
            consumer_home.show()