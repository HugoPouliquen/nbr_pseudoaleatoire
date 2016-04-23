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

dices_nbr = 6
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
                        for n in dices:
                            res = i + j + k + l + m + n
                            if res == sumvalue:
                                possibility += 1
    return str(possibility)

print('Traitement pour '+ str(dices_nbr) +' dés')
# Le nombre maximum d'un dés multiplié par le nbr de dés moins 5
# car la plus petite combinaison c'est 5.
print('Nombre de sommes possibles : ' + str(6*dices_nbr - 5))
print('Nombre de combinaisons possibles : ' + str(6**dices_nbr))
print('\n-> Lancement des dés...\n')
print('Somme des dés lancés : ' + str(res_sum))

print('Nombre de combinaisons possible pour :')
for i in range(5, (6*dices_nbr) +1):
    res = possibility(i)
    print(str(i) + ' : ' + res)
