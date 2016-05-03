#!/usr/bin/python3
import matplotlib.pyplot as plt
import math 

def VonNeumann(N, A, display):
        if not N:
	    # Calcul de la longueur du nombre
            N = len(str(A))
        square = A * A
	# Calcul de la longueur du carre du nombre
        square_len = len(str(square))
        part = square_len * 0.25
        square = str(square)
	# On sauvegarde la tranche du milieu du carre
        middle_slice = square[int(part):int(part+N)]
	# On divise cette tranche par 10^N
        res = float(middle_slice) / float(10**N)

        if(display == 1):
            print(  "----\nA : " + str(A)+ "\nN : " + \
                    str(N) + "\nCarre de A : " + \
                    str(square) + "\nTranche: " + \
                    str(middle_slice) + "Resultat : " + \
                    str(res)
            )
        return res

VonNeumann(4, 5678, 1)
VonNeumann(6, 123456, 1)

outputs = []
loop_nbrs = 100
N = 10
for i in range(loop_nbrs):
    outputs.append(math.trunc(VonNeumann(None, i, 0)*N+1))

plt.title("Sortie en fonction de leur nombre d'apparition")
plt.hist(outputs, loop_nbrs)
plt.axis([0, N , 0, 0.2*loop_nbrs])
plt.xlabel('Sorties')
plt.ylabel("Nombre d'apparitions")
plt.show()
