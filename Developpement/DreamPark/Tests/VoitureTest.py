import unittest


class VoitureTest(unittest.TestCase):
    def test_get_element(self):
        simple_comme_bonjour = ('pomme', 'banane')
        self.assertEqual('pomme', 'pomme')


if __name__ == '__main__':
    unittest.main()