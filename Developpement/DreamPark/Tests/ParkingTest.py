import unittest
from Developpement.DreamPark.Model.Parking.Parking import Parking
from Developpement.DreamPark.Model.Parking.Place import Place


class ParkingTest(unittest.TestCase):

    def test_createParking(self):
        p = Parking()
        self.assertEqual(p.places, [])

        places = [Place(1, 100, 200, 300), Place(2, 200, 100, 350)]
        p2 = Parking(places)
        self.assertEqual(p.places, places)

if __name__ == '__main__':
    unittest.main()