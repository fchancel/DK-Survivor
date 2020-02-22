from random import randrange
from constante import Consts
import pygame
import time
from threading import Thread

class Enemy(Thread):
    def __init__(self, frame, labyrinth, perso, enemy):
        Thread.__init__(self)
        self.enemy = enemy
        self.frame = frame
        self.cross = 'C'
        self.labyrinth = labyrinth
        self.perso = perso
        self.loose = False
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
                time.sleep(0.15)
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
        i = self.x
        j = self.y
        lst = ['down', 'left', 'up', 'right']
        if (self.x, self.y) == (self.perso.x, self.perso.y):
            self.loose = True
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
            if self.labyrinth.grille[i][j][0] != self.labyrinth.obstacle :
                self.x = i
                self.y = j
                if self.labyrinth.grille[i][j][0] == self.cross:
                    self.way = randrange(0, 4) 
            else:
                self.way = randrange(0, 4)
                self.moveEnemy()
        else:
            self.way = randrange(0, 4)
            self.moveEnemy()

    def findEnemy(self):
        for i, elt in enumerate(self.labyrinth.grille):
            for j, char in enumerate(elt):
                if self.enemy in char[0]:
                    return (i, j)
