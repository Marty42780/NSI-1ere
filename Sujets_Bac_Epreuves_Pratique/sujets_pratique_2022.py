'''--------------------------------------------------------------------------- #
#                                     Sujet 1                                  #
# -------------------------------------------------------------------------- '''

''' Exercice 1 '''

from ast import Index


def recherche(caractere: str, mot: str):
    result = 0
    for element in mot:
        if element == caractere:
            result += 1
    return result

# print(recherche("i", "mississippi"))


'''--------------------------------------------------------------------------- #
#                                     Sujet 2                                  #
# -------------------------------------------------------------------------- '''

''' Exercice 1 '''

def moyenne(listeNotes: list): # Take list of tuples
    total, nb = 0, 0
    for note in listeNotes:
        total += note[0]*note[1]
        nb += note[1]
    return total / nb

# print(moyenne([(15,2),(9,1),(12,3)]))


'''--------------------------------------------------------------------------- #
#                                     Sujet 4                                  #
# -------------------------------------------------------------------------- '''

''' Exercice 1 '''

def recherche(liste: list):
    result = []
    for el in range(len(liste)-1):
        if liste[el]+1 == liste[el+1]:
            result.append((liste[el], liste[el+1]))
    return result

# print(recherche([7, 1, 2, 5, 3, 4]))


'''--------------------------------------------------------------------------- #
#                                     Sujet 5                                  #
# -------------------------------------------------------------------------- '''

''' Exercice 1 '''

def RechercheMinMax(liste: list):
    try :
        maxi, mini = liste[0], liste[0]
    except IndexError:
        maxi, mini = None, None
    for el in liste:
        if el < mini:
            mini = el
        if el > maxi:
            maxi = el
    return mini, maxi

# print(RechercheMinMax([0, 1, 4, 2, -2, 9, 3, 1, 7, 1]))


'''--------------------------------------------------------------------------- #
#                                     Sujet 6                                  #
# -------------------------------------------------------------------------- '''

''' Exercice 1 '''

def maxi(liste: list) -> tuple:
    try :
        maxi = liste[0]
    except IndexError:
        maxi = None
    for el in liste:
        if el > maxi:
            maxi = el
    return maxi, liste.index(maxi)

# print(maxi([1,5,6,9,1,2,3,7,9,8]))


'''--------------------------------------------------------------------------- #
#                                     Sujet 8                                  #
# -------------------------------------------------------------------------- '''

''' Exercice 1 '''

def recherche_2(elt: int, tab: list) -> int:
    for el in tab:
        if el == elt:
            return tab.index(elt)
    return -1

# print(recherche_2(1, [10, 12, 1, 56]))

''' Exercice 2 '''

def insere(a, tab):
    l = list(tab) # l contient les mêmes éléments que tab
    l.append(a)
    i = len(l)-2
    while a < l[i] and i >= 0:
        l[i+1] = l[i]
        l[i] = a
        i = i-1
    return l

# print(insere(3,[1,2,4,5]))


'''--------------------------------------------------------------------------- #
#                                     Sujet 10                                  #
# -------------------------------------------------------------------------- '''

''' Exercice 1 '''

def occurence_lettres(phrase: str) -> dict:
    result = {}
    for el in phrase:
        if el in result:
            result[el] += 1
        else:
            result[el] = 1
    return result

# print(occurence_lettres('Hello world !'))

''' Exercice 2 '''

def fusion(L1,L2):
    n1 = len(L1)
    n2 = len(L2)
    L12 = [0]*(n1+n2)
    i1 = 0
    i2 = 0
    i = 0
    while i1 < n1 and ... :
        if L1[i1] < L2[i2]:
            L12[i] = ...
            i1 = ...
        else:
            L12[i] = L2[i2]
            i2 = ...
            i += 1
    while i1 < n1:
        L12[i] = ...
        i1 = i1 + 1
        i = ...
    while i2 < n2:
        L12[i] = ...
        i2 = i2 + 1
        i = ...
    return L12

print(fusion([1,6,10],[0,7,8,9]))