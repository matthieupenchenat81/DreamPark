import datetime
from enum import Enum

class Service:

    class TypeService(Enum):
        MAINTENANCE = 1
        ENTRETIEN = 2
        LIVRAISON = 3

    @property
    def typeService(self):
        return self.__typeService

    def __init__(self, idClient, dateDemande, dateService, typeService, adresse = None, rapport=None):
        from Developpement.DreamPark.Model.Abonnement.Client import Client
        self.__client = Client.get(idClient)
        self.__dateD = dateDemande
        self.__dateF = dateService
        self.__typeService = typeService
        if typeService == Service.TypeService.LIVRAISON: self.__adr = adresse
        self.__rapport = rapport

    def effectuerTache(self, x):

        now = datetime.datetime.now()
        self.__dateF = now.strftime("%d-%m-%Y")
        return {
            1 : self.effectuerMaintenance(),
            2 : self.effectuerEntretien(),
            3 : self.effectuerLivraison(),
        }[x]

    def effectuerMaintenance(self):
        self.__rapport += "Maintenance effectué"

    def effectuerEntretien(self):
        self.__rapport += "Entretien effectué"

    def effectuerLivraison(self):
        self.__client.recupererVehicule()
