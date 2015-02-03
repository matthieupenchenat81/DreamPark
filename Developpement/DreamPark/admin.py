from Developpement.DreamPark.Controler.AdminControler import *
from Developpement.DreamPark.Model.Parking.Placement import *
from Developpement.DreamPark.Model.Parking.Voiture import *
from Developpement.DreamPark.Model.Parking.Place import *

# on charge la bdd
Voiture.loadAll()
Place.loadAll()
Client.loadAll()
Placement.loadAll()
Service.loadAll()

hc = AdminControler()

