notes = [(15,2), (20,1), (17,3)]
numerateur, denomirateur = 0, 0
for note in notes:
    numerateur += note[0]*note[1]
    denomirateur += note[1]
    
moyenne = numerateur / denomirateur