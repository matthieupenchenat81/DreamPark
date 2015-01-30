import sys

from Developpement.DreamPark.View.UIAdmin import *
from Developpement.DreamPark.Model.Parking.Placement import *


class AdminControler:
    def __init__(self):
        QtGui.QApplication.setStyle(QtGui.QStyleFactory.create("Cleanlooks"))
        app = QtGui.QApplication(sys.argv)
        # app.aboutToQuit.connect(self.exitProgram)
        self.view = QtGui.QMainWindow()
        self.ui = Ui_Admin()
        self.ui.setupUi(self.view)
        self.view.setWindowIcon(QtGui.QIcon("icon.png"))
        self.refreshMainPage()
        self.view.show()
        sys.exit(app.exec_())


    def refreshMainPage(self):
        self.ui.lcdNumber.display(len(Place.tous))
        self.ui.lcdNumber_2.display(Placement.nbPlaceOccupes())
        self.ui.lcdNumber_3.display(len(Client.tous))
        self.ui.lcdNumber_4.display(Client.getNbSuperAbonne())
        self.ui.lcdNumber_5.display(Client.getNbAbonne())