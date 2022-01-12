listeCapitales1=["Berlin","Vienne","Bruxelles","Sofia","Nicosie","Zagreb", "Copenhague","Madrid","Talinn","Helsinki","Paris","Athène","Budapest","Dublin","Rome"]
listeCapitales2=["Riga","Vilnius","Luxembourg","La Valette","Amsterdam","Varsovie","Lisbonne","Prague","Bucarest","Londres","Bratislava","Ljubljana","Stockholm"]

listePays1=["Allemagne","Autriche","Belgique","Bulgarie","Chypre","Croatie","Dannemark","Espagne","Estonie","Finfande","France","Grèce","Hongrie","Irlande","Italie"]
listePays2=["Lettonie","Lituanie","Luxembourg","Malte","Pays Bas","Pologne","Portugal","République-Tchèque","Roumanie","Royaume-Uni","Slovaquie","Slovénie","Suède"]

listePays, listeCapitales, capitalePays = listePays1 + listePays2, listeCapitales1 + listeCapitales2, []
for i in zip(listePays, listeCapitales):
    print(i[0], "a pour capitale", i[1])
    capitalePays.append(i)
print(capitalePays)


# Solution de Dictionnaires
dictio = dict(zip(listePays, listeCapitales))
# print (dictio)


