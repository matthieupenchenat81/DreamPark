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

    def __str__(self):
         return "Voiture, " + str(self.__longueur) + "x" + str(self.__largeur) + "x" + str(self.hauteur) + ", Immatr : " + self.__immatriculation

    @staticmethod
    def loadAll():
        con = sqlite3.connect("test.db")
        with con:
            con.row_factory = sqlite3.Row
            cur = con.cursor()
            cur.execute("SELECT * FROM Placement")
            rows = cur.fetchall()
            for row in rows:
                Voiture(row["immatriculation"], row["longueur"], row["largeur"], row["hauteur"])
        con.close()