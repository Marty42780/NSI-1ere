# ---------------------------------------------------------------------------- #
#                                03-ALGOMITMIQUE                               #
#                               -----------------                              #
#                           Etape 1 de l'acivité 1 :                           #
#                          Test de triangle rectangle                          #
# ---------------------------------------------------------------------------- #

# ---------------------------- Méthode 1 : Facile ---------------------------- #

def meth1():
    a = int(input("Donnez 'a' : "))
    b = int(input("Donnez 'b' : "))
    c = int(input("Donnez 'c' : "))
    if a > b and a > c: # maxi
        maxi = a ; more1 = b ; more2 = c
    if b > a and b > c: # maxi
        maxi = b ; more1 = a ; more2 = c
    if c > a and c > b: # maxi
        maxi = c ; more1 = a ; more2 = b
    if (maxi**2 == more1**2 + more2**2):
        print ("Ce triangle est rectangle")
    else:
        print ("Ce triangle n'est pas rectangle")


# --------------------------- Méthode 2 : Compliqué -------------------------- #

def meth2():
    a = int(input("Donnez 'a' : "))
    b = int(input("Donnez 'b' : "))
    c = int(input("Donnez 'c' : "))
    if a > b and a > c: # maxi
        if (a**2 == b**2 + c**2):
            print ("Ce triangle est rectangle")
        else:
            print ("Ce triangle n'est pas rectangle")
    if b > a and b > c: # maxi
        if (b**2 == a**2 + c**2):
            print ("Ce triangle est rectangle")
        else:
            print ("Ce triangle n'est pas rectangle")
    if c > a and c > b: # maxi
        if (c**2 == a**2 + b**2):
            print ("Ce triangle est rectangle")
        else:
            print ("Ce triangle n'est pas rectangle")
