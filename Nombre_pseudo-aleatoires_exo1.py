import random
import matplotlib.pyplot as plt

N = 10
nbr_loop = 10000
results = {}
sorties = []

# Boucle réalisant 100 000 tirage "aléatoire" entre 1 et 10
for i in range(nbr_loop):
    result = random.randrange(0, N + 1)
    sorties.append(result)

print("\nGraphique des résultats en fonction de leur nombre d'apparition")

# CREATION DU GRAPHIQUE
plt.title("Sortie en fonction de leur nombre d'apparition")
plt.hist(sorties, N)
plt.axis([0, N, 0, 0.20*nbr_loop])
plt.xlabel('Sorties')
plt.ylabel("Nombre d'apparitions")
plt.show()
