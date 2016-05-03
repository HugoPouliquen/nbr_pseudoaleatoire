#!/usr/bin/python3
import random
import matplotlib.pyplot as plt

z = 0
i = 1
sorties = []
nbr_loop = 100
for i in range(nbr_loop + 1): # entre 1 et 100
    z = round(3*random.random())
    print(z, end=' ')
    sorties.append(z)

plt.title("Sortie en fonction de leur nombre d'apparition")
plt.hist(sorties, nbr_loop)
plt.axis([0, 5, 0, 0.5*nbr_loop])
plt.xlabel('Sorties')
plt.ylabel("Nombre d'apparitions")
plt.show()
