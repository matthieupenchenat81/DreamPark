from Model.Parking.Parking import Parking
from Model.Parking.Place import Place

print("Démarrage...")

places = []

for i in range(0,10) :
    places.append(Place(id, 1, 1, 1, voiture=None))


p1 = Parking(places)

for p in p1.places:
    print(p)