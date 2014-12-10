class Placement:

    def __init__(self, place, voiture, client, dateD, dateF=None):
        self.__voiture = voiture
        self.__place = place
        self.__client = client
        self.__dateD = dateD
        self.__dateF = dateF


    def partirPlace(self, dateF):
        self.__dateF = dateF

        # on libere la place
        self.__place

    @property
    def estEnCours(self):
        return (self.__dateF == None)
