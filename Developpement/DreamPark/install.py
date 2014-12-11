from random import *
from Developpement.DreamPark.Model.Parking.Place import *
from Developpement.DreamPark.Model.Abonnement.Client import *
from Developpement.DreamPark.Model.Abonnement.Type import *
import sqlite3

def initClient():
    # connect table
    conn = sqlite3.connect("test.db")
    curseur = conn.cursor()
    #create table
    curseur.execute("DROP TABLE IF EXISTS Client")
    curseur.execute("""create table Client (numClient varchar(10) PRIMARY KEY, nomClient varchar(30), prenomClient varchar(30), adrClient varchar(50), typeClient int(1))""")
    #insert lines
    curseur.execute("""insert into Client values ("ABC", "PEREIRA", "Alexandre", "4 Boulevard Koenings 31300 Toulouse", 0)""")
    conn.commit()
    conn.close()

initClient()
Client.loadAll();

print("Définition des Clients...")
Client("ABCD", "PENCHENAT", "Mathieu", "2 Impasse Louis Tharaud 31300 Toulouse", Type.ABONNE)
Client.saveAll()

for client in Client.tous:
    print(client)





# print("Définition des places de bases...", end="")
# placeType = [[1.2,2.3,1.5],[1.8,3.0,1.9],[3,5,2.6]] # hauteur, largeur, longueur de 3 types de places
# for i in range(0,20) :
#     choosenPlaceType = placeType[randint(0,2)];
#     Place(i, randint(1,2), choosenPlaceType[0], choosenPlaceType[1], choosenPlaceType[2])
# #Place.saveAll()
# print("OK\n")