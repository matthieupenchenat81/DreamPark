import sqlite3
class Voiture:
    """
    Cette classe représente une voiture. Une voiture est représenté par son immatriculation
    sa longueur, largeur ainsi que son hauteur.
    """

    tous = []

    def __init__(self, immatriculation= None, longueur = None, largeur = None, hauteur = None):
        """
        Le constructeur de la classe voiture instancie l'objet voiture et l'ajoute dans l'attribut de classe Voiture.tous.

        :param immatriculation:
        :param longueur:
        :param largeur:
        :param hauteur:
        """
        if (longueur == None and largeur == None and hauteur == None):
            self.setDim()
        else:
            self.__longueur = longueur
            self.__largeur = largeur
            self.__hauteur = hauteur
            self.__immatriculation = immatriculation
        self.tous.append(self)

    def setDim(self):
        """
        Cette méthode permet récupérer les valeurs prises par la caméra et de les assigner aux attributs de la voiture

        """
        from Developpement.DreamPark.Model.Parking.Camera import Camera
        self.__longueur = Camera.capturerLongueur()
        self.__hauteur = Camera.capturerHauteur()
        self.__largeur = Camera.capturerLargeur()
        self.__immatriculation = Camera.capturerImmat()

    @property
    def hauteur(self):
        """
        Cette propriété permet de retourner la hauteur de la voiture

        :return: Integer
        """
        return self.__hauteur

    @property
    def largeur(self):
        """
        Cette méthode permet de retourner la largeur de la voiture

        :return: Integer
        """
        return self.__largeur

    @property
    def longueur(self):
        """
        Cette méthode permet de retourner la longueur de la voiture

        :return: Integer
        """
        return self.__longueur

    @property
    def immatriculation(self):
        """
        Cette méthode permet de retourner l'immatricultaion de la voiture
        :return: String
        """
        return self.__immatriculation

    @staticmethod
    def get(key):
        """
        Cette méthode permet de retourner la voiture ayant l'immatriculation donné en paramètre
        :param key: String
        :return: Voiture
        """
        for item in Voiture.tous:
            if (item.immatriculation == key): return item
        return None


    @staticmethod
    def loadAll():
        """
        Cette méthode permet de charger la liste des voitures de la base de données en mémoire,
        Chaque voiture est alors instancié
        """
        con = sqlite3.connect("test.db")
        with con:
            con.row_factory = sqlite3.Row
            cur = con.cursor()
            cur.execute("SELECT * FROM Voiture")
            rows = cur.fetchall()
            for row in rows:
                Voiture(row["immatriculation"], row["longueur"], row["largeur"], row["hauteur"])
        con.close()

    @staticmethod
    def saveAll():
        """
        Cette méthode permet de sauvegarder la totalité des instances voiture dans la base de données
        """
        conn = sqlite3.connect("test.db")
        curseur = conn.cursor()
        curseur.execute("delete from Voiture")
        for c in Voiture.tous:
            curseur.execute("insert into Voiture values (?, ?, ?, ?)", (str(c.immatriculation), int(c.longueur), int(c.largeur), int(c.hauteur)))
        conn.commit()
        conn.close()
