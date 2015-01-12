import sqlite3

class Place:

    tous = []

    def __init__(self, id, niveau, hauteur, largeur, longueur, voiture=None):
        self.__id = id
        self.__hauteur = hauteur
        self.__largeur = largeur
        self.__longueur = longueur
        self.__voiture = voiture
        self.__niveau = niveau
        self.tous.append(self)

    def __str__(self):
         return "Place[ id : " + str(self.__id) + ", niveau : " + str(self.__niveau) + ", hauteur : "+ str(self.__hauteur) + ", largeur : "+ str(self.__largeur)+ ", longueur : "+ str(self.__longueur)+ ", voiture : "+str(self.__voiture)+"]"

    @property
    def estLibre(self):
        return (self.__voiture == None)

    @property
    def id(self):
        return self.__id

    @property
    def hauteur(self):
        return self.__hauteur

    @property
    def largeur(self):
        return self.__largeur

    @property
    def longueur(self):
        return self.__longueur

    @property
    def voiture(self):
        return self.__voiture

    @property
    def niveau(self):
        return self.__niveau

    @staticmethod
    def hasSpace(self, voiture):
        for i in Place.tous:
            if(i.hauteur >= voiture.hauteur & i.largeur >= voiture.largeur & i.hauteur == voiture.hauteur & i.estLibre): return i.id
        return False


    def utiliserPlace(self):
        if self.estLibre():
            self.__estLibre = False
        else:
            print("Erreur, place non libre")

    @staticmethod
    def loadAll():
        con = sqlite3.connect("test.db")
        with con:
            con.row_factory = sqlite3.Row
            cur = con.cursor()
            cur.execute("SELECT * FROM Place")
            rows = cur.fetchall()
            for row in rows:
                Place(row["id"], row["hauteur"], row["longueur"], row["largeur"], int(row["niveau"]))
        con.close()

    @staticmethod
    def saveAll():

        # connect table
        conn = sqlite3.connect("test.db")
        curseur = conn.cursor()
        #reset table Client
        curseur.execute("DROP TABLE IF EXISTS Place")
        curseur.execute("""create table Place (id int PRIMARY KEY, hauteur decimal(4,2), longueur decimal(4,2), largeur decimal(4,2), idVoiture int, niveau int)""")
        # insert clients
        for c in Place.tous:
            curseur.execute("insert into Place values (?, ?, ?, ?, ?, ?)", (c.id, c.hauteur, c.largeur, c.longueur, c.voiture, c.niveau))
        conn.commit()
        conn.close()