import csv

''' Ouverture du fichier '''
file = open('data/echantillon_villes_manche.csv') #permet d'ouvrir le ficher en vert
fichier = csv.reader(file) # fichier est une liste des lignes

''' Declaration des variables '''
listeVille = []
altitudeVilleMax = []
altitudeVilleMin = []

''' On récupere pour chaques villes :
        - nom   
        - altitude minimum
        - altitude maximum
'''
for ligne in fichier:
    listeVille.append(ligne[1]) # Rajoute le nom de la ville a la liste des villes
    altitudeVilleMin.append(ligne[12]) # Rajoute la hauteur min de la ville a la liste des altitudes
    altitudeVilleMax.append(ligne[13]) # Rajoute la hauteur max de la ville a la liste des altitudes

''' On enleve le premier element de chaques lignes car il s'agit du header '''
del listeVille[0] 
del altitudeVilleMax[0]
del altitudeVilleMin[0]


print("listeVille :", listeVille) 
print("altitudeVilleMax :", altitudeVilleMax)
print("altitudeVilleMin :", altitudeVilleMin)

DictVilleAltitudeMax={}
for i in range(len(listeVille)):
    DictVilleAltitudeMax[listeVille[i]]=altitudeVilleMax[i]
print(DictVilleAltitudeMax)

DictVilleAltitudeMin={}
for i in range(len(listeVille)):
    DictVilleAltitudeMin[listeVille[i]]=altitudeVilleMin[i]
print(DictVilleAltitudeMin)

def maxi(DictVilleAltitudeMax):
    """Give the city with the highest altitude

    Args:
        DictVilleAltitudeMax (Dictionnary): All cities with their highest altitudes without headers

    Returns:
        Tuple: Name of the city and its altitude
    """    
    Ville=""
    Nmax=0
    for x in DictVilleAltitudeMax:
        if float(DictVilleAltitudeMax[x])>Nmax:
            Nmax=float(DictVilleAltitudeMax[x])
            Ville=x
    return (Ville, Nmax)



def mini(DictVilleAltitudeMin):
    """Give the city with the lowest altitude

    Args:
        DictVilleAltitudeMin (Dictionary): All cities with their lowest altitudes without headers

    Returns:
        Tuple: Name of the city and its altitude
    """
    Villemin=""
    Nmin=maxi(DictVilleAltitudeMin)[1]
    for x in DictVilleAltitudeMin:
        if float(DictVilleAltitudeMin[x])<Nmin:
            Nmin=float(DictVilleAltitudeMin[x])
            Villemin=x
    return Villemin, Nmin