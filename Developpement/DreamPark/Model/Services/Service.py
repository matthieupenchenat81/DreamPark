import datetime
from enum import Enum
import sqlite3


class Service:
    """
    La classe Service est associé à un placement. Il y a plusieurs type de service possible (maintenance, entretien, livraison)
    """

    tous = []

    class TypeService(Enum):
        MAINTENANCE = 1
        ENTRETIEN = 2
        LIVRAISON = 3

    @property
    def typeService(self):
        """
        Cette propriété permet de retourner le type de service du service
        MAINTENANCE = 1
        ENTRETIEN = 2
        LIVRAISON = 3

        :return: Integer
        """
        return self.__typeService

    @property
    def placement(self):
        """
        Cette propriété permet de retourner le placement associé au service

        :return: Placement
        """
        return self.__placement

    @property
    def dateF(self):
        """
        Cette propriété permet de retourner la date finale du service

        :return: String
        """
        return self.__dateF

    @dateF.setter
    def dateF(self, value):
        """
        Cette méthode permet de modifier la valeur de la dateFinale du service par ce qui est passé en paramètre
        :param value: String
        """
        self.__dateF = value

    @property
    def argument(self):
        """
        Cette propriété permet de retourner l'argument (qui est l'adresse de livraison) du service

        :return: String
        """
        return self.__argument

    def __init__(self, placement, dateFin, typeService, argument=None):
        """
        Constructeur de la classe Service
        :param placement: Placement
        :param dateFin: String
        :param typeService: Integer
        :param argument: String
        """
        self.__placement = placement
        self.__dateF = dateFin
        self.__typeService = typeService
        self.__argument = argument
        self.tous.append(self)

    def effectuerTache(self):
        """
        Cette méthode permet d'effectuer un service qui a été demandé par le client.

        """
        now = datetime.datetime.now()
        self.__dateF = now.strftime("%d-%m-%Y")

    @staticmethod
    def loadAll():
        """
        Cette méthode permet de charger la totalité des services de la base de données dans l'application.
        Chaque service est alors instancié dans l'application.
        """
        from Developpement.DreamPark.Model.Parking.Placement import Placement
        con = sqlite3.connect("test.db")
        with con:
            con.row_factory = sqlite3.Row
            cur = con.cursor()
            cur.execute("SELECT * FROM Service")
            rows = cur.fetchall()
            for row in rows:
                Service(Placement.get(row["placement"]), row["dateFin"], Service.TypeService(row["typeService"]),
                        row["argument"])
        con.close()

    @staticmethod
    def saveAll():
        """
        Cette méthode permet de sauvegarder la totalité des instances services de l'application dans la base de données
        """
        conn = sqlite3.connect("test.db")
        curseur = conn.cursor()
        #reset table Service
        curseur.execute("delete from Service")
        # insert Service
        for c in Service.tous:
            print(str(c.typeService.value))
            curseur.execute("insert into Service values (?, ?, ?, ?)",
                            (c.placement.id, "" if not c.dateF else c.dateF, c.typeService.value, c.argument))
        conn.commit()
        conn.close()