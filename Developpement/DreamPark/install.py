from random import *
from Developpement.DreamPark.Model.Abonnement.Client import *
from Developpement.DreamPark.Model.Abonnement.Type import *
import sqlite3

def initTable():
    # connect table
    conn = sqlite3.connect("test.db")
    curseur = conn.cursor()
    #voiture
    curseur.execute("DROP TABLE IF EXISTS Voiture")
    curseur.execute("""create table Voiture(immatriculation varchar(20) PRIMARY KEY, longueur int, largeur int, hauteur int)""")
    #client
    curseur.execute("DROP TABLE IF EXISTS Client")
    curseur.execute("""create table Client (numClient varchar(15) PRIMARY KEY, nomClient varchar(30), prenomClient varchar(30), adrClient varchar(50), typeClient int(1), idVoiture varchar(20), numCB int(20), cryptoVisuel int(3), dateExpiration varchar(10), FOREIGN KEY(idVoiture) REFERENCES Voiture(immatriculation))""")
    #place
    curseur.execute("DROP TABLE IF EXISTS Place")
    curseur.execute("""create table Place (id int PRIMARY KEY, hauteur decimal(4,2), longueur decimal(4,2), largeur decimal(4,2), idVoiture int, niveau int)""")
    #placement
    curseur.execute("DROP TABLE IF EXISTS Placement")
    curseur.execute("""create table Placement (place int, client int, dateD date, dateF date)""")

    conn.commit()
    conn.close()

initTable()

print("Définition des Clients...")
Client("PEREIRA", "Alexandre", "4 Boulevard Koenings 31300 Toulouse", Type.SUPER_ABONNE, "JJSJJ", 12363663, 144, "12/12/1212")
Client("PENCHENAT", "Matthieu", "2 Impasse Louis Tharaud 31300 Toulouse", Type.ABONNE, "KKJJSJJ", 12363669, 147, "12/12/1212")
Client.saveAll()

for client in Client.tous:
    print(client)

print("Définition des places de bases...", end="")
placeType = [[300,150,200],[150,200,300],[500,400,300]] # hauteur, largeur, longueur de 3 types de places
for i in range(0,20) :
    choosenPlaceType = placeType[randint(0,2)];
    Place(i, randint(1,2), choosenPlaceType[0], choosenPlaceType[1], choosenPlaceType[2])
Place.saveAll()

for place in Place.tous:
    print(place)
print("OK\n")
