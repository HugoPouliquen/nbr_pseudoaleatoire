import random


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

dices_nbr = 5
values = drawing(dices_nbr)
res_sum = sum(values, dices_nbr)

print('Traitement pour '+ str(dices_nbr) +' dés')
# Le nombre maximum d'un dés multiplié par le nbr de dés moins 5
# car la plus petite combinaison c'est 5.
print('Nombre de sommes possibles : ' + str(6*dices_nbr - 5))
print('Nombre de combinaisons possibles : ' + str(6**dices_nbr))
print('\n-> Lancement des dés...\n')
print('Somme des dés lancés : ' + str(res_sum))
