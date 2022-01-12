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
    
grille = creeGrille(3,3)

print(afficheGrille(grille))