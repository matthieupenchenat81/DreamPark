class Voiture:

    def __init__(self, longueur, largeur, hauteur, immatriculation):
        self.__longueur = longueur
        self.__largeur = largeur
        self.__hauteur = hauteur
        self.__immatriculation = immatriculation

    def __str__(self):
         return "Voiture, " + str(self.__longueur) + "x" + str(self.__largeur) + "x" + str(self.hauteur)