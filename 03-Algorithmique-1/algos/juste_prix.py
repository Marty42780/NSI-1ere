# ---------------------------------------------------------------------------- #
#                                03-ALGOMITMIQUE                               #
#                               -----------------                              #
#                           Etape 2 de l'acivité 1 :                           #
#                                  Juste Prix                                  #
# ---------------------------------------------------------------------------- #

import random

nb = random.randint(0,100)
prop = -1
essais_restants = 2
essais_joueur = 0

print (nb)
while nb != prop and essais_restants > 0:
    essais_restants -= 1
    essais_joueur +=1
    prop = int(input("Donnez un nombre : "))
    if essais_restants != 0:
        if prop > nb:
            print ("Plus petit")
        if prop < nb:
            print ("Plus grand")

if nb == prop:
    print("Vous avez trouvé le nombre en", str(essais_joueur), "essais")
elif essais_restants < 1:
    print("Vous avez perdu")

