import random
import matplotlib.pyplot as plt

N = 10
nbr_loop = 10000
results = {}
sorties = []
for i in range(nbr_loop):
    result = random.randrange(0, N + 1)
    sorties.append(result)  # + 1 pour etre entre 1 et 1000 inclus
    # if result in results:
    #     counter = results[result]
    #     counter += 1
    #     results[result] = counter
    # else:
    #     results[result] = 1

print("\nGraphique des resultats en fonction de leur nombre d'apparition")


# nbr_apparition = []
# for item in results:
#     sorties.append(item)
#     nbr_apparition.append(results[item])

plt.title("Sortie en fonction de leur nombre d'apparition")
plt.hist(sorties, N)
plt.axis([0, N, 0, 0.20*nbr_loop])
plt.xlabel('Sorties')
plt.ylabel("Nombre d'apparitions")
plt.show()
