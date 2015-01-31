import sqlite3

from Developpement.DreamPark.Model.Abonnement.Client import Client
from Developpement.DreamPark.Model.Parking.Place import Place


class Placement:

    tous = []

    def __init__(self, id, place, client, dateD, services, dateF=None):
        self.__id = id if (id != None) else len(Placement.tous)
        self.__place = place
        self.__client = client
        self.__dateD = dateD
        self.__dateF = dateF
        self.__services = services
        self.tous.append(self)

    def partirPlace(self, dateF):
        self.__dateF = dateF

        # on libere la place
        self.__place.toogleAvailable()

    @property
    def estEnCours(self):
        return (self.__dateF == None)

    @property
    def place(self):
        return self.__place

    @property
    def id(self):
        return self.__id

    @property
    def services(self):
        return self.__services

    @property
    def client(self):
        return self.__client

    @property
    def dateD(self):
        return self.__dateD

    @property
    def dateF(self):
        return self.__dateF

    @dateF.setter
    def dateF(self, value):
        self.__dateF = value

    @staticmethod
    def loadAll():
        con = sqlite3.connect("test.db")
        with con:
            con.row_factory = sqlite3.Row
            cur = con.cursor()
            cur.execute("SELECT * FROM Placement")
            rows = cur.fetchall()
            for row in rows:
                Placement(row["id"], Place.get(row["place"]), Client.get(row["client"]), row["dateD"], row["dateF"])
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
            curseur.execute("insert into Placement values (?, ?, ?, ?, ?)", (c.id, c.place.id, c.client.num, c.dateD,
                                                                          "" if c.dateF == None else c.dateF))
        conn.commit()
        conn.close()

    @staticmethod
    def get(id):
        for p in Placement.tous:
            if p.id == id: return p
        return None

    @staticmethod
    def canPark(client):
        if(Placement.hasParkedCar(client)): return False
        if(Place.getAvailablePlace(client.idVoiture) == None): return False
        return True

    @staticmethod
    def nbPlaceOccupes():
        i = 0
        for p in Placement.tous:
            if not p.dateF:
                i = i + 1
        return i