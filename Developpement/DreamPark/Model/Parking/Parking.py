class Parking:

    def __init__(self, places=[]):
        self.__places = places

    @property
    def places(self):
        return self.__places

    @property
    def placesAvailable(self):
        sum(1 for place in self.places if place.voiture == None)

    def getBestPlaceForVehicule(self, longueur, largeur, hauteur):
        for place in self.places:
            if not(place.vehicle) and longueur < place.longueur and largeur < place.largeur and hauteur < place.hauteur:
                #if(not(bestPlace) or bestPlace.longueur < )
                bestPlace = place
        return bestPlace

    def setPlaceForVehicule(self, place, vehicule):
        place.voiture = vehicule

    def freeVehicule(self, place):
        place.voiture = None



