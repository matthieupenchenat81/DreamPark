import unittest
from Developpement.DreamPark.Model.Parking.Voiture import Voiture

class VoitureTest(unittest.TestCase):

    def test_create_voiture(self):
        v= Voiture()
        self.assertNotEquals(v.immatriculation, None)
        self.assertNotEquals(v.hauteur, None)
        self.assertNotEquals(v.largeur, None)
        self.assertNotEquals(v.longueur, None)

    def test_get_voiture(self):
        v= Voiture()
        self.assertEquals(v, Voiture.get(v.immatriculation))

    def test_get_dim(self):
        v= Voiture("IMMAT", 100, 200, 300)
        self.assertEquals(v.hauteur, 300)
        self.assertEquals(v.longueur, 100)
        self.assertEquals(v.largeur, 200)

    def test_get_id(self):
        v= Voiture("IMMAT", 100, 200, 300)
        self.assertEquals(v.immatriculation, "IMMAT")


if __name__ == '__main__':
    unittest.main()