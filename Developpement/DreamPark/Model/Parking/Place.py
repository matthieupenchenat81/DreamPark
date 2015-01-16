import sqlite3

class Place:

    tous = []

    def __init__(self, niveau, hauteur, largeur, longueur, voiture=None):
        self.__id = len(self.tous)
        self.__hauteur = hauteur
        self.__largeur = largeur
        self.__longueur = longueur
        self.__voiture = voiture
        self.__niveau = niveau
        self.tous.append(self)

    def __init__(self, id, niveau, hauteur, largeur, longueur, voiture=None):
        self.__id = id
        self.__hauteur = hauteur
        self.__largeur = largeur
        self.__longueur = longueur
        self.__voiture = voiture
        self.__niveau = niveau
        self.tous.append(self)

    def __str__(self):
         return "Place[ id : " + str(self.__id) + ", niveau : " + str(self.__niveau) + ", hauteur : "+ str(self.__hauteur) + ", largeur : "+ str(self.__largeur)+ ", longueur : "+ str(self.__longueur)+ ", voiture : "+str(self.__voiture)+"]"

    @property
    def estLibre(self):
        return (self.__voiture == None)

    @property
    def id(self):
        return self.__id

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
    def voiture(self):
        return self.__voiture

    @property
    def niveau(self):
        return self.__niveau

    @staticmethod
    def getPlace(idPlace):
        for item in Place.tous:
            if(item.id == idPlace): return item
        return None

    @staticmethod
    def getAvailablePlace(voiture):
        for i in Place.tous:
            if(i.hauteur >= voiture.hauteur and i.largeur >= voiture.largeur and i.hauteur == voiture.hauteur and i.estLibre): return i
        return None

    def toogleAvailable(self):
        self.__estLibre = not self.__estLibre

    def utiliserPlace(self):
        if self.estLibre():
            self.__estLibre = False
        else:
            print("Erreur, place non libre")

    @staticmethod
    def loadAll():
        con = sqlite3.connect("test.db")
        with con:
            con.row_factory = sqlite3.Row
            cur = con.cursor()
            cur.execute("SELECT * FROM Place")
            rows = cur.fetchall()
            for row in rows:
                Place(row["id"], row["hauteur"], row["longueur"], row["largeur"], int(row["niveau"]))
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
            curseur.execute("insert into Place values (?, ?, ?, ?, ?, ?)", (c.id, c.hauteur, c.largeur, c.longueur, c.voiture, c.niveau))
        conn.commit()
        conn.close()