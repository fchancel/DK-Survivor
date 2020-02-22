from random import randrange
from constante import Consts
import pygame
import time
from threading import Thread

class Labyrinth:

    def __init__(self, frame, name, strLabyrinth):
        self.frame = frame
        self.name = name
        self.obstacle = 'O'
        self.way = ' '
        self.exitWay = 'U'
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
                elif char == self.exitWay:
                    self.frame.blit(wayImg, (j * Consts.SIZE_SPRITE, i * Consts.SIZE_SPRITE))
                    self.frame.blit(arriveImg, (j * Consts.SIZE_SPRITE, i * Consts.SIZE_SPRITE))
                elif char == self.start:
                    self.frame.blit(startImg, (j * Consts.SIZE_SPRITE, i * Consts.SIZE_SPRITE))
                else:
                    self.frame.blit(wayImg, (j * Consts.SIZE_SPRITE, i * Consts.SIZE_SPRITE))                 


    def findStart(self):
        for i, elt in enumerate(self.grille):
            if self.start in elt:
                return(i, elt.index(self.start))

    def __repr__(self):
        return '<class labyrinth {}>'.format(self.name)

class Enemy(Thread):
    def __init__(self, frame, labyrinth, perso, enemy):
        Thread.__init__(self)
        self.enemy = enemy
        self.frame = frame
        self.cross = 'C'
        self.labyrinth = labyrinth
        self.perso = perso
        self.continueThread = True
        self.haltThread = True
        self.enemyPos = self.findEnemy()
        self.x = self.enemyPos[0]
        self.y = self.enemyPos[1]
        self.up = pygame.image.load(Consts.ENEMY_UP).convert_alpha()
        self.down = pygame.image.load(Consts.ENEMY_DOWN).convert_alpha()
        self.right = pygame.image.load(Consts.ENEMY_RIGHT).convert_alpha()
        self.left = pygame.image.load(Consts.ENEMY_LEFT).convert_alpha()
        self.direction = self.down
        self.way = 0

    def run(self):
        while self.continueThread == True:
            while self.haltThread == True:
                time.sleep(0.17)
                self.moveEnemy()

    def breakThread(self):
        self.haltThread = False

    def againThread(self):
        self.haltThread = True

    def stopThread(self):
        self.haltThread = False
        self.continueThread = False


    def printEnemy(self):
        self.frame.blit(self.direction, (self.y * Consts.SIZE_SPRITE, self.x * Consts.SIZE_SPRITE))

    def moveEnemy(self):
        pygame.time.Clock().tick(3000)
        i = self.x
        j = self.y
        lst = ['down', 'left', 'up', 'right']
        if lst[self.way] == 'up':
            i -= 1
            self.direction = self.up
        elif lst[self.way] == 'down':
            i += 1
            self.direction = self.down
        elif lst[self.way] == 'left':
            j -= 1            
            self.direction = self.left
        elif lst[self.way] == 'right':
            j += 1
            self.direction = self.right
        if i < (Consts.NB_SPRITE ) and j < (Consts.NB_SPRITE ):
            if self.labyrinth.grille[i][j] != self.labyrinth.obstacle :
                self.x = i
                self.y = j
                if self.labyrinth.grille[i][j] == self.cross:
                    self.way = randrange(0, 4) 
            else:
                self.way = randrange(0, 4)
                self.moveEnemy()
        else:
            self.way = randrange(0, 4)
            self.moveEnemy()


    def findEnemy(self):
        for i, elt in enumerate(self.labyrinth.grille):
            if self.enemy in elt:
                return(i, elt.index(self.enemy))

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
        if i < (Consts.NB_SPRITE ) and j < (Consts.NB_SPRITE ):
            if self.labyrinth.grille[i][j] != self.labyrinth.obstacle:
                self.x = i
                self.y = j
                return 0
            elif self.labyrinth.grille[i][j] == self.labyrinth.exitWay:
                self.x = i
                self.y = j
                return 1
            else:
                return -1