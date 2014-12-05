class Place:

    def __init__(self, id, niveau, hauteur, largeur, longueur, voiture=None):
        self.__id = id
        self.__hauteur = hauteur
        self.__largeur = largeur
        self.__longueur = longueur
        self.__voiture = voiture
        self.__niveau = niveau

    def __str__(self):
         return "Place, id : " + str(self.__id)

    def estLibre(self):
        ...