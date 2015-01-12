from random import uniform

class Camera:

    @staticmethod
    def capturerHauteur(self):
        return uniform(100, 300)

    @staticmethod
    def capturerLongueur(self):
        return uniform(200, 600)

    @staticmethod
    def capturerLargeur(self):
        return uniform(100, 250)