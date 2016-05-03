#!/usr/bin/python3

# Usage : La fonction congru generator permet de generer des congruences lineaire
# Param : les parametres sont ceux donnes par l'exercice pour le calcul des congruences.
# Sortie: La sortie est une suite de nombres aleatoires avec la periode
def Congru_generator(b, X, a, N, display = 1):
    first = True
    p = 0
    n_res = []
    Xn_res = []
    print('\n-- b = ' + str(b) +', X0 = ' + str(X) + ', a = ' + str(a) \
        + ', N = ' + str(N) + '--')

    X = first_element = X
    Xn_res.append(first_element)  # Traitement de X0
    n_res.append(0)
    X = ((a*X)+b) % N
    Xn_res.append(X)  # Traitement de X1
    n_res.append(1)
    for j in range(2, N + 1): # Boucle pour generer chaque nombre
        X = ((a*X)+b) % N
        if(X == first_element and first is True): # Recherche de la periode
            p = j
            first = False
        n_res.append(j)
        Xn_res.append(X)
    if(display != 0): # Option pour ne pas afficher des logs en permanence
        print('n  =', end=" ")
        for k in n_res: # Affichage du resultat en ligne
            print (str(k), end=" ")
        print('\nXn =', end=" ")
        for l in Xn_res:
            print (str(l), end=" ")
    else:
        print('La suite est trop importante pour etre affichee dans la console')
    print('\nLa periode est de : ' + str(p))

Congru_generator(3, 7, 5, 16)
Congru_generator(6, 7, 5, 16)
Congru_generator(0, 1, 2, 17)
Congru_generator(6, 1, 2, 17)
Congru_generator(0, 3, 13, 2**7, 0)
Congru_generator(0, 4567, 9749, 2**17, 0)
