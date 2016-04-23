#!/usr/bin/python3
import matplotlib.pyplot as plt
def VonNeumann(A):
	# Calcul de la longueur du nombre
	N=len(str(A))
	carre=A*A
	# Calcul de la longueur du carre du nombre
	len_carre=len(str(carre))
	partie=len_carre*0.25
	carre=str(carre)
	# On sauvegarde la tranche du milieu du carre
	tranche=carre[int(partie):int(partie+N)]
	# On divise cette tranche par 10^N
	resultat=float(tranche)/float(10**N)
	print("A="+str(A))
	print("N="+str(N))
	print("Carre de A="+str(carre))
	print("Tranche="+str(tranche))
	print("Resultat="+str(resultat))
	print("------------------")
	return resultat

VonNeumann(123456)
VonNeumann(5678)
