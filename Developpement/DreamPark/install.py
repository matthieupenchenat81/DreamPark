from random import *
from Developpement.DreamPark.Model.Parking.Place import *
from Developpement.DreamPark.Model.Abonnement.Client import *

print("Définition des places de bases...", end="")
placeType = [[1.2,2.3,1.5],[1.8,3.0,1.9],[3,5,2.6]] # hauteur, largeur, longueur de 3 types de places
for i in range(0,20) :
    choosenPlaceType = placeType[randint(0,2)];
    Place(i, randint(1,2), choosenPlaceType[0], choosenPlaceType[1], choosenPlaceType[2])
Place.saveAll()
print("OK\n")

print("Définition des Clients...", end="")
Client("PEREIRA", "Alexandre", "4 Boulevard Koenings\n31300 Toulouse", Type.SUPER_ABONNE, "ABC")
Client("PENCHENAT", "Mathieu", "2 Impasse Louis Tharaud\n31300 Toulouse", Type.ABONNE, "ABCD")
Client.saveAll()
print("OK\n")
