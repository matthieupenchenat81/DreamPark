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

    def __init__(self, dateDemande, dateFin, typeService, argument=None):
        self.__dateD = dateDemande
        self.__dateF = dateFin
        self.__typeService = typeService
        self.__argument = argument

    def effectuerTache(self):
        now = datetime.datetime.now()
        self.__dateF = now.strftime("%d-%m-%Y")