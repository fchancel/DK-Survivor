
from constante import Consts
import pygame

class Labyrinth:

    def __init__(self, frame, name, strLabyrinth):
        self.frame = frame
        self.name = name
        self.obstacle = 'O'
        self.way = ' '
        self.exitWay = 'U'
        self.ennemie = 'E'
        self.start = 'X'
        self.perso = 'D'
        self.grille = self.createLabyrinth(strLabyrinth)

    def createLabyrinth(self, strLabyrinth):
        labyrinth = strLabyrinth.split('\n')
        lstLabyrinth = []
        for i, string in enumerate(labyrinth):
            lstLabyrinth.append([])
            for char in string:
                lstLabyrinth[i].append(char)
        return lstLabyrinth

    def printLabyrinth(self):
        obstacleImg = pygame.image.load(Consts.OBSTACLE).convert()
        startImg = pygame.image.load(Consts.START).convert()
        arriveImg = pygame.image.load(Consts.ARRIVE).convert_alpha()
        wayImg = pygame.image.load(Consts.WAY).convert()
        for i, string in enumerate(self.grille):
            for j, char in enumerate(string):
                if char == self.obstacle:
                    self.frame.blit(obstacleImg, (j * Consts.SIZE_SPRITE, i * Consts.SIZE_SPRITE))
                elif char == self.way or char == self.ennemie:
                    self.frame.blit(wayImg, (j * Consts.SIZE_SPRITE, i * Consts.SIZE_SPRITE))
                elif char == self.exitWay:
                    self.frame.blit(wayImg, (j * Consts.SIZE_SPRITE, i * Consts.SIZE_SPRITE))
                    self.frame.blit(arriveImg, (j * Consts.SIZE_SPRITE, i * Consts.SIZE_SPRITE))
                elif char == self.start:
                    self.frame.blit(startImg, (j * Consts.SIZE_SPRITE, i * Consts.SIZE_SPRITE))                    


    def findStart(self):
        for i, elt in enumerate(self.grille):
            if self.start in elt:
                return(i, elt.index(self.start))

class Enemy:
    def __init__(self, frame, labyrinth, perso):
        self.frame = frame
        self.labyrinth = labyrinth
        self.perso = perso
        self.enemyPos = findEnemy()
        self.x = enemyPos[0]
        self.y = enemyPos[1]

    # def moveEnemy(self):

    def findEnemy(self):
        for i, elt in enumerate(self.labyrinth.grille):
            if self.labyrinth.enemy in elt:
                return(i, elt.index(self.labyrinth.enemy))

class Perso:

    def __init__(self, frame, labyrinth):
        self.frame = frame
        self.labyrinth = labyrinth
        self.start = self.labyrinth.findStart()
        self.x = self.start[0]
        self.y = self.start[1]
        self.persoPos = self.start
        self.up = pygame.image.load(Consts.DK_UP).convert_alpha()
        self.down = pygame.image.load(Consts.DK_DOWN).convert_alpha()
        self.right = pygame.image.load(Consts.DK_RIGHT).convert_alpha()
        self.left = pygame.image.load(Consts.DK_LEFT).convert_alpha()
        self.direction = self.down 

    def printPerso(self):
        self.frame.blit(self.direction, (self.y * Consts.SIZE_SPRITE, self.x * Consts.SIZE_SPRITE))

    # def moveDk(self, key):
    #     result = self.checkPosition(key)
    #     if result == 0:
    #         if key == 'up'

    def moveDk(self, key):
        i = self.x
        j = self.y
        if key == 'up':
            i -= 1
            self.direction = self.up
        elif key == 'down':
            i += 1
            self.direction = self.down
        elif key == 'left':
            j -= 1            
            self.direction = self.left
        elif key == 'right':
            j += 1
            self.direction = self.right
        print(i, j)
        if i < (Consts.NB_SPRITE ) and j < (Consts.NB_SPRITE ):
            if self.labyrinth.grille[i][j] == self.labyrinth.way or self.labyrinth.grille[i][j] == self.labyrinth.start:
                self.x = i
                self.y = j
                return 0
            elif self.labyrinth.grille[i][j] == self.labyrinth.exitWay:
                self.x = i
                self.y = j
                return 1
            else:
                return -1