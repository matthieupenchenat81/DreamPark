import sqlite3

from Developpement.DreamPark.Model.Abonnement.Client import Client
from Developpement.DreamPark.Model.Parking.Place import Place
from Developpement.DreamPark.Model.Services.Service import Service


class Placement:
    """
    Un placement est associé à une place et un client.
    Un placement est défini dans une intervalle de temps entre la date de départ et la date de fin
    """

    tous = []

    def __init__(self, id, place, client, dateD, dateF=None):
        """
        Constructeur de la classe Placement
        :param id: Integer
        :param place: Place
        :param client: Client
        :param dateD: String
        :param dateF: String
        """
        self.__id = id if (id != None) else len(Placement.tous)
        self.__place = place
        self.__client = client
        self.__dateD = dateD
        self.__dateF = dateF
        self.__services = self.getServices()
        self.tous.append(self)

    @property
    def estEnCours(self):
        """
        Cette propriété permet de savoir si le placement est en cours ou s'il est terminé

        :return: Boolean
        """
        return (self.__dateF == None)

    @property
    def place(self):
        """
        Cette propriété permet de retourné la place associé au placement

        :return: Boolean
        """
        return self.__place

    @property
    def id(self):
        """
        Cette propriété permet de retourner l'identifiant de la classe Placement

        :return: Integer
        """
        return self.__id

    def getServices(self):
        """
        Cette méthode permet de retourner la liste des services associés à ce placement

        :return: Liste de Service
        """
        services = []
        for s in Service.tous:
            if (s.placement == self): services.append(s)
        return services

    @property
    def services(self):
        """
        Cette propriété permet de retourner la liste des services associés à notre placement

        :return: Liste de Service
        """
        return self.__services

    @property
    def client(self):
        """
        Cette méthode permet de retourner le client associé au placement

        :return: Client
        """
        return self.__client

    @property
    def dateD(self):
        """
        Cette propriété permet de retourner la date de départ du placement

        :return: String
        """
        return self.__dateD

    @property
    def dateF(self):
        """
        Cette propriété permet de retourner la date finale du placement

        :return: String
        """
        return self.__dateF

    @dateF.setter
    def dateF(self, value):
        """
        Cette méthode permet de modifier la valeur de la date finale du placement
        :param value: String
        """
        self.__dateF = value

    @staticmethod
    def loadAll():
        """
        Cette méthode permet de charger la totalité des placements de la base de données dans l'aapplication.
        Chaque placement vont alors être instancié.

        """
        con = sqlite3.connect("test.db")
        with con:
            con.row_factory = sqlite3.Row
            cur = con.cursor()
            cur.execute("SELECT * FROM Placement")
            rows = cur.fetchall()
            for row in rows:
                Placement(row["id"], Place.get(row["place"]), Client.get(row["client"]), row["dateD"], row["dateF"])
        con.close()

    @staticmethod
    def saveAll():
        """
        Cette fonction permet de sauvegarder dans la base de données la totalité des objet placement instanciés dans notre application.

        """
        conn = sqlite3.connect("test.db")
        curseur = conn.cursor()
        #reset table Placement
        curseur.execute("delete from Placement")
        # insert Placement
        for c in Placement.tous:
            print(c.place)
            curseur.execute("insert into Placement values (?, ?, ?, ?, ?)", (c.id, c.place.id, c.client.num, c.dateD,
                                                                             "" if c.dateF == None else c.dateF))
        conn.commit()
        conn.close()

    @staticmethod
    def get(id):
        """
        Cette fonction retourne le placement doté de l'identifiant passé en paramètre
        :param id: String
        :return: Placement
        """
        for p in Placement.tous:
            if p.id == id: return p
        return None

    @staticmethod
    def nbPlaceOccupes():
        """
        Cette fonction permet de retourner le nombre de place occupés du parking

        :return: Integer
        """
        i = 0
        for p in Placement.tous:
            if not p.dateF:
                i = i + 1
        return i