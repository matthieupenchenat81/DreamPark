from View.consumer_home import *
import sys

class HomeControler:

    def __init__(self):
        app = QtGui.QApplication(sys.argv)
        consumer_home = QtGui.QMainWindow()
        ui = Ui_consumer_home()
        ui.setupUi(consumer_home, self)
        consumer_home.show()
        sys.exit(app.exec_())

    def launch(id):
        ...
        #ouvrir l'ui qui demande le choix des personnes

    def choose_interface(self, type):
        print("Choix : " + str(type))