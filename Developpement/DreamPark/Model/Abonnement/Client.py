import random
import sqlite3
import string

from Developpement.DreamPark.Model.Parking.Place import Place
from Developpement.DreamPark.Model.Parking.Voiture import Voiture


class Client:
    """
    La Classe Client: une instance de Client peut être un utilisateur non abonné, ou un utilisateur abonné.
    Il y a deux types d'utilisateur abonné: les abonnés simple et les super abonnés (qui ont une place toujours réservé)
    """

    tous = []

    @staticmethod
    def get(key):
        """
        Cette fonction permet de retourner un client. L'id d'un client est passé en paramètre et cette fonction retourne le client associé.
        :param key:
        :return Client:
        """
        for item in Client.tous:
            if (item.num == key): return item
        return None

    @staticmethod
    def generateId():
        """
        Cette méthode generateId permet de générer un id Utilisateur

        :return String:
        """
        d = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(8))
        while Client.get(d) != None:
            d = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(8))
        return d

    @property
    def prenom(self):
        """
        Cette propriété permet de récupérer le prenom du client

        :return String:
        """
        return self.__prenom

    @property
    def nom(self):
        """
        Cette propriété permet de récupérer le nom du client

        :return String:
        """
        return self.__nom

    @property
    def num(self):
        """
        Cette propriété permet de récupérer le numéro du client

        :return String:
        """
        return self.__num

    @property
    def adr(self):
        """
        Cette propriété permet de récupérer l'adresse du client

        :return String:
        """
        return self.__adresse

    @property
    def cryptoVisuel(self):
        """
        Cette propriété permet de récupérer le cryptogramme visuel de la carte bancaire du client

        :return String:
        """
        return self.__cryptoVisuel

    @property
    def numCB(self):
        """
        Cette propriété permet de récupérer le numéro de la carte bancaire de l'utilisateur

        :return String:
        """
        return self.__numCB

    @property
    def voiture(self):
        """
        Cette propriété permet de récupérer la voiture du client.

        :return Voiture:
        """
        return self.__voiture

    @property
    def dateExpiration(self):
        """
        Cette propriété permet de retourner la date d'expiration de la carte bancaire du client

        :return String:
        """
        return self.__dateExpiration

    @property
    def placeReserve(self):
        """
        Cette propriété permet de retourner la place réservé du client

        :return Place:
        """
        return self.__placeReserve

    @property
    def estAbonne(self):
        """
        Cette propriété permet de savoir si le client est un client abonné ou non

        :return Boolean:
        """
        return self.__estAbonne

    def __init__(self, nom, prenom, adresse, estAbonne, voiture, numCB, cryptoVisuel, dateExpiration, placeReserve,
                 num=None):
        """
        Ceci est le constructeur de la classe Client. A la création du client, l'objet est ajouté dans l'attribut de classe Client.tous.
        :param nom:
        :param prenom:
        :param adresse:
        :param estAbonne:
        :param voiture:
        :param numCB:
        :param cryptoVisuel:
        :param dateExpiration:
        :param placeReserve:
        :param num:
        """
        self.__num = Client.generateId() if num == None else num
        self.__dateExpiration = dateExpiration
        self.__voiture = voiture
        self.__placeReserve = placeReserve
        self.__numCB = numCB
        self.__cryptoVisuel = cryptoVisuel
        self.__nom = nom
        self.__prenom = prenom
        self.__estAbonne= estAbonne
        self.__adresse = adresse
        self.tous.append(self)

    @staticmethod
    def loadAll():
        """
        Cette fonction permet de charger tous les clients qui sont dans la base de donnée.
        Chaque client présent dans la base de données sont alors instancié.

        """
        con = sqlite3.connect("test.db")
        with con:
            con.row_factory = sqlite3.Row
            cur = con.cursor()
            for row in cur.execute("""SELECT * FROM Client"""):
                Client(row["nomClient"], row["prenomClient"], row["adrClient"],
                       True if (row["estAbonne"] == 1) else False,
                       Voiture.get(row["idVoiture"]), row["numCB"], row["cryptoVisuel"], row["dateExpiration"],
                       Place.get(row["placeReserve"]), row["numClient"])
        con.close()

    @staticmethod
    def saveAll():

        """
        Cette fonction permet de sauvegarder dans la base de données la totalité des client instancié dans l'application

        """
        conn = sqlite3.connect("test.db")
        curseur = conn.cursor()
        # reset table Client
        curseur.execute("delete from Client")
        # insert clients
        for c in Client.tous:
            curseur.execute("insert into Client values (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (
                c.num, c.nom, c.prenom, c.adr, c.estAbonne, c.voiture.immatriculation, c.numCB, c.cryptoVisuel,
                c.dateExpiration, None if (c.placeReserve == None) else c.placeReserve.id))
        conn.commit()
        conn.close()

    def __str__( self ):
        """
        Cette fonction permet de retourner un objet client sous forme de chaine de caractère.

        :return String:
        """
        tmpP = "-" if self.__prenom == None else self.__prenom
        tmpN = "-" if self.__nom == None else self.__nom
        return "( " + self.__num + ", " + tmpN + " " + tmpP + " )"

    def hasParkedCar(self):
        """
        Cette fonction permet de savoir si le client a déjà garé sa voiture

        :return Boolean:
        """
        from Developpement.DreamPark.Model.Parking.Placement import Placement

        for item in Placement.tous:
            if (item.client == self and not item.dateF):
                return True
        return False

    def recupererVehicule(self):
        """
        Cette fonction permet au client de récupérer sa voiture. En appelant cette méthode, le placement est alors finalisé.
        Si la récupération se passe avec succès, cette fonction retourne True ou False sinon.

        :return Boolean:
        """
        from Developpement.DreamPark.Model.Parking.Placement import Placement

        for pc in Placement.tous:
            if (pc.client == self and not pc.dateF):
                from datetime import datetime

                pc.dateF = datetime.today().strftime("%d/%m/%Y %H:%M:%S")
                return True
        return False

    @staticmethod
    def getNbSuperAbonne():
        """
        Cette fonction permet de retourner le nombre de super abonnés dans le parking.

        :return Integer:
        """
        i = 0
        for c in Client.tous:
            print(c.placeReserve)
            if c.placeReserve:
                i = i + 1
        return i

    @staticmethod
    def getNbAbonne():
        """
        Cette fonction permet de retourner le nombre d'abonnés dans le parking.

        :return Integer:
        """
        i = 0
        for c in Client.tous:
            if c.estAbonne:
                i = i + 1
        return i