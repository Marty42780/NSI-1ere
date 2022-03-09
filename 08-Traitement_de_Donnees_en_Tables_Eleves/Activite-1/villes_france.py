import csv

ligne0 = ['Département', 'Slug', 'Nom', 'Nom simple', 'Nom reel', 'Nom soundex', 'Nom metaphone', 'Code postal', 'Numéro de commune', 'Code commune (ou code INSEE)', 'Arrondissement', 'Canton', 'Population en 2010', 'Population en 1999', 'Population en 2012 (approximatif)', 'Densité en 2010', 'Surface / superficie', 'Longitude en degré', 'Latitude en degré', 'Longitude en DMS', 'Latitude en DMS', 'Longitude en DMS', 'Latitude en DMS', 'Altitude minimale', 'Altitude maximale']

# Open Files
file = open('villes_france.csv', 'r')
newfile = open('villes_france2.csv', 'w')
reader = csv.reader(file)
writer = csv.DictWriter(newfile, fieldnames=ligne0)

writer.writeheader()

for row in reader:
    writer.writerow(row)

