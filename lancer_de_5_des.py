import random
import matplotlib.pyplot as plt

dices_nbr = 5

def drawing(nbr):
    drawing = []
    for i in range(nbr):
        drawing.append(random.randrange(1, 7))
    return drawing

def sum(values, dices_nbr):
    score = 0
    for i in range(dices_nbr):
        score = score + values[i]
    return score

nbr_sum = 6*dices_nbr
values = drawing(dices_nbr)
res_sum = sum(values, dices_nbr)

def possibility(sumvalue):
    possibility = 0
    dices = [1, 2, 3, 4, 5, 6]
    for i in dices:
        for j in dices:
            for k in dices:
                for l in dices:
                    for m in dices:
                            res = i + j + k + l + m
                            if res == sumvalue:
                                possibility += 1
    return possibility

print('Traitement pour '+ str(dices_nbr) +' dés')
# Le nombre maximum d'un dés multiplié par le nbr de dés moins 5
# car la plus petite combinaison c'est 5.
print('Nombre de sommes possibles : ' + str(nbr_sum - 5))
print('Nombre de combinaisons possibles : ' + str(6**dices_nbr))
print('\n-> Lancement des dés...\n')
print('Somme des dés lancés : ' + str(res_sum))

print('\nTableau du nombre de combinaison possible pour chaque somme :')
values = []
sorties = []
j = k = dices_nbr
for i in range(dices_nbr, (nbr_sum) + 1):
    values.append(possibility(i))

for i in values:
    print(str(j) + ' : ' + str(i))
    j += 1
    sorties.append(j)
print('\nTableau des fréquences :\n')
frequences = []
for i in range(len(values)):
    frequencesres = 100*(values[i] / (6**dices_nbr))
    frequences.append(frequencesres)
    print(str(k) + ' : ' + str(frequencesres))
    k += 1

print('\nGraphique des fréquences')

plt.title("Fréquence d'apparition")

plt.plot(sorties, frequences)
plt.xlabel('Sorties possibles')
plt.ylabel('Fréquence (%)')
plt.show()
