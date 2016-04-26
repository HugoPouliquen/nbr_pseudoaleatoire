import random
import matplotlib.pyplot as plt

i = z = 0
sorties = []
i = 1
nbr_loop = 100
for i in range(nbr_loop + 1): # entre 1 et 100
    z = round(3*random.random())
    sorties.append(z)
    print(z, end=' ')


plt.title("Sortie en fonction de leur nombre d'apparition")
plt.hist(sorties, nbr_loop)
plt.axis([0, 10, 0, 0.5*nbr_loop])
plt.xlabel('Sorties')
plt.ylabel("Nombre d'apparitions")
plt.show()

# Commentaires :
# Cela n'est pas non plus très aleatoires.. -> à creuser
