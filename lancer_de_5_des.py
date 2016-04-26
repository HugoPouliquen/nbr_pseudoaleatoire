#!/usr/bin/python3
from random import randrange
import matplotlib.pyplot as plt

# Usage : La fonction roll_dice permet de lancer un nombre de dés
# Param : nbr est le nombre de dés a lancer
# Retour : La fonction retourne un tableau avec la valeur des dés lancés
def roll_dice(nbr):
    throw_value = []
    for i in range(nbr):
        throw_value.append(randrange(1, 7))
    return throw_value

# Usage : La fonction dice_sum effectue la somme du resultat de chaque dés
# Param : - values
#         - nbr est le nombre de dés lancé
# Retour : La fonction retourne la somme total des dés
def dice_sum(nbr, values):
    score = 0
    for i in range(nbr):
        score = score + values[i]
    return str(score)

# Usage : La fonction possibilities calcul le nombre de possibilités pour une
#         somme de dés donnée apparaisse
# Param : - la somme a traiter
# Retour : La fonction retourne le nombre de possibilités de combinaison de dés
# pour cette somme
def possibilities(sum_values):
    possibility = 0
    dices = [1, 2, 3, 4, 5, 6]
    for i in dices:
        for j in dices:
            for k in dices:
                for l in dices:
                    for m in dices:
                            res = i + j + k + l + m
                            if res == sum_values:
                                possibility += 1
    return possibility

# Usage : La fonction possible_sum calcul le nombre de somme possible
# Param : - Le nombre de dés à traiter
# Retour : La fonction retourne le nombre de somme possible lors du lancement
#          de ce nombre de dés (ici 5 dés)
def possible_sum(dices_nbr):
    return str((6*dices_nbr)  - 5)

# Usage : La fonction possible_combinations calcul le nombre decombinaison pour
#         chaque somme possible
# Param : - Le nombre de dés à traiter
#         - Les valeurs des dés lancés
# Retour : La fonction retourne le nombre de combinaisons possible
def possible_combinations(dices_nbr):
    values = []
    outputs = []
    j = dices_nbr
    for i in range(dices_nbr, (6*dices_nbr) + 1):
        values.append(possibilities(i))

    for i in values:
        print(str(j) + ' : ' + str(i))
        j += 1
        outputs.append(j)
    return outputs, values

# Usage : La fonction frequencies calcul la fréquence de chaque sortie
# Param : - Le nombre de dés à traiter
#         - Les valeurs des dés lancés
# Retour : La fonction retourne les fréquences de chaque sortie
def frequencies(dices_nbr, values):
    freqs = []
    k = dices_nbr
    for i in range(len(values)):
        frequencesres = 100*(values[i] / (6**dices_nbr))
        freqs.append(frequencesres)
        print(str(k) + ' : ' + str(frequencesres))
        k += 1
    return freqs

dices_nbr = 5 # Nombre de dés

print('\nTraitement pour : ' + str(dices_nbr) + ' dés comportant 6 faces de 1 à 6')
print('Nombre de sommes possibles : ' + possible_sum(dices_nbr))
print('\n-> Lancement des dés...')
print('Somme des dés lancés : ' + dice_sum(dices_nbr, roll_dice(dices_nbr)))
print('\nTableau du nombre de combinaisons possibles pour chaque somme :')
outputs, values = possible_combinations(dices_nbr)
print('\nTableau des fréquences de chaque somme :')
freqs = frequencies(dices_nbr, values)

# CREATION DU GRAPHIQUE
plt.title("Fréquence d'apparition")
plt.plot(outputs, freqs)
plt.xlabel('Sorties possibles')
plt.ylabel('Fréquence (%)')
plt.show()
