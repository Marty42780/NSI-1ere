# La fonction affiche une liste l1 de 50 multiples de 5 aléatoires inferieurs à 1000 puis retourne une deuxième liste qui récupère dans la première liste tout les mutliples de 3.

import random

def random_list():
    L1, L2, nb = [] , [], 1
    for i in range(50):
        while nb % 5 != 0:
            nb = random.randint(0, 1000)
        L1.append(nb)
        nb = 1
    print(L1)
    for i in L1:
        if i % 3 == 0:
            L2.append(i)
    return L2