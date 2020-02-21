#!/usr/bin/env python
# -*-coding:utf-8 -*

import pygame
from pygame.locals import *
from constante import Consts
from function import *
from Class import *

pygame.init()
frame = pygame.display.set_mode((Consts.FRAME_SIZE, Consts.FRAME_SIZE))
pygame.display.set_caption(Consts.TITLE_FRAME)

keepFrame = 1
menu = 1
game = 0
choiceLvl = 1
firstTime = 1

pygame.key.set_repeat(100, 50)
while keepFrame == 1: #BOUCLE FENETRE
    while menu == 1: #BOUCLE UTILISATION DU MENU
        pygame.time.Clock().tick(30)
        printMenu(frame, choiceLvl)
        for event in pygame.event.get():
            if event.type == QUIT:
                keepFrame = 0
                menu = 0
            if event.type == KEYDOWN:
                if event.key == K_DOWN and choiceLvl < 3:
                    choiceLvl += 1
                elif event.key == K_UP and choiceLvl > 1:
                    choiceLvl -= 1
                elif event.key == K_1:
                    choiceLvl =1 
                elif event.key == K_2:
                    choiceLvl = 2 
                elif event.key == K_3:
                    choiceLvl = 3 
                elif event.key == K_RETURN:
                    menu = 0
                    game = 1
                elif event.key == K_ESCAPE:
                    game = 0
                    menu = 0
                    keepFrame = 0
    
    while game == 1: #BOUCLE UTILISATION DU JEU
        pygame.time.Clock().tick(30)
        if firstTime == 1:
            with open('maps/n_' + str(choiceLvl) + '.txt', 'r') as fileMap:
                labyrinth = Labyrinth(frame, 'n_' + str(choiceLvl), fileMap.read())
            perso = Perso(frame, labyrinth)
            firstTime = 0

        labyrinth.printLabyrinth()
        perso.printPerso()
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == QUIT:
                keepFrame = 0
                game = 0
            if event.type == KEYDOWN:
                if event.key == K_DOWN:
                    perso.moveDk('down')
                elif event.key == K_UP:
                    perso.moveDk('up')
                elif event.key == K_LEFT:
                    perso.moveDk('left')
                elif event.key == K_RIGHT:
                    perso.moveDk('right')
                elif event.key == K_ESCAPE:
                    game = 0
                    menu = 1
                    firstTime = 1