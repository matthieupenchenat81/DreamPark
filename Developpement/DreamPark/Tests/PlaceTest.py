import unittest
from Developpement.DreamPark.Model.Abonnement.Client import Client
from Developpement.DreamPark.Model.Parking.Place import Place
from Developpement.DreamPark.Model.Parking.Placement import Placement
from Developpement.DreamPark.Model.Parking.Voiture import Voiture


class PlaceTest(unittest.TestCase):

    def test_create_place(self):
        p = Place(1, 300, 200, 500, 777)
        self.assertEquals(p.id, 777)
        self.assertEquals(p.niveau, 1)
        self.assertEquals(p.hauteur, 300)
        self.assertEquals(p.longueur, 200)
        self.assertEquals(p.largeur, 500)

    def test_get(self):
        p = Place(1, 300, 200, 500, 777)
        self.assertEqual(Place.get(7797), None)
        self.assertEqual(str(Place.get(777)), str(p))

    def test_isAvailable(self):
        p = Place(1, 300, 200, 500, 777)
        self.assertEqual(p.isAvailable(), True)

        # la place a été réservé
        c = Client("PEREIRA", "Alexandre", "4 Boulevard Koenings 31300 Toulouse", True, Voiture(), 12363663, 144, "12/12/1212", p, None)
        self.assertEqual(p.isAvailable(), False)

        p2 = Place(1, 300, 200, 500, 778)
        Placement(None, p2, c, "date..", None)
        self.assertEqual(p2.isAvailable(), False)

    def test_getAvailablePlace(self):
        Place.tous = []
        p2 = Place(1, 300, 200, 500, 788)
        c = Client("PEREIRA", "Alexandre", "4 Boulevard Koenings 31300 Toulouse", True, Voiture(), 12363663, 144, "12/12/1212", p2, None)

        Placement(None, p2, c, "date..", None)
        self.assertEqual(p2.isAvailable(), False)
        v= Voiture("IMMAT", 100, 200, 40)
        self.assertEqual(Place.getAvailablePlace(v), None)

        p2 = Place(1, 300, 200, 500, 788)
        self.assertNotEqual(Place.getAvailablePlace(v), None)
        self.assertEqual(Place.getAvailablePlace(v), p2)

if __name__ == '__main__':
    unittest.main()