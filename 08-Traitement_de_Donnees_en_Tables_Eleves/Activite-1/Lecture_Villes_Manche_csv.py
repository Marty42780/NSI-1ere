import csv
file = open('Villes_Manche_csv.csv')
reader = csv.reader(file)
for row in reader:
    print(row)

