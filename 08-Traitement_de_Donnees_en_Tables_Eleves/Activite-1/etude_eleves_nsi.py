import csv

''' Ouverture du fichier '''
file = open('data/eleves_1eres_NSI_2021-2022.csv')
fichier = csv.reader(file) # fichier est une liste des lignes


''' Declaration des variables '''
noms = []
prenoms = []
dict_NomsPrenoms = {}


''' On récupere pour chaques villes :
        - nom   
        - prenoms
'''
for ligne in fichier:
    noms.append(ligne[0]) # Rajoute le nom de la ville a la liste des villes
    prenoms.append(ligne[1]) # Rajoute la hauteur min de la ville a la liste des altitudes


''' On enleve le premier element de chaques lignes car il s'agit du header '''
del noms[0] 
del prenoms[0]

print("Noms :", noms) 
print("Prenoms :", prenoms)


''' Creation du dictionnaire Nom: Prénom '''
for nom, prenom in zip(noms, prenoms):
    dict_NomsPrenoms[nom] = prenom

print(dict_NomsPrenoms)