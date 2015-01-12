import sqlite3


class Placement:

    tous = []

    def __init__(self, place, voiture, client, dateD, dateF=None):
        self.__voiture = voiture
        self.__place = place
        self.__client = client
        self.__dateD = dateD
        self.__dateF = dateF
        self.tous.append(self)

    def partirPlace(self, dateF):
        self.__dateF = dateF

        # on libere la place
        self.__place

    @property
    def estEnCours(self):
        return (self.__dateF == None)

    @staticmethod
    def loadAll():
        con = sqlite3.connect("test.db")
        with con:
            con.row_factory = sqlite3.Row
            cur = con.cursor()
            cur.execute("SELECT * FROM Placement")
            rows = cur.fetchall()
            for row in rows:
                Placement(row["id"], row["place"], row["voiture"], row["client"], row["dateD"], row["dateF"])
        con.close()

    @staticmethod
    def saveAll():

        # connect table
        conn = sqlite3.connect("test.db")
        curseur = conn.cursor()
        #reset table Client
        curseur.execute("DROP TABLE IF EXISTS Placement")
        curseur.execute("""create table Place (id int PRIMARY KEY, hauteur decimal(4,2), longueur decimal(4,2), largeur decimal(4,2), idVoiture int, niveau int)""")
        # insert clients
        for c in Placement.tous:
            curseur.execute("insert into Placement values (?, ?, ?, ?, ?, ?)", (c.id, c.hauteur, c.largeur, c.longueur, c.voiture, c.niveau))
        conn.commit()
        conn.close()

