from Developpement.DreamPark.Controler.HomeControler import *
from Developpement.DreamPark.Model.Abonnement.Client import *
from Developpement.DreamPark.Model.Parking.Placement import *

# on charge la bdd
Client.loadAll()
Placement.loadAll()

#Place.loadAll()
#Voiture.loadAll()


hc = HomeControler()

