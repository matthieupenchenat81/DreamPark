from enum import Enum

class Type(Enum):
    ABONNE = 1
    SUPER_ABONNE = 2

class Client:
    def __init__(self, nom, prenom, adresse, typeAbonnement):
        self.__nom = nom
        self.__prenom = prenom
        self.__typeAbonnement = typeAbonnement