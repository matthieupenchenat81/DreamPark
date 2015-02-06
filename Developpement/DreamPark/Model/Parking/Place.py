import sqlite3

class Place:
    """
    Cette classe représente une place de parking
    """

    tous = []

    def __init__(self, niveau, hauteur, longueur, largeur, id=None):
        """
        Constructeur de la classe Place
        :param niveau: Integer
        :param hauteur: Integer
        :param longueur: Integer
        :param largeur: Integer
        :param id: Integer
        """
        self.__id = id if (id != None) else len(Place.tous)
        self.__hauteur = hauteur
        self.__largeur = largeur
        self.__longueur = longueur
        self.__niveau = niveau
        self.tous.append(self)

    def __str__(self):
         """
        Cette méthode permet de retourner l'objet place sous forme de chaine de caractère

         :return: String
         """
         return "Place[ id : " + str(self.__id) + ", niveau : " + str(self.__niveau) + ", hauteur : "+ str(self.__hauteur) + ", largeur : "+ str(self.__largeur)+ ", longueur : "+ str(self.__longueur)+ "]"

    @property
    def id(self):
        """
        Cette fonction permet de retourner l'id de la place

        :return: Integer
        """
        return self.__id

    @property
    def hauteur(self):
        """
        Cette fonction permet de retourner la hauteur de la place

        :return: Integer
        """
        return self.__hauteur

    @property
    def largeur(self):
        """
        Cette fonction permet de retourner la largeur de la place

        :return: Integer
        """
        return self.__largeur

    @property
    def longueur(self):
        """
        Cette fonction permet de retourner la longueur de la place

        :return: Integer
        """
        return self.__longueur

    @property
    def niveau(self):
        """
        Cette fonction permet de retourner le niveau de la place

        :return: Integer
        """
        return self.__niveau

    @staticmethod
    def get(key):
        """
        Cette méthode permet de retourner la place avec l'id donné en paramètre
        :param key: Integer
        :return: Place
        """
        for item in Place.tous:
            if (item.id == key): return item
        return None

    @staticmethod
    def loadAll():
        """
        Cette fonction permet de charger la liste des places contenu dans la base de données. Chaque place est alors instancié dans l'application

        """
        con = sqlite3.connect("test.db")
        with con:
            con.row_factory = sqlite3.Row
            cur = con.cursor()
            cur.execute("SELECT * FROM Place")
            rows = cur.fetchall()
            for row in rows:
                Place(row["niveau"], row["hauteur"], row["longueur"], row["largeur"], row["id"])
        con.close()

    @staticmethod
    def saveAll():

        """
        Cette fonction permet de sauvegarder la totalité des objet instancié de l'application dans la base de données.

        """
        conn = sqlite3.connect("test.db")
        curseur = conn.cursor()
        #reset table Place
        curseur.execute("delete from Place")
        # insert places
        for c in Place.tous:
            curseur.execute("insert into Place values (?, ?, ?, ?, ?)",
                            (c.niveau, c.hauteur, c.longueur, c.largeur, c.id))
        conn.commit()
        conn.close()


    def isAvailable(self):
        """
        Cette fonction permet de tester si cette place est disponible

        :return: Boolean
        """
        from Developpement.DreamPark.Model.Abonnement.Client import Client
        from Developpement.DreamPark.Model.Parking.Placement import Placement

        for c in Client.tous:
            if c.placeReserve == self: return False
        for pc in Placement.tous:
            if pc.place == self and pc.dateF == None: return False
        return True

    @staticmethod
    def getAvailablePlace(voiture):
        """
        Cette méthode permet de retourner une place disponible et de bonne dimension par rapport à la voiture donnée en paramètre.
        Si aucune place n'est disponible, None est retourné
        :param voiture: Voiture
        :return: Place
        """
        for i in Place.tous:
            if (i.hauteur >= voiture.hauteur and i.largeur >= voiture.largeur and i.hauteur >= voiture.hauteur):
                if i.isAvailable(): return i
        return None