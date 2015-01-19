import sqlite3

from Developpement.DreamPark.Model.Abonnement.Client import Client
from Developpement.DreamPark.Model.Parking.Place import Place


class Placement:

    tous = []

    def __init__(self, place, client, dateD, dateF=None):
        self.__place = place
        self.__client = client
        self.__dateD = dateD
        self.__dateF = dateF
        self.tous.append(self)

    def partirPlace(self, dateF):
        self.__dateF = dateF

        # on libere la place
        self.__place.toogleAvailable()

    @property
    def estEnCours(self):
        return (self.__dateF == None)

    @property
    def id(self):
        return self.__id

    @property
    def place(self):
        return self.__place

    @property
    def client(self):
        return self.__client

    @property
    def dateD(self):
        return self.__dateD

    @property
    def dateF(self):
        return self.__dateF

    @staticmethod
    def loadAll():
        con = sqlite3.connect("test.db")
        with con:
            con.row_factory = sqlite3.Row
            cur = con.cursor()
            cur.execute("SELECT * FROM Placement")
            rows = cur.fetchall()
            for row in rows:
                Placement(row["id"], Place[row["place"]], Client[row["client"]], row["dateD"], row["dateF"])
        con.close()

    @staticmethod
    def saveAll():
        # connect table
        conn = sqlite3.connect("test.db")
        curseur = conn.cursor()
        #reset table Placement
        curseur.execute("delete from Placement")
        # insert Placement
        for c in Placement.tous:
            curseur.execute("insert into Placement values (?, ?, ?, ?, ?, ?)", (c.place.id, c.client.num, c.dateD, c.dateF))
        conn.commit()
        conn.close()

    @staticmethod
    def hasParkedCar(client):
        for item in Placement.tous:
           if(item.client == client and item.dateF == None):
               return True
        return False

    @staticmethod
    def canPark(client):
        if(Placement.hasParkedCar(client)): return False
        if(Place.getAvailablePlace(client.idVoiture) == None): return False
        return True

