import matplotlib.pyplot as plt
points = [[0.5, 1.5, "r"], [0.75, 1, "r"], [0.75, 1.75, "r"], [0.75, 2.25, "r"], [0.8, 1.4, "r"], [0.8, 2.75, "r"], [1, 1.6, "r"], [1, 2.25, "r"], [1.25, 1.25, "r"], [1.75, 1.25, "b"], [2, 1.25, "b"], [2, 1.5, "b"], [2.25, 1, "b"], [2.25, 1.25, "b"], [2, 1.75, "b"], [2.5, 0.5, "b"], [2.5, 1.5, "b"], [2.5, 2, "b"], [2.75, 1, "b"], [2.75, 1.75, "b"]]
point_vert = (1.5, 1.5, "g")
for u in points:
    plt.plot(u[0], u[1], u[2]+"s")
plt.plot(point_vert[0], point_vert[1], point_vert[2]+"o")
plt.plot([0, 5], [0, 10], color = 'red', linestyle = 'solid')
plt.title("K plus proches voisins")
plt.grid()
plt.xlabel('abscisses')
plt.ylabel('ordonnées')
plt.axis('equal')

plt.show()
plt.close()
