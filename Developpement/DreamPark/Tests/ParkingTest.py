import unittest
from Developpement.DreamPark.Model.Parking.Parking import Parking
from Developpement.DreamPark.Model.Parking.Place import Place


class ParkingTest(unittest.TestCase):

    def test_createParking(self):
        p = Parking()
        self.assertEqual(p.places, [])

        places = [Place(1, 300, 200, 500, 777), Place(2, 300, 129, 500, 999)]
        p2 = Parking(places)
        self.assertEqual(p2.places, places)

if __name__ == '__main__':
    unittest.main()