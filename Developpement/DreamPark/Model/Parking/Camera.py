from random import uniform
import uuid


class Camera:

    @staticmethod
    def capturerHauteur():
        return uniform(100, 300)

    @staticmethod
    def capturerLongueur():
        return uniform(200, 600)

    @staticmethod
    def capturerLargeur():
        return uniform(100, 250)

    @staticmethod
    def capturerImmat():
        return uuid.uuid4();
