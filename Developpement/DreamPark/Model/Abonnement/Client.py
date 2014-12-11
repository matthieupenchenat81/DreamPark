import sqlite3

class Client:

    tous = []

    def __init__(self, num, nom, prenom, adresse, typeAbonnement):
        self.__num = num
        self.__nom = nom
        self.__prenom = prenom
        self.__typeAbonnement = typeAbonnement
        self.__adresse = adresse
        self.__placements = []
        self.tous.append(self)

    @staticmethod
    def loadAll():
        # On teste la persistance

        conn = sqlite3.connect("test.db")
        curseur = conn.cursor()
        for ligne in curseur.execute("""select * from client"""):
            print(ligne)
        conn.close()

    @staticmethod
    def saveAll():
        ...


