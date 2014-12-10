class Place:

    def __init__(self, id, niveau, hauteur, largeur, longueur, voiture=None):
        self.__id = id
        self.__hauteur = hauteur
        self.__largeur = largeur
        self.__longueur = longueur
        self.__voiture = voiture
        self.__niveau = niveau
        self.__estLibre = False;
        self.__placements = []

    def __str__(self):
         return "Place, id : " + str(self.__id)

    @property
    def estLibre(self):
        return 0

    def utiliserPlace(self):
        if self.estLibre():
            self.__estLibre = False
        else:
            print("Erreur, place non libre")

    @classmethod
    def loadAll(self):
        ...