class Client:

    def __init__(self, nom, prenom, typeAbonnement, code):
        self.__nom = nom
        self.__prenom = prenom
        self.__typeAbonnement = typeAbonnement
        self.code = code

    def changerAbonnement(self, typeAbonnement):

        if typeAbonnement == None :
            del self
            #shelve

        else if Type.ABONNE:
            self.typeAbonnement = typeAbonnement
