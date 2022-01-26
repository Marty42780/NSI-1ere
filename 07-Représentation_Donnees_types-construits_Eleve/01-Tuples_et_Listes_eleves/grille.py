listGrille = []

def creeGrille(l: int, c: int):
    grille = [[0]*c]*l
    return grille

def afficheGrille(grille: list):
    result = ""
    for i in grille:
        for k in i:
            result += str(k) + " "
        result += "\n"
    return(result)
    
def sommeLigne(grille: list, lig: int):
    result = 0
    for el in grille[lig]:
        result += el
    return result

def sommeColone(grille: list, col: int):
    result = 0
    for ligne in grille:
        result += ligne[col]
    return result

def sommeDiagonale(grille: list):
    i = 0
    result = 0
    try:
        for ligne in grille:
            result += ligne[i]
            i += 1
    except IndexError:
        print("La grille n'est pas carré")
    return result

grille0 = creeGrille(3,3)
grille1 = [[1,2,3],[4,5,6],[7,8,9],[10,11,12]]
print("sommeLigne " + str(sommeLigne(grille1, 0)))
print("sommeColone " + str(sommeColone(grille1, 0)))
print("sommeDiagonale " + str(sommeDiagonale(grille1)))

