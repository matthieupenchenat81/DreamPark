import sqlite3
from Developpement.DreamPark.Model.Parking import Placement
from Developpement.DreamPark.Model.Parking.Place import Place
from Developpement.DreamPark.Model.Parking.Voiture import Voiture


class Client:

    tous = []

    @staticmethod
    def get(num):
        for client in Client.tous:
            if client.__num == num:
                return client
        return None

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
    def abonnement(self):
        return self.__typeAbonnement

    def __init__(self, num, nom = None, prenom = None, adresse = None, typeAbonnement = None):
        self.__num = num
        self.__nom = nom
        self.__prenom = prenom
        self.__typeAbonnement = typeAbonnement
        self.__adresse = adresse
        self.tous.append(self)

    @staticmethod
    def loadAll():
        con = sqlite3.connect("test.db")
        with con:
            con.row_factory = sqlite3.Row
            cur = con.cursor()
            cur.execute("SELECT * FROM Client")
            rows = cur.fetchall()
            for row in rows:
                Client(row["numClient"], row["nomClient"], row["prenomClient"], row["adrClient"], int(row["typeClient"]))
        con.close()

    @staticmethod
    def saveAll():

        # connect table
        conn = sqlite3.connect("test.db")
        curseur = conn.cursor()
        # reset table Client
        curseur.execute("DROP TABLE IF EXISTS Client")
        curseur.execute("""create table Client (numClient varchar(10) PRIMARY KEY, nomClient varchar(30), prenomClient varchar(30), adrClient varchar(50), typeClient int(1))""")
        # insert clients
        for c in Client.tous:
            curseur.execute("insert into Client values (?, ?, ?, ?, ?)", (c.num, c.nom, c.prenom, c.adr, c.abonnement))
        conn.commit()
        conn.close()

    def __str__( self ):
        return "( " + self.__num +", " + self.__nom+", " + self.__prenom+", " + self.__adresse +", " + str(self.__typeAbonnement) +" )"

    def hasParkedCar(self):
        for item in Placement.tous:
           if(item.client ==  self and item.dateF == None):
               return True
        return False

    def canPark(self):
        if(self.hasParkedCar()): return False
        Place.hasSpace(Voiture("imm", None, None, None))
