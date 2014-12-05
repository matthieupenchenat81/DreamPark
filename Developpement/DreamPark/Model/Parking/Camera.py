from random import uniform

class Camera:
    def __init__(self):
        ...

    def capturerHauteur(self):
        return uniform(1, 2)

    def capturerLongueur(self):
        return uniform(2, 4)

    def capturerLargeur(self):
        return uniform(1.3, 2.2)