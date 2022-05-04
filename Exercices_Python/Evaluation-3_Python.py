# Exercice 1: Tuples

from distutils.sysconfig import PREFIX


def ordre():
    mots = ("rien", "Rien", "ne", "ne", "se", "se", "se", "perd", "crée", ",", ",", ".", "tout", "transforme")
    print(mots[1], mots[2], mots[4], mots[7] + mots[9], mots[0], mots[3], mots[5], mots[8] + mots[10], mots[12], mots[6], mots[13] + mots[11])
# ordre()


# Exercice 2: Pizzas

liste1= ['jambon', 'mozzarella', 'sauce_tomate', 'champignons', 'poivrons']
liste2= ['chèvre', 'lardons', 'crème_fraîche', 'mozzarella', 'tomates', 'sauce_tomate', 'oignons']

def nombreIngredients(liste: list):
    return liste.__len__()
# print(nombreIngredients(liste1))

def sommeIngredients(*listes: list):
    listeTotal = []
    for liste in listes:
        listeTotal += liste
    return listeTotal
# print(sommeIngredients(liste1, liste2))

def unionSansdoublon(*listes: list):
    listeTotal = []
    for liste in listes:
        for element in liste:
            if not element in listeTotal:
                listeTotal.append(element)
    return listeTotal
# print(unionSansdoublon(liste1, liste2))

# Exercice 3: Dictionnaires

dico1={"jambon": 2.2, "mozzarella": 1.6, "sauce_tomate": 1.5, "champignons": 1.7, "poivrons": 1.5, "chèvre": 1.6, "lardons": 2.0, "crème_fraîche": 1.6,  "tomates": 1.5,  "oignons": 1.5}
pizza1= ["jambon", "sauce_tomate", "lardons", "crème_fraîche", "oignons"]

def prix_pizza(dicoPrix: dict, pizza: list):
    prixTotal = 0
    for element in pizza:
        prixTotal += dicoPrix[element]
    return prixTotal
# print(prix_pizza(dico1, pizza1))

# Exercice 4: Grilles

grille1=[[1,2,3,0],[4,1,2,0],[3,3,1,0],[0,0,0,0]]

def sommeLigne(grille: list):
    somme = 0
    for ligne in grille:
        for element in ligne:
            somme += element
        ligne[-1] = somme
        somme = 0
    return grille

def sommeColonne(grille: list):
    somme = 0
    for colone in range(grille[0].__len__()):
        for ligne in grille:
            somme += ligne[colone]
        grille[-1][colone] = somme
        somme = 0
    return grille

print(sommeColonne(grille1))