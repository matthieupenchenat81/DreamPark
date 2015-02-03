import unittest
from Developpement.DreamPark.Model.Abonnement.Client import Client
from Developpement.DreamPark.Model.Parking.Place import Place
from Developpement.DreamPark.Model.Parking.Placement import Placement
from Developpement.DreamPark.Model.Parking.Voiture import Voiture
from Developpement.DreamPark.Model.Services.Service import Service


class PlacementTest(unittest.TestCase):

    def test_creer(self):
        p2 = Place(1, 300, 200, 500, 788)
        c = Client("PEREIRA", "Alexandre", "4 Boulevard Koenings 31300 Toulouse", True, Voiture(), 12363663, 144, "12/12/1212", p2, None)
        pp = Placement("ID", p2, c, "date..", None)

        self.assertEqual(pp.client, c)
        self.assertEqual(pp.dateD, "date..")
        self.assertEqual(pp.dateF, None)
        self.assertEqual(pp.id, "ID")
        self.assertEqual(pp.place, p2)
        self.assertEqual(pp.services, [])

    def test_estEnCours(self):
        p2 = Place(1, 300, 200, 500, 788)
        c = Client("PEREIRA", "Alexandre", "4 Boulevard Koenings 31300 Toulouse", True, Voiture(), 12363663, 144, "12/12/1212", p2, None)
        pp = Placement("ID", p2, c, "date..", None)
        self.assertEqual(pp.estEnCours, True)

    def test_getServices(self):
        p2 = Place(1, 300, 200, 500, 788)
        c = Client("PEREIRA", "Alexandre", "4 Boulevard Koenings 31300 Toulouse", True, Voiture(), 12363663, 144, "12/12/1212", p2, None)
        pp = Placement("ID", p2, c, "date..", None)
        s1 = Service(pp, "26/10/2015", 1, "Livraison")
        s2 = Service(pp, "28/10/2015", 2, "Livraison 2")
        self.assertEqual(pp.getServices(), [s1, s2])

    def test_get(self):
        Placement.tous = []
        p2 = Place(1, 300, 200, 500, 788)
        c = Client("PEREIRA", "Alexandre", "4 Boulevard Koenings 31300 Toulouse", True, Voiture(), 12363663, 144, "12/12/1212", p2, None)
        pp = Placement("ID", p2, c, "date..", None)
        self.assertEqual(Placement.get("ID"), pp)
        self.assertNotEqual(Placement.get("IDD"), pp)

    def test_nbPlaceOccupes(self):
        Placement.tous = []
        self.assertEqual(Placement.nbPlaceOccupes(), 0)

        p2 = Place(1, 300, 200, 500, 788)
        c = Client("PEREIRA", "Alexandre", "4 Boulevard Koenings 31300 Toulouse", True, Voiture(), 12363663, 144, "12/12/1212", p2, None)
        Placement("ID", p2, c, "date..", None)
        self.assertEqual(Placement.nbPlaceOccupes(), 1)

if __name__ == '__main__':
    unittest.main()