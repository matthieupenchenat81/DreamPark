import sys
from random import *

from Developpement.DreamPark.View.UIAdmin import *
from Developpement.DreamPark.View.UIAdminServices import *
from Developpement.DreamPark.Model.Parking.Placement import *
from Developpement.DreamPark.Model.Parking.Voiture import *


class AdminControler:
    def __init__(self):
        QtGui.QApplication.setStyle(QtGui.QStyleFactory.create("Cleanlooks"))
        app = QtGui.QApplication(sys.argv)
        app.aboutToQuit.connect(self.exitProgram)
        self.view = QtGui.QMainWindow()
        self.ui = Ui_Admin()
        self.ui.setupUi(self.view)
        self.view.setWindowIcon(QtGui.QIcon("icon.png"))
        self.refreshMainPage()

        self.ui.pushButton.clicked.connect(self.showServices)
        self.ui.pushButton_2.clicked.connect(self.reInitilialize)


        self.view.show()
        sys.exit(app.exec_())


    def refreshMainPage(self):
        self.ui.lcdNumber.display(len(Place.tous))
        self.ui.lcdNumber_2.display(Placement.nbPlaceOccupes())
        self.ui.lcdNumber_3.display(len(Client.tous))
        self.ui.lcdNumber_4.display(Client.getNbSuperAbonne())
        self.ui.lcdNumber_5.display(Client.getNbAbonne())


    def showServices(self):
        d = QtGui.QDialog()
        self.uis = Ui_Services()
        self.uis.setupUi(d)

        self.uis.pushButton.clicked.connect(self.doService)
        self.uis.tableWidget.setRowCount(len(Service.tous))
        self.servicesToShow = []
        i = 0
        for s in Service.tous:
            if not s.dateF:
                self.servicesToShow.append(s)
                t = ""
                if s.typeService == Service.TypeService.ENTRETIEN: t = "Entretien"
                if s.typeService == Service.TypeService.MAINTENANCE: t = "Maintenance"
                if s.typeService == Service.TypeService.LIVRAISON: t = "Livraison"

                self.addInTab(i, [t, s.placement.dateD, s.placement.client.voiture.immatriculation,
                                  str(s.placement.place.niveau)])
                i = i + 1

        self.uis.tableWidget.setRowCount(i)

        d.exec_()

    def addInTab(self, line, array):
        for i in range(len(array)):
            self.uis.tableWidget.setItem(line, i, QtGui.QTableWidgetItem(array[i]))

    def doService(self):
        from datetime import datetime

        print(self.servicesToShow[self.uis.tableWidget.currentRow()].typeService)

        s = self.servicesToShow[self.uis.tableWidget.currentRow()]
        s.dateF = datetime.today().strftime("%d/%m/%Y %H:%M:%S")
        self.servicesToShow.remove(s)
        self.uis.tableWidget.removeRow(self.uis.tableWidget.currentRow())


    def exitProgram(self):
        Voiture.saveAll()
        Client.saveAll()
        Place.saveAll()
        Placement.saveAll()
        Service.saveAll()
        print("Goodbye !")

    def reInitilialize(self):
        conn = sqlite3.connect("test.db")
        curseur = conn.cursor()
        # voiture
        curseur.execute("DROP TABLE IF EXISTS Voiture")
        curseur.execute(
            """create table Voiture(immatriculation varchar(20) PRIMARY KEY, longueur int, largeur int, hauteur int)""")
        # client
        curseur.execute("DROP TABLE IF EXISTS Client")
        curseur.execute(
            """create table Client (numClient varchar(15) PRIMARY KEY, nomClient varchar(30), prenomClient varchar(30), adrClient varchar(50), estAbonne int(1), idVoiture varchar(20), numCB int(20), cryptoVisuel int(3), dateExpiration varchar(10), placeReserve int, FOREIGN KEY(idVoiture) REFERENCES Voiture(immatriculation))""")
        #place
        curseur.execute("DROP TABLE IF EXISTS Place")
        curseur.execute(
            """create table Place (niveau int, hauteur decimal(4,2), longueur decimal(4,2), largeur decimal(4,2), id int PRIMARY KEY)""")
        #placement
        curseur.execute("DROP TABLE IF EXISTS Placement")
        curseur.execute("""create table Placement (id int, place int, client int, dateD date, dateF date)""")
        #Service
        curseur.execute("DROP TABLE IF EXISTS Service")
        curseur.execute(
            """create table Service (placement int, dateFin date, typeService int, argument varchar(100))""")

        conn.commit()
        conn.close()

        Client.tous = []
        Place.tous = []
        Placement.tous = []
        Service.tous = []
        Voiture.tous = []

        placeType = [[300, 150, 200], [150, 200, 300],
                     [500, 400, 300]]  # hauteur, largeur, longueur de 3 types de places
        for i in range(0, 20):
            choosenPlaceType = placeType[randint(0, 2)]
            Place(randint(1, 2), choosenPlaceType[0], choosenPlaceType[2], choosenPlaceType[1])
        Place.saveAll()

        self.ui.pushButton_2.setDisabled(True)
        self.refreshMainPage()