class Client:
    def __init__(self, nom, prenom, typeAabonnement, code):
        self.__nom = nom
        self.__prenom = prenom
        self.__typeAbonnement = typeAbonnement
        self.code = code

    def changerAbonnement(self, typeAbonnement):
        if typeAbonnement == None :
            del self
            #shelve

        else :
            self.typeAbonnement = typeAbonnement
