# nbr_pseudoaleatoire
Génération de nombres pseudo-aléatoires

## Exercice 1

Au vu du graphe, l'aléatoire de la fonction `random.randrange` donnée par
le constructeur n'est pas satisfaisant.
Chaque bar devrait avoir une probabilité de 1 / N car nous sommes dans l'intervalle
{1, ..., 10} (à mettre en fraction dans LateX) .
Dans notre exemple, N = 10. Pour chaque barre, 1 / N devrait donc être égale à 0,10
.

Prenons la première barre, on remarque que la valeur 1 est sortie 918 fois
Calculons sa probabilité :
918 / 10 000 = 0.0918

Prenons la dernière barre, on remarque que la valeur 10 est sortie 1736 fois
Calculons sa probabilité :
1736 / 10 000 = 0.1736

Les probabilités d'apparitions de chaque valeur ne respecte donc pas 0.10.
En conclusion, la fonction `random.randrange` n'est pas aléatoire et pour notre
exemple, la valeur 10 apparait le plus souvent.

## Exercice 2

Ce programme permet de calculer 100 fois une valeur comprise entre 0 et 1,
multiplié par 3 et arrondi. La valeur est choisit grâce à la fonction : aleatoire().
Pour terminer ce nombre est affiché dans la console et la boucle est incrémentée.

Au vu du graphe nous pensons que cette algorithme se rapproche d'un algorithme
aléatoire mais n'en est pas un.
Pour le prouver calculons la probabilités théorique de chaque valeur :
1 / (N + 1) = 0.25 avec N = 3

0 = 0,15
1 = 0,32
2 = 0,33
3 = 0,20

Cette fois les probabilités obtenues se rapproche un peu plus de la probabilité
théorique cependant on ne peut pas encore parler d'aléatoire car les différences
entre chaque probabilités d'apparition est bien trop différente.

## Exercice 3
