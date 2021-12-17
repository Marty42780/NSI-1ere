# ---------------------------------------------------------------------------- #
#                                03-ALGOMITMIQUE                               #
#                               -----------------                              #
#                           Etape 2 de l'acivité 1 :                           #
#                              Année bissextile ?                              #
# ---------------------------------------------------------------------------- #

# Il faut que ce soit divisible par 4 mais pas par 100 sauf par 400

annee = int(input("Entrez une année : "))

if annee%4==0 and (annee%100!=0 or annee%400==0):
    print("L'année est bissextile")
else:
    print("L'année n'est pas bissextile")