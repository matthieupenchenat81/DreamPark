import sqlite3

class Place:

    tous = []

    def __init__(self, niveau, hauteur, longueur, largeur, id=None):
        self.__id = id if (id != None) else len(Place.tous)
        self.__hauteur = hauteur
        self.__largeur = largeur
        self.__longueur = longueur
        self.__niveau = niveau
        self.tous.append(self)

    def __str__(self):
         return "Place[ id : " + str(self.__id) + ", niveau : " + str(self.__niveau) + ", hauteur : "+ str(self.__hauteur) + ", largeur : "+ str(self.__largeur)+ ", longueur : "+ str(self.__longueur)+ "]"

    @property
    def id(self):
        return self.__id

    @property
    def estLibre(self):
        return self.__estLibre

    @property
    def hauteur(self):
        return self.__hauteur

    @property
    def largeur(self):
        return self.__largeur

    @property
    def longueur(self):
        return self.__longueur

    @property
    def niveau(self):
        return self.__niveau

    @staticmethod
    def get(key):
        for item in Place.tous:
            if (item.id == key): return item
        return None

    def toogleAvailable(self):
        self.__estLibre = not self.__estLibre

    @staticmethod
    def loadAll():
        con = sqlite3.connect("test.db")
        with con:
            con.row_factory = sqlite3.Row
            cur = con.cursor()
            cur.execute("SELECT * FROM Place")
            rows = cur.fetchall()
            for row in rows:
                Place(row["niveau"], row["hauteur"], row["longueur"], row["largeur"], row["id"])
        con.close()

    @staticmethod
    def saveAll():

        # connect table
        conn = sqlite3.connect("test.db")
        curseur = conn.cursor()
        #reset table Place
        curseur.execute("delete from Place")
        # insert places
        for c in Place.tous:
            curseur.execute("insert into Place values (?, ?, ?, ?, ?)",
                            (c.niveau, c.hauteur, c.longueur, c.largeur, c.id))
        conn.commit()
        conn.close()


    def isAvailable(self):
        from Developpement.DreamPark.Model.Abonnement.Client import Client
        from Developpement.DreamPark.Model.Parking.Placement import Placement

        for c in Client.tous:
            if c.placeReserve == self: return False
        for pc in Placement.tous:
            if pc.place == self and pc.dateF == None: return False
        return True

    @staticmethod
    def getAvailablePlace(voiture):
        # TODO : Soustraire les places réservées
        for i in Place.tous:
            if (i.hauteur >= voiture.hauteur and i.largeur >= voiture.largeur and i.hauteur >= voiture.hauteur):
                if i.isAvailable(): return i
        return None