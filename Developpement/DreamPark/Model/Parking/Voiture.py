import sqlite3
from Developpement.DreamPark.Model.Parking import Camera

class Voiture:

    tous = []

    def __init__(self, immatriculation, longueur = None, largeur = None, hauteur = None):
        if (longueur == None & largeur == None & hauteur == None):
            self.setDim()
        else:
            self.__longueur = longueur
            self.__largeur = largeur
            self.__hauteur = hauteur
        self.__immatriculation = immatriculation
        self.tous.append(self)

    def setDim(self):
        self.__longueur = Camera.capturerLongueur()
        self.__hauteur = Camera.capturerHauteur()
        self.__largeur = Camera.capturerLargeur()

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
    def immatriculation(self):
        return self.__immatriculation

    def __str__(self):
         return "Voiture, " + str(self.__longueur) + "x" + str(self.__largeur) + "x" + str(self.hauteur) + ", Immatr : " + self.__immatriculation

    @staticmethod
    def loadAll():
        con = sqlite3.connect("test.db")
        with con:
            con.row_factory = sqlite3.Row
            cur = con.cursor()
            cur.execute("SELECT * FROM Voiture")
            rows = cur.fetchall()
            for row in rows:
                Voiture(row["immatriculation"], row["longueur"], row["largeur"], row["hauteur"])
        con.close()


    @staticmethod
    def saveAll():
        # connect table
        conn = sqlite3.connect("test.db")
        curseur = conn.cursor()
        curseur.execute("DROP TABLE IF EXISTS Voiture")
        curseur.execute("""create table Voiture (immatriculation varchar(20) PRIMARY KEY, longueur decimal(4,2), largeur decimal(4,2), hauteur decimal(4,2))""")
        for c in Voiture.tous:
            curseur.execute("insert into Voiture values (?, ?, ?, ?, ?, ?)", (c.immatriculation, c.longueur, c.largeur, c.hauteur))
        conn.commit()
        conn.close()