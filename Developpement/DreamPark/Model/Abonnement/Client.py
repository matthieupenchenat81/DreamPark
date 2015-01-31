import random
import sqlite3
import string

from Developpement.DreamPark.Model.Parking.Place import Place
from Developpement.DreamPark.Model.Parking.Voiture import Voiture


class Client:

    tous = []

    @staticmethod
    def get(key):
        for item in Client.tous:
            if (item.num == key): return item
        return None

    @staticmethod
    def generateId():
        d = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(8))
        while Client.get(d) != None:
            d = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(8))
        return d

    @property
    def prenom(self):
        return self.__prenom

    @property
    def nom(self):
        return self.__nom

    @property
    def num(self):
        return self.__num

    @property
    def adr(self):
        return self.__adresse

    @property
    def cryptoVisuel(self):
        return self.__cryptoVisuel

    @property
    def numCB(self):
        return self.__numCB

    @property
    def voiture(self):
        return self.__voiture

    @property
    def dateExpiration(self):
        return self.__dateExpiration

    @property
    def placeReserve(self):
        return self.__placeReserve

    @property
    def estAbonne(self):
        return self.__estAbonne

    def __init__(self, nom, prenom, adresse, estAbonne, voiture, numCB, cryptoVisuel, dateExpiration, placeReserve,
                 num=None):
        self.__num = Client.generateId() if num == None else num
        self.__dateExpiration = dateExpiration
        self.__voiture = voiture
        self.__placeReserve = placeReserve
        self.__numCB = numCB
        self.__cryptoVisuel = cryptoVisuel
        self.__nom = nom
        self.__prenom = prenom
        self.__estAbonne= estAbonne
        self.__adresse = adresse
        self.tous.append(self)

    @staticmethod
    def loadAll():
        con = sqlite3.connect("test.db")
        with con:
            con.row_factory = sqlite3.Row
            cur = con.cursor()
            for row in cur.execute("""SELECT * FROM Client"""):
                Client(row["nomClient"], row["prenomClient"], row["adrClient"],
                       True if (row["estAbonne"] == 1) else False,
                       Voiture.get(row["idVoiture"]), row["numCB"], row["cryptoVisuel"], row["dateExpiration"],
                       Place.get(row["placeReserve"]), row["numClient"])
        con.close()

    @staticmethod
    def saveAll():

        # connect table
        conn = sqlite3.connect("test.db")
        curseur = conn.cursor()
        # reset table Client
        curseur.execute("delete from Client")
        # insert clients
        for c in Client.tous:
            curseur.execute("insert into Client values (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (
                c.num, c.nom, c.prenom, c.adr, c.estAbonne, c.voiture.immatriculation, c.numCB, c.cryptoVisuel,
                c.dateExpiration, None if (c.placeReserve == None) else c.placeReserve.id))
        conn.commit()
        conn.close()

    def __str__( self ):
        tmpP = "-" if self.__prenom == None else self.__prenom
        tmpN = "-" if self.__nom == None else self.__nom
        return "( " + self.__num + ", " + tmpN + " " + tmpP + " )"


    def hasParkedCar(self):
        from Developpement.DreamPark.Model.Parking.Placement import Placement

        for item in Placement.tous:
            if (item.client == self and item.dateF == None):
                return True
        return False

    def recupererVehicule(self):
        from Developpement.DreamPark.Model.Parking.Placement import Placement

        for pc in Placement.tous:
            if (pc.client == self and not pc.dateF):
                pc.dateF = "FINI"  # mettre vrai date
                return True
        return False
    @staticmethod
    def getNbSuperAbonne():
        i = 0
        for c in Client.tous:
            if not c.placeReserve and c.estAbonne:
                i = i + 1
        return i

    @staticmethod
    def getNbAbonne():
        i = 0
        for c in Client.tous:
            if c.estAbonne:
                i = i + 1
        return i