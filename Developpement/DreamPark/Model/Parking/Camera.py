import string
import random
from random import uniform

from Developpement.DreamPark.Model.Parking.Voiture import Voiture


class Camera:

    @staticmethod
    def capturerHauteur():
        return uniform(100, 300)

    @staticmethod
    def capturerLongueur():
        return uniform(100, 150)

    @staticmethod
    def capturerLargeur():
        return uniform(100, 220)

    @staticmethod
    def capturerImmat():
        chars1 = "".join([random.choice(string.ascii_uppercase) for _ in range(2)])
        digits = "".join([random.choice(string.digits) for _ in range(3)])
        chars2 = "".join([random.choice(string.ascii_uppercase) for _ in range(2)])
        digits2 = "".join([random.choice(string.digits) for _ in range(2)])
        d = chars1 + "-" + digits + "-" + chars2 + "(" + digits2 + ")"

        while Voiture.get(d) != None:
            chars1 = "".join([random.choice(string.ascii_uppercase) for _ in range(2)])
            digits = "".join([random.choice(string.digits) for _ in range(3)])
            chars2 = "".join([random.choice(string.ascii_uppercase) for _ in range(2)])
            digits2 = "".join([random.choice(string.digits) for _ in range(2)])
            d = chars1 + "-" + digits + "-" + chars2 + "(" + digits2 + ")"
        return d