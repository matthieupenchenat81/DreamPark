from Developpement.DreamPark.Controler.HomeControler import *
from Developpement.DreamPark.Model.Parking.Placement import *
from Developpement.DreamPark.Model.Parking.Voiture import *
from Developpement.DreamPark.Model.Parking.Place import *

# on charge la bdd
Voiture.loadAll()
Client.loadAll()
Place.loadAll()
Placement.loadAll()
Service.loadAll()


hc = HomeControler()

