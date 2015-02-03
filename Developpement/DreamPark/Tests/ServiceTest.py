import unittest
from Developpement.DreamPark.Model.Abonnement.Client import Client
from Developpement.DreamPark.Model.Parking.Place import Place
from Developpement.DreamPark.Model.Parking.Placement import Placement
from Developpement.DreamPark.Model.Parking.Voiture import Voiture
from Developpement.DreamPark.Model.Services.Service import Service


class ServiceTest(unittest.TestCase):

    def test_creerService(self):
        p2 = Place(1, 300, 200, 500, 788)
        c = Client("PEREIRA", "Alexandre", "4 Boulevard Koenings 31300 Toulouse", True, Voiture(), 12363663, 144, "12/12/1212", p2, None)
        pp = Placement("ID", p2, c, "date..", None)
        s = Service(pp, "26/10/2015", 1, "Livraison")
        self.assertEqual(s.dateF, "26/10/2015")
        self.assertEqual(s.argument, "Livraison")
        self.assertEqual(s.placement, pp)
        self.assertEqual(s.typeService, 1)

    def test_effectuerTache(self):
        p2 = Place(1, 300, 200, 500, 788)
        c = Client("PEREIRA", "Alexandre", "4 Boulevard Koenings 31300 Toulouse", True, Voiture(), 12363663, 144, "12/12/1212", p2, None)
        pp = Placement("ID", p2, c, "date..", None)
        s = Service(pp, None, 1, "Livraison")
        s.effectuerTache()
        self.assertNotEqual(s.dateF, None)

if __name__ == '__main__':
    unittest.main()