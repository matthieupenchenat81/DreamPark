from Developpement.DreamPark.Controler.HomeControler import *
from Developpement.DreamPark.Model.Abonnement.Client import *
from Developpement.DreamPark.Model.Parking.Placement import *
from Developpement.DreamPark.Model.Parking.Voiture import *
from Developpement.DreamPark.Model.Parking.Place import *

# on charge la bdd
Client.loadAll()
Voiture.loadAll()
Place.loadAll()
Placement.loadAll()




hc = HomeControler()

