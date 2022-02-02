peoples = [{"nom": "Pasquier", "prenom": "Martin", "date_de_naissance": "31/03/2006"}, {"nom": "Sincock", "prenom": "Max", "date_de_naissance": "17/09/2005"}]
peoples[0]['lieu_de_naissance'], peoples[1]['lieu_de_naissance'] = "Cherbourg", "Cherbourg"

for sb in peoples:
    print(f"Je m'appelle {sb['prenom']} {sb['nom']} et je suis né le {sb['date_de_naissance']} à {sb['lieu_de_naissance']}.")

stock={"crayon":43,"stylobleu":23,"stylorouge":40, "stylovert":30, "gomme":12,"regle":25, "compas":10}
prix={'regle': 5, 'compas': 6, 'gomme': 1.2, 'crayon': 1.1, 'stylorouge': 3, 'stylobleu': 2.5, 'stylovert': 2.3}
commande1={"crayon": 3,"stylovert":23,"gomme":22,"regle":5}
commande2={"crayon": 3,"stylorouge":23,"gomme":22,"regle":5}

def nb_objet(commande: dict):
    result = 0
    for el in commande:
        result += commande[el]
    return result

def augmente(prix: dict, pourcentageAugmentation: float or int):
    for el in prix:
        prix[el] *= 1 + pourcentageAugmentation/100
    return prix

def facture(commande: dict, prix: dict):
    result = 0
    for el in commande:
        result += commande[el]*prix[el]
    return result

print(nb_objet(commande1))
print(augmente(prix, 10)) # REMPLACE LA VALEUR DE PRIX
print(facture(commande2, prix))
