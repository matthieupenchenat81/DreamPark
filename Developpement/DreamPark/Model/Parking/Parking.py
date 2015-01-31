class Parking:

    def __init__(self, places=[]):
        self.__places = places

    @property
    def places(self):
        return self.__places