import unittest
from Developpement.DreamPark.Model.Abonnement.Client import Client
from Developpement.DreamPark.Model.Parking.Place import Place
from Developpement.DreamPark.Model.Parking.Placement import Placement
from Developpement.DreamPark.Model.Parking.Voiture import Voiture

class ClientTest(unittest.TestCase):

    def test_create(self):
        v1 = Voiture()
        c = Client("PEREIRA", "Alexandre", "4 Boulevard Koenings 31300 Toulouse", True, v1, 12363663, 144, "12/12/1212", None)
        self.assertEqual(c.nom, "PEREIRA")
        self.assertEqual(c.prenom, "Alexandre")
        self.assertEqual(c.adr, "4 Boulevard Koenings 31300 Toulouse")
        self.assertEqual(c.placeReserve, None)
        self.assertEqual(c.cryptoVisuel, 144)
        self.assertEqual(c.dateExpiration, "12/12/1212")
        self.assertEqual(c.estAbonne, True)
        self.assertEqual(c.numCB, 12363663)
        self.assertEqual(c.voiture, v1)

    def test_get(self):
        v1 = Voiture()
        c = Client("PEREIRA", "Alexandre", "4 Boulevard Koenings 31300 Toulouse", True, v1, 12363663, 144, "12/12/1212", None, "W9V69Q27")
        self.assertEqual(c.num, "W9V69Q27")

    def test_generateId(self):
        for i in range(1, 100):
            str1 = Client.generateId()
            str2 = Client.generateId()
            self.assertNotEqual(str1, str2)

    def test_hasParkedCar(self):
        v1 = Voiture()
        c1 = Client("PEREIRA", "Alexandre", "4 Boulevard Koenings 31300 Toulouse", True, v1, 12363663, 144, "12/12/1212", None, "W9V69Q27")
        self.assertEqual(c1.hasParkedCar(), False)

        p2 = Place(1, 300, 200, 500, 778)
        Placement(None, p2, c1, "date..", None)
        self.assertEqual(c1.hasParkedCar(), True)

    def test_recupererVehicule(self):
        v1 = Voiture()
        c1 = Client("PEREIRA", "Alexandre", "4 Boulevard Koenings 31300 Toulouse", True, v1, 12363663, 144, "12/12/1212", None, "W9V69Q27")
        p2 = Place(1, 300, 200, 500, 778)

        self.assertEqual(c1.recupererVehicule(), False)
        Placement(None, p2, c1, "date..", None)
        self.assertEqual(c1.recupererVehicule(), True)

    def test_getNbSuperAbonne(self):
        Client.tous = []
        self.assertEqual(Client.getNbSuperAbonne(), 0)

        Client("PEREIRA", "Alexandre", "4 Boulevard Koenings 31300 Toulouse", True, Voiture(), 12363663, 144, "12/12/1212", None, "W9V69Q27")
        self.assertEqual(Client.getNbSuperAbonne(), 1)

    def test_getNbAbonne(self):
        Client.tous = []
        self.assertEqual(Client.getNbAbonne(), 0)

        Client("PEREIRA", "Alexandre", "4 Boulevard Koenings 31300 Toulouse", True, Voiture(), 12363663, 144, "12/12/1212", None, "W9V69Q27")
        self.assertEqual(Client.getNbAbonne(), 1)

if __name__ == '__main__':
    unittest.main()