import csv
import random

''' Ouverture du fichier '''
file = open('data/detectionParticules.csv')
fichier = csv.reader(file) # fichier est une liste des lignes

''' Declaration des variables '''
liste1 = [26, 36, 42, 44, 46, 50]
liste2 = [5, 14, 22, 29, 38, 40, 47]
tableau1 = [3*[0] for i in range (3)]

def ligneSur10(fichier):
    """Give 1 row out of 10 in fichier """
    i=1
    result = []
    for ligne in fichier:
        if i % 10==0:
            result += ligne
        i+=1
    return result


def createListeNombre():
    """ Create list of random numbers between 0 and 500 """
    listeNombre = []
    for i in range(0, 100):
        listeNombre.append(random.randint(0, 500))
    return(listeNombre)

# print(createListeNombre())

def listePaire(liste: list):
    """ Return the list of even numbers in list and sort it """
    listePaire = []
    for i in liste:
        if i % 2 == 0:
            listePaire.append(i)
    listePaire.sort()
    return(listePaire)

def listeImpaire(liste: list):
    """ Return the list of odd numbers in list and sort it in reverse order """ 
    listeImpaire = []
    for i in liste:
        if i % 2 != 0:
            listeImpaire.append(i)
    listeImpaire.sort(reverse=True)
    return(listeImpaire)

def fusion(*listes: list):
    """ Fusion of *listes in one list and sort it """
    result = []
    for liste in listes:
        result += liste
    result.sort()
    return(result)

def mystere(liste1: list, liste2: list):
    """ Fonction Mystere ??? """
    liste = []
    j, k = 0, 0
    while j < len(liste1) and k < len(liste2):
        if liste1[j] < liste2[k]:
            liste.append(liste1[j])
            j += 1
        else:
            liste.append(liste2[k])
            k += 1
    return liste

def qcm(tableau: list):
    """ Give the result of the QCM in tableau (list) and return the tableau """
    for j in range(3):
        tableau[j][j] = j + 1
        tableau[0][j] = tableau[0][j] + j + 1
        tableau[j][2] = tableau[j][2] + j + 1
    return tableau
