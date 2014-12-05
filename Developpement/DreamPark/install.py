from Model.Parking import Parking, Place

print("Démarrage...")

places = []

for i in range(0,10) :
    places.append(Place(i, 1, 1, 1))


p1 = Parking(places)

for p in p1.places:
    print(p)