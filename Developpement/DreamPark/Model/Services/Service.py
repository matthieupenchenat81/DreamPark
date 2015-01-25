class Service:
    tous = []

    def __init__(self, type, argument):
        self.__id = len(Service.tous)
        self.__type = type
        self.__argument = argument