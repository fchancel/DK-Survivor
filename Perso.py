from random import randrange
from constante import Consts
import pygame
import time
from threading import Thread

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
            if self.labyrinth.grille[i][j][0] == '1' or self.labyrinth.grille[i][j][0] == '2' or self.labyrinth.grille[i][j][0] == '3':
                print('fewfwe')
                return 0
            if self.labyrinth.grille[i][j][0] != self.labyrinth.obstacle:
                self.x = i
                self.y = j
                self.labyrinth.manageBanana((i, j))
                return -1
