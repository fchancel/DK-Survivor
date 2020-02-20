#!/bin/python3
# -*-coding:Utf-8 -*

"""Ce module contient la classe Labyrinth."""

class Labyrinth:
    """Classe représentant un labyrinthe."""

    #attribut pour mettre en couleur les éléments du labyrinthe
    escape = "\033"
    colorRobot = escape + "[31m\033[47m" 
    colorObsacle = escape + "[44m\033[34m"
    colorWay = escape + "[47m\033[97m"
    colorExit = escape + "[41m\033[31m"
    colorDoor = escape + "[42m\033[32m"
    endColor = escape + "[39m"
    endBgColor = escape + "[49m"
    
    def __init__(self, robot, way, obstacles, exitway, door, labyrinth):
        """
        Initialise les différents composant nécéssaire à la création du labyrinthe
        """
        self.robot = robot
        self.door = door
        self.way = way
        self.oldPosition = way
        self.obstacles = obstacles
        self.exitway = exitway
        self._grille = labyrinth

    def __str__(self):
        print('')

    def printColor(self):
        """
        Affiche le labyrinthe
        """
        labyrinth = self.colorLabyrinth(self._grille)
        for elt in labyrinth:
            print(elt)

    # def returnLabyrinth(self):
    #     return self._grille

    # def returnStrLabyrinth(self):
    #     string = '\n'.join(self._grille)
    #     print(string)
    #     return(string)

    def colorLabyrinth(self, labyrinth):
        """
        Met en couleur les éléments du labyrinthe
        Retourne une liste comportant le labyrinthe
        """
        newElt = []
        newLabyrinth = []
        for lst in labyrinth:
            for elt in lst:
                if elt == self.obstacles:
                    newElt.append(self.colorObsacle + elt + self.endBgColor)
                elif elt == self.way:
                    newElt.append(self.colorWay + elt + self.endBgColor)
                elif elt == self.exitway:
                    newElt.append(self.colorExit + elt + self.endBgColor)
                elif elt == self.robot:
                    newElt.append(self.colorRobot + elt + self.endColor) 
                elif elt == self.door:
                    newElt.append(self.colorDoor + elt + self.endBgColor)
            newLabyrinth.append(''.join(newElt))
            newElt = [] 
        return(newLabyrinth)
    
    def newPosition(self, key):
        """
        Prends en paramètre key, qui correspond à la direction souhaité par le joueur
        Retourne une tuple correspondant au indice de la grille correspondant à la position
        """
        pstRobot = self.findRobot()
        i = pstRobot[0]
        j = pstRobot[1]
        if key == 'up':
            i-=1
        elif key == 'down':
            i+=1
        elif key == 'left':
            j-=1
        elif key == 'right':
            j+=1
        return (i, j)
    

    def checkNewPosition(self, newPst):
        """
        Prend en paramètre la nouvelle position voulu.
        Verifie s'il est possible d'accéder à la nouvelle position
        Retourne 1 si la nouvelle position est la sortie
        Retourne 0 si la nouvelle position est OK
        Retourne -1 si la nouvelle position est inaccessible
        """
        onNewPst = self._grille[newPst[0]][newPst[1]]
        if onNewPst == self.exitway:
            self.moveRobot(newPst)
            return 1
        elif onNewPst == self.way or onNewPst == self.door:
            self.moveRobot(newPst)
            return 0
        else:
            # VERIFIER DE NE PAS SORTIR DE LA CARTE
            return -1

    def moveRobot(self,newPst):
        """
        Prends en paramètre la nouvelle position désiré
        Déplace le robot sur la nouvelle position
        Réinscrit ce qui se situait sous l'ancienne position (porte, chemin, obstacle)
        """
        oldPst = self.findRobot()
        Oi = oldPst[0]
        Oj = oldPst[1]
        Ni = newPst[0]
        Nj = newPst[1]
        Nstring = self._grille[Oi][:Oj] + self.oldPosition + self._grille[Oi][Oj + 1:]
        self._grille[Oi] = Nstring
        self.oldPosition = self._grille[Ni][Nj]
        Nstring = self._grille[Ni][:Nj] + self.robot + self._grille[Ni][Nj + 1:]
        self._grille[Ni] = Nstring

    def findRobot(self):
        """
        Renvoie la position du robot
        """
        for i, elt in enumerate(self._grille):
            if self.robot in elt:
                return(i, elt.index(self.robot))




