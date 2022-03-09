import csv

file = open('villes_manche.csv')
reader = csv.reader(file)
for row in reader:
    print(row)

