# ---------------------------------------------------------------------------- #
#                                  Exercice 1                                  #
# ---------------------------------------------------------------------------- #
'''
Écrire un petit programme qui affichera ce « dialogue »
- "Bonjour"
- "Quel est votre prénom ?" --> "Françoise"
- "Comment allez-vous françoise ?"
- "On va faire un calcul"
- "Entrez un nombre :" --> "6"
- "Entrez un autre nombre :" --> "7"
- "La somme de 6 et 7 est égale à 13"
'''

def dialogue():
    print('Bonjour !')
    nom = input('Quelle est votre nom ? : ')
    print('Comment allez vous ', nom, '?')
    print('On va faire un calcul')
    nb1 = float(input('Entrez un nombre : '))
    nb2 = float(input('Enrtez un autre nombre : '))
    somme = nb1 + nb2
    print("L'addition de", nb1, "et", nb2, "est égale à ", somme)

# dialogue()

# ---------------------------------------------------------------------------- #
#                                  Exercice 2                                  #
# ---------------------------------------------------------------------------- #

'''  Pythagore 
Le but est de créer un programme qui affiche si un triangle est rectangle ou non après avoir rentré la longueur de ses trois côtés.
1. Écrire la fonction maxi(a,b,c) qui renvoie le plus grand de 3 nombres.
2. Écrire la fonction mini(a,b,c) qui renvoie le plus petit de 3 nombres.
3. Écrire la fonction moyen(a,b,c) qui renvoie le nombre médian parmi 3 nombres.
4. Écrire la fonction pythagore() qui demande à l’utilisateur de rentrer les longueurs des trois côtés d’un triangle et qui affiche si le triangle est rectangle ou pas.
'''

def pythagore(a, b, c):
    if max(a,b,c) == a: # maxi = a
        print(a)
        if (a**2 == b**2 + c**2):
            print ("Ce triangle est rectangle")
        else:
            print ("Ce triangle n'est pas rectangle")

    if max(a,b,c) == b: # maxi = b
        # print(b)
        if (b**2 == a**2 + c**2):
            print ("Ce triangle est rectangle")
        else:
            print ("Ce triangle n'est pas rectangle")

    if max(a,b,c) == c: # maxi = c
        print(c)
        if (c**2 == a**2 + b**2):
            print ("Ce triangle est rectangle")
        else:
            print ("Ce triangle n'est pas rectangle")

# pythagore(3,4,5)

# ---------------------------------------------------------------------------- #
#                                 Exercice n°3                                 #
# ---------------------------------------------------------------------------- #

def moyenne(*values):
    total = 0
    print(values)
    for i in values:
        total += i
    return total/len(values)

# print(moyenne(20,18,20,15,16,18,17,15))

# ---------------------------------------------------------------------------- #
#                                 Exercice n°4                                 #
# ---------------------------------------------------------------------------- #

def somme_cube(*values):
    total = 0
    for i in values:
        total += i**3
    return total

# print(somme_cube(4))

# ---------------------------------------------------------------------------- #
#                                 Exercice n°5                                 #
# ---------------------------------------------------------------------------- #

from random import randint

def alea(n):
    return randint(1, n)

def calcul(n):
    rep = 0
    a, b = alea(n), alea(n)
    rep = input('Entrez le résultat de ' + str(a) + ' et de ' + str(b) + ' : ')
    if int(rep) == a+b:
        print('Bravo')
        return 1
    elif int(rep) != a+b:
        print('Perdu, il fallait trouver', str(a+b))
        return 0

def serie_calcul(n, nb):
    score = 0
    print('La valeur maximale des nombre est', str(n))
    print('Nombre de calcul : ', str(nb))
    for i in range(nb):
        if calcul(n) == 1:
            score += 1
    print('Score total pour les', str(nb), 'calculs : ', str(score))

# serie_calcul(10, 5)

# ---------------------------------------------------------------------------- #
#                                 Exercice n°6                                 #
# ---------------------------------------------------------------------------- #

from random import randint

def generer_nombre(n):
    return randint(0, n)

def demande_coup():
    return int(input("Donnez un nombre : "))

def compare_nombre(nb, prop):
    if nb == prop:
        return 0
    elif nb < prop:
        return 1
    elif nb > prop:
        return -1


def partie(essais_restants, n):
    nb = generer_nombre(n)
    essais_joueur = 0
    prop = -1
    print (nb)
    while compare_nombre(nb, prop) != 0 and essais_restants > 0:
        essais_restants -= 1
        essais_joueur +=1
        prop = demande_coup()
        if essais_restants != 0:
            if compare_nombre(nb, prop) == 1:
                print ("Plus petit")
            if compare_nombre(nb, prop) == -1:
                print ("Plus grand")

    if compare_nombre(nb, prop) == 0:
        print("Vous avez trouvé le nombre en", str(essais_joueur), "essais")
    elif essais_restants < 1:
        print("Vous avez perdu")

# partie(5, 10)



# ---------------------------------------------------------------------------- #
#                                 Exercice n°7                                 #
# ---------------------------------------------------------------------------- #

def affiche(n):     # Fonction qui affiche 'n' fois '*'
    print('* '*n)

def saisie(a, b):   # Demande d'entrer un nombre entre 'a' et 'b'
    try:
        prop = int(input('Entrez un nombre entre ' + str(a) + ' et ' + str(b) + ' : '))
    except ValueError:
        pass
    while prop < a or prop > b:
        try:
            prop = int(input('Entrez un nombre entre ' + str(a) + ' et ' + str(b) + ' : '))
        except ValueError:
            pass
    return(prop)

def jeuAllumette(nbAllumette):
    winState = 0
    while winState == 0:
        affiche(nbAllumette)
        print('Joueur 1, il reste', nbAllumette, end=' ')

        if nbAllumette > 3:
            prop1 = saisie(1, 3)
        elif nbAllumette <= 3:
            prop1 = saisie(1, nbAllumette)
        
        if prop1 == nbAllumette:
            winState = 1
        else:
            nbAllumette -= prop1
            affiche(nbAllumette)
            print('Joueur 2, il reste', nbAllumette, end=' ')

            if nbAllumette > 3:
                prop2 = saisie(1, 3)
            elif nbAllumette < 3:
                prop2 = saisie(1, nbAllumette)

            if prop2 == nbAllumette:
                winState = 2
            else:
                nbAllumette -= prop2

    if winState == 1:
        print('Le joueur 1 a gagné')
    elif winState == 2:
        print('Le joueur 2 a gagné')

jeuAllumette(21)



