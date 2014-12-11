import sqlite3

class Client:

    tous = []

    @staticmethod
    def get(num):
        for client in Client.tous:
            if client.__num == num:
                return client
        return None

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
        con = sqlite3.connect("test.db")
        with con:
            con.row_factory = sqlite3.Row
            cur = con.cursor()
            cur.execute("SELECT * FROM Client")
            rows = cur.fetchall()
            for row in rows:
                Client(row["numClient"], row["nomClient"], row["prenomClient"], row["adrClient"], int(row["typeClient"]))
        con.close()

    @staticmethod
    def saveAll():
        ...

    def __str__( self ):
        return "( " + self.__num +", " + self.__nom+", " + self.__prenom+", " + self.__adresse +", " + str(self.__typeAbonnement) +" )"


