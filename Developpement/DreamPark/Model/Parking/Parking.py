class Parking:
    """
    Cette classe représente le parking, le parking qui est composé d'une liste de places
    """

    def __init__(self, places=[]):
        """
        Constructeur de la classe parking, il associe le parking à un ensemble de places
        :param places:
        """
        self.__places = places

    @property
    def places(self):
        """
        Cette fonction permet de retourner la liste des places du parking

        :return Liste de Place:
        """
        return self.__places