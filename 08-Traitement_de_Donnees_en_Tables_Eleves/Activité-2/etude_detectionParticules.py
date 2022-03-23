import csv
import random

''' Ouverture du fichier '''
file = open('data/detectionParticules.csv')
fichier = csv.reader(file) # fichier est une liste des lignes

''' Declaration des variables '''

# Yen a pas lol


''' On récupere pour chaques villes :
        - Rien
'''

# for ligne in fichier:
    # noms.append(ligne[0])


''' On enleve le premier element de chaques lignes car il s'agit du header '''
# del noms[0]
# del latitudes[0]
# del hebergements[0]
# print("Noms :", noms) 
# print("Latitudes :", latitudes) 
# print(("Hebergement :", hebergements))



def ligneSur10(fichier):
    """Give 1 row out of 10 in fichier

    Args:
        fichier (list or csv_reader): high number of row list or csv_reader

    Returns:
        List: List of 1 row out of 10 in fichier
    """
    i=1
    result = []
    for ligne in fichier:
        if i % 10==0:
            result += ligne
        i+=1
    return result


def createListeNombre():
    listeNombre = []
    for i in range(0, 100):
        listeNombre.append(random.randint(0, 501))
    return(listeNombre)

print(createListeNombre())