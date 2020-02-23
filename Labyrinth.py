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
        self.banana = ' '
        self.start = 'X'
        self.perso = 'D'
        self.totalBanana = int()
        self.nbBanana = int()
        self.strLabyrinth = strLabyrinth
        self.grille = list()
        self.createLabyrinth()

    def createLabyrinth(self):
        self.nbBanana = 0
        banana = 0
        labyrinth = self.strLabyrinth.split('\n')
        lstLabyrinth = []
        for i, string in enumerate(labyrinth):
            lstLabyrinth.append([])
            for char in string:
                if char != self.obstacle and char != self.start:
                    lstLabyrinth[i].append([char, 1])
                    banana += 1
                else:
                    lstLabyrinth[i].append([char, 0])
        self.totalBanana = banana
        self.grille = lstLabyrinth

    def printLabyrinth(self, perso, lstEnemy):
        obstacleImg = pygame.image.load(Consts.OBSTACLE).convert()
        startImg = pygame.image.load(Consts.START).convert()
        bananaImg = pygame.image.load(Consts.BANANA).convert_alpha()
        wayImg = pygame.image.load(Consts.WAY).convert()
        for i, string in enumerate(self.grille):
            for j, char in enumerate(string):
                if char[0] == self.obstacle:
                    self.frame.blit(obstacleImg, (j * Consts.SIZE_SPRITE, i * Consts.SIZE_SPRITE))
                elif char[0] == self.start:
                    self.frame.blit(startImg, (j * Consts.SIZE_SPRITE, i * Consts.SIZE_SPRITE))
                elif char[0] != self.obstacle:
                    self.frame.blit(wayImg, (j * Consts.SIZE_SPRITE, i * Consts.SIZE_SPRITE))
                if char[0] != self.obstacle and char[1] ==  1:
                    self.frame.blit(bananaImg, (j * Consts.SIZE_SPRITE, i * Consts.SIZE_SPRITE))
        if perso != None: 
                perso.printPerso()
        if lstEnemy != None:
            for enemy in lstEnemy:
                enemy.printEnemy()     
        pygame.display.flip()       

    def manageBanana(self, pos):
        i = pos[0]
        j = pos[1]
        if self.grille[i][j][1] == 1:
            self.grille[i][j][1] = 0
            self.nbBanana += 1

    def finishBanana(self):
        if self.totalBanana - self.nbBanana == 0:
            return 1 

    def findStart(self):
        for i, elt in enumerate(self.grille):
            for j, char in enumerate(elt):
                if self.start in char:
                    return(i, j)

    def finishGame(self, contactEnemy, noBanana):
        """
        Result contient soit 1 en cas de victoire soit 0 en cas de défaite
        """
        text = pygame.font.Font('police/SuperMario256.ttf', 80)
        if contactEnemy == 0:
            loose = text.render('PERDU', True, Consts.WHITE)
            loosePos = loose.get_rect()
            loosePos.topleft = 300, 300
            self.frame.blit(loose, loosePos)
        elif noBanana == 1:
            win = text.render('GAGNER', True, Consts.WHITE)
            winPos = win.get_rect()
            winPos.topleft = 300, 300
            self.frame.blit(win, winPos)
            
        pygame.display.flip()

    def __repr__(self):
        return '<class labyrinth {}>'.format(self.name)