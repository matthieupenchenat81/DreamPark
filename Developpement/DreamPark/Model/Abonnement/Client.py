class Client:

    def __init__(self, nom, prenom, typeAbonnement, adresse):
        self.__nom = nom
        self.__prenom = prenom
        self.__typeAbonnement = typeAbonnement
        self.__adresse = adresse
        self.__placements = []

    @classmethod
    def loadAll(self):
        ...


