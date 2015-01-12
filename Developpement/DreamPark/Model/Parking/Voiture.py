from Developpement.DreamPark.Model.Parking import Camera

class Voiture:

    def __init__(self, immatriculation):
        self.__longueur = Camera.capturerLongueur()
        self.__largeur = Camera.capturerLargeur()
        self.__hauteur = Camera.capturerHauteur()
        self.__immatriculation = immatriculation

    def __str__(self):
         return "Voiture, " + str(self.__longueur) + "x" + str(self.__largeur) + "x" + str(self.hauteur) + ", Immatr : " + self.__immatriculation

    @classmethod
    def loadAll(self):
        ...