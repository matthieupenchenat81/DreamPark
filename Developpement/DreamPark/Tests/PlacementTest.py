import unittest

class CameraTest(unittest.TestCase):

    def test_caturerHauteur(self):
        for i in range(1, 5000):
            # -> random
            self.assertNotEqual(Camera.capturerHauteur(), Camera.capturerHauteur())
            self.assertNotEqual(Camera.capturerImmat(), Camera.capturerImmat())
            self.assertNotEqual(Camera.capturerLargeur(), Camera.capturerLargeur())
            self.assertNotEqual(Camera.capturerLongueur(), Camera.capturerLongueur())

if __name__ == '__main__':
    unittest.main()