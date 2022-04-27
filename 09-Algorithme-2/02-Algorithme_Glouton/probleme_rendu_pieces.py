pieces = [500, 200, 100, 50, 20, 10, 5, 2, 1]
choix = [0, 0, 0, 0, 0, 0, 0, 0, 0]
quantite = [0, 0, 0, 0, 0, 0, 0, 0, 0]
somme = 210 
i = 0
n = 0

n = len(pieces)

for i in range(1, n):
    while somme >= pieces[i]:
        somme -= pieces[i]
        quantite[i] += 1
        choix[i] = pieces[i]
        
# print(choix)
# print(quantite)

choix_quantite = {4: 0, 3: 0, 1: 0}
choix_quantite = dict(sorted(choix_quantite.items(), reverse=True)) # Marche que sur dernières versions de Python

somme = 6
i = 0

for i in choix_quantite:
    while i <= somme:
        somme -= i
        choix_quantite[i] += 1

print(choix_quantite)
