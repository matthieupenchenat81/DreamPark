from random import *
from Developpement.DreamPark.Model.Parking.Place import *
from Developpement.DreamPark.Model.Abonnement.Client import *
from Developpement.DreamPark.Model.Abonnement.Type import *
import sqlite3

# Test connexion base de données

conn = sqlite3.connect("test.db")

curseur = conn.cursor()

curseur.execute("DROP TABLE IF EXISTS Client")
curseur.execute("""create table Client (numClient varchar(10) PRIMARY KEY, nomClient varchar(30), prenomClient varchar(30), adrClient varchar(50), typeClient int(1))""")

curseur.execute("""insert into etudiants values (100, 'Brahim')""")
curseur.execute("""insert into Client values ("ABC", "PEREIRA", "Alexandre", "4 Boulevard Koenings\n 31300 Toulouse", 0)""")
conn.commit()
conn.close()

# On teste la persistance

con = sqlite3.connect("test.db")

with con:

    con.row_factory = sqlite3.Row

    cur = con.cursor()
    cur.execute("SELECT * FROM Client")

    rows = cur.fetchall()

    for row in rows:
        print("%s %s %s" % (row["Id"], row["Name"], row["Price"]))



print("Définition des places de bases...", end="")
placeType = [[1.2,2.3,1.5],[1.8,3.0,1.9],[3,5,2.6]] # hauteur, largeur, longueur de 3 types de places
for i in range(0,20) :
    choosenPlaceType = placeType[randint(0,2)];
    Place(i, randint(1,2), choosenPlaceType[0], choosenPlaceType[1], choosenPlaceType[2])
Place.saveAll()
print("OK\n")

print("Définition des Clients...", end="")
Client("ABC", "PEREIRA", "Alexandre", "4 Boulevard Koenings\n 31300 Toulouse", Type.SUPER_ABONNE)
Client("ABCD", "PENCHENAT", "Mathieu", "2 Impasse Louis Tharaud\n 31300 Toulouse", Type.ABONNE)
Client.saveAll()
print("OK\n")


Client.loadAll()
