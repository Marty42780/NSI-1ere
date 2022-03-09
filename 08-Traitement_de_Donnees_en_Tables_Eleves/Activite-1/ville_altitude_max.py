import csv
file = open('echantillon_villes_manche.csv')

fichier = csv.reader(file)
listeVille = []
altitudeVille = []
for ligne in fichier:
    Ville = (ligne[1])
    listeVille.append(Ville)
    Altitude = (ligne[13])
    altitudeVille.append(Altitude)
print(listeVille)
del listeVille[0]
print(listeVille)
print(altitudeVille)
del altitudeVille[0]
print(altitudeVille)


VilleAltitude={}
for i in range(len(listeVille)):
    VilleAltitude[listeVille[i]]=altitudeVille[i]
print(VilleAltitude)


def maxi(VilleAltitude):
    Ville=""
    Nmax=0
    for x in VilleAltitude:
        if float(VilleAltitude[x])>Nmax:
            Nmax=float(VilleAltitude[x])
            Ville=x
    return Ville, Nmax

