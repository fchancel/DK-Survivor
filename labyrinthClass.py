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
        self.obstacles = obstacles
        self.exitway = exitway
        self._grille = labyrinth

    def __str__(self):
        print('')

    def print(self):
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
    
    def checkPosition(self, key):
        positionRobot = self.findRobot()



    def findRobot(self):
        """
        Renvoie la position du robot
        """
        for i, elt in enumerate(self._grille):
            if self.robot in elt:
                return(i, elt.index(self.robot))

