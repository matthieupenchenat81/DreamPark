from random import randint
import unittest
from Developpement.DreamPark.Model.Parking.Place import Place


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

if __name__ == '__main__':
    unittest.main()