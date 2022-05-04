grille1=[[1,5,3,0],[4,1,2,0],[3,3,1,0],[0,0,0,0]]

def sommeLigne(grille: list):
    for ligne in grille:
        for el in ligne[:-1]:
            ligne[3] += el
    return grille

def sommeColone(grille: list):
    for colone in range(len(grille[0])):
        for ligne in grille[:-1]:
            grille[-1][colone] += ligne[colone]
    return grille

def sommeDiagonale(grille: list):
    total, i = 0, 0
    for ligne in grille:
        print('i: ', i)
        print('ligne', ligne[i])
        total += ligne[i]
        i += 1
    return total

print(sommeDiagonale(grille1))