import datetime
from enum import Enum
import sqlite3


class Service:

    tous = []

    class TypeService(Enum):
        MAINTENANCE = 1
        ENTRETIEN = 2
        LIVRAISON = 3

    @property
    def typeService(self):
        return self.__typeService

    @property
    def placement(self):
        return self.__placement

    @property
    def dateFin(self):
        return self.__dateFin

    @property
    def argument(self):
        return self.__argument

    def __init__(self, placement, dateFin, typeService, argument=None):
        self.__placement = placement
        self.__dateF = dateFin
        self.__typeService = typeService
        self.__argument = argument
        self.tous.append(self)

    def effectuerTache(self):
        now = datetime.datetime.now()
        self.__dateF = now.strftime("%d-%m-%Y")

    @staticmethod
    def loadAll():
        from Developpement.DreamPark.Model.Parking import Placement
        con = sqlite3.connect("test.db")
        with con:
            con.row_factory = sqlite3.Row
            cur = con.cursor()
            cur.execute("SELECT * FROM Service")
            rows = cur.fetchall()
            for row in rows:
                Service(Placement.get(row["placement"]), row["dateFin"], row["typeService"], row["argument"])
        con.close()

    @staticmethod
    def saveAll():
        # connect table
        conn = sqlite3.connect("test.db")
        curseur = conn.cursor()
        #reset table Service
        curseur.execute("delete from Service")
        # insert Service
        for c in Service.tous:
            curseur.execute("insert into Service values (?, ?, ?, ?)",
                            (c.placement.id, c.dateFin, c.typeService, c.argument))
        conn.commit()
        conn.close()