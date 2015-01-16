import random
import sqlite3
import string
from Developpement.DreamPark.Model.Parking.Voiture import Voiture
from Developpement.DreamPark.Model.Parking.Placement import Placement
from Developpement.DreamPark.Model.Parking.Place import Place

class Client:

    tous = []

    @staticmethod
    def get(num):
        for client in Client.tous:
            if client.__num == num:
                return client
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

    def __init__(self, nom, prenom, adresse, estAbonne, idVoiture, numCB, cryptoVisuel, dateExpiration, placeReserve = None, num = None):
        self.__num = Client.generateId() if num == None else num
        self.__placeReserve = placeReserve
        self.__dateExpiration = dateExpiration
        self.__voiture = Voiture.getCar(idVoiture)
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
                Client(row["nomClient"], row["prenomClient"], row["adrClient"], row["estAbonne"], row["idVoiture"], row["numCB"], row["cryptoVisuel"], row["dateExpiration"], row["placeReserve"], row["numClient"])
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
            curseur.execute("insert into Client values (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (c.num, c.nom, c.prenom, c.adr, c.estAbonne, None if(c.voiture == None) else c.voiture.immatriculation, c.numCB, c.cryptoVisuel, c.dateExpiration, c.placeReserve))
        conn.commit()
        conn.close()

    def __str__( self ):
        return "( " + str(self.__num) +", " + self.__nom+", " + self.__prenom+", " + self.__adresse +", " + str(self.__estAbonne)+", " + str(self.__voiture) +", " + str(self.__numCB) +", " + str(self.__cryptoVisuel) +" )"

    def hasParkedCar(self):
        for item in Placement.tous:
           if(item.client ==  self and item.dateF == None):
               return True
        return False

    def canPark(self):
        if(self.hasParkedCar()): return False
        if(not Place.hasSpace(self.idVoiture)): return False
        return True