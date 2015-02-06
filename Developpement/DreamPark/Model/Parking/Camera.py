import string
import random
from random import uniform
from Developpement.DreamPark.Model.Parking.Voiture import Voiture


class Camera:
    """
    Cette classe permet de créer une caméra fictive. Cette caméra génère la hauteur, longueur,
    la largeur ainsi que l'immatriculation d'un véhicule
    """

    @staticmethod
    def capturerHauteur():
        """
        Cette fonction permet de générer une hauteur aléatoirement entre 1 et 3 mètres

        :return Integer:
        """
        return uniform(100, 300)

    @staticmethod
    def capturerLongueur():
        """
        Cette fonction permet de générer une longueur aléatoirement entre 1 et 1,5 mètres

        :return Intéger:
        """
        return uniform(100, 150)

    @staticmethod
    def capturerLargeur():
        """
        Cette fonction permet de générer une largeur aléatoirement entre 1 et 2,2 mètres

        :return Integer:
        """
        return uniform(100, 220)

    @staticmethod
    def capturerImmat():
        """
        Cette fonction permet de générer l'immatriculation aléatoirement d'un véhicule

        :return String:
        """
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