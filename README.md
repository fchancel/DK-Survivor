# DK SURVIVOR

## Challenge

Découverte du langage Python et de ses paquets graphique (pygame).
Création d'un jeu 2D où le joueur à le rôle de Donkey Kong et dont son objectif
est de récupérer toutes les bananes sur le labyrinth sans rencontrer un ennemie.

Le joueur débute en choisissant un niveau : Facile, Moyen, Difficile.
Le niveau est régulé par le nombre d'ennemie, allant de 1 à 3 et par la quantité 
de banane à récupérer.

Dès le lancement de la partie, le joueur doit se déplacer avec l'aide des flèches
directionnelles de son clavier. 

À tout moment le joueur peut soit quitter la partie avec l'aide de la touche échappe
ou mettre la partie en Pause avec la barre espace du clavier.

La partie prend fin lorsque le joueur rencontre un ennemie (défaite) ou lorsqu'il 
réussit à récupérer toutes les bananes (victoire)

## Détails et Conception

Le menu (sélection du niveau) affiche la représentation des labyrinthes sur la 
partie gauche de la fênetre selon le niveau sélectionné.

La séléction des niveaux se fait avec l'aide des flèches directionnelles ou avec 
l'aide des chiffres indiqués.

Les labyrinthes sont créées à partir de fichier texte (trouvable dans le dossier
/map).

Les ennemies sont lancés sur différents thread afin d'être indépendant les uns 
des autres. Leurs mouvements sont semi aléatoirs.

## Démonstration

![Démonstration ft_ls](https://gitlab.com/fchancel/python-terminal-labyrinth-game/-/blob/master/img/dk-demo.gif)