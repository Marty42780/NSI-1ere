import csv

''' Ouverture du fichier '''
file = open('data/lycees25_manche.csv')
fichier = csv.reader(file) # fichier est une liste des lignes


''' Declaration des variables '''
noms = []
latitudes = []
hebergements = []
DictLyceeLatitudes = {}
DictLyceeHebergements = {}

''' On récupere pour chaques villes :
        - Nom
        - Latitude (POINT_Y)
'''
for ligne in fichier:
    noms.append(ligne[0])
    latitudes.append(ligne[15])
    hebergements.append(ligne[11])


''' On enleve le premier element de chaques lignes car il s'agit du header '''
del noms[0] 
del latitudes[0]
del hebergements[0]
print("Noms :", noms) 
print("Latitudes :", latitudes) 
print(("Hebergement :", hebergements))


''' On récupère dans un dictionnaire la latitude pour chaque lycee ''' 
for nom, latitude in zip(noms, latitudes):
    DictLyceeLatitudes[nom] = latitude
print(DictLyceeLatitudes)

''' On récupère dans un dictionnaire l'hébergement pour chaque lycée '''
for nom, hebergement in zip(noms, hebergements):
    DictLyceeHebergements[nom] = hebergement
print(DictLyceeHebergements)
    

def mini(DictLyceeLatitudes):
    """Give the high school with the lowest latitude

    Args:
        DictLyceeAltitudeMin (Dictionary): All cities with their latitude

    Returns:
        Tuple: Name of the city and its latitude
    """
    Lycee=""
    Nmin=10000000
    for x in DictLyceeLatitudes:
        if float(DictLyceeLatitudes[x])<Nmin:
            Nmin=float(DictLyceeLatitudes[x])
            Lycee=x
    return Lycee, Nmin
print(mini(DictLyceeLatitudes))

def nbInternat(DictLyceeHebergements):
    """Give number of high schools with boarding school

    Args:
        DictLyceeHebergements (Dictionary): All cities with their 'hébergement'

    Returns:
        Integer: number of high schools with boarding school
    """
    Lycee=""
    nbInternat = 0
    for x in DictLyceeHebergements:
        if str(DictLyceeHebergements[x])=='avec internat et demi-pension':
            nbInternat += 1
    return nbInternat

print(nbInternat(DictLyceeHebergements))

# TODO : Finir l'activité 1 ici