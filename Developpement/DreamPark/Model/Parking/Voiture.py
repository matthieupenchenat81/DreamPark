import sqlite3

from Developpement.DreamPark.Model.Parking.Camera import Camera
from Developpement.DreamPark.Model.Parking.Place import Place


class Voiture:

    tous = []

    def __init__(self, immatriculation= None, longueur = None, largeur = None, hauteur = None):
        if (longueur == None and largeur == None and hauteur == None):
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
        self.__immatriculation = Camera.capturerImmat()

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
    def get(idCar):
        for item in Voiture.tous:
            if(item.immatriculation == idCar): return item
        return None

    @staticmethod
    def saveAll():
        # connect table
        conn = sqlite3.connect("test.db")
        curseur = conn.cursor()
        curseur.execute("delete from Voiture")
        for c in Voiture.tous:
            curseur.execute("insert into Voiture values (?, ?, ?, ?)", (str(c.immatriculation), int(c.longueur), int(c.largeur), int(c.hauteur)))
        conn.commit()
        conn.close()

    def getAvailablePlace(self):
        # TODO : Soustraire les places réservées
        for i in Place.tous:
            if (i.hauteur >= self.hauteur and i.largeur >= self.largeur and i.hauteur >= self.hauteur):
                for pc in Placement.tous:
                    if not (pc.place == i and pc.dateF != None and pc.client.placeReserve != pc.place):
                        tmp = i
                    else:
                        tmp = None

        return tmp