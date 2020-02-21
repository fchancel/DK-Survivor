#!/usr/bin/env python
# -*-coding:utf-8 -*

import pygame
from pygame.locals import *
from constante import Consts

def printMenu(frame, choice):
    #MENU
    #AFFICHAGE DU TITRE
    titleText = pygame.font.SysFont('quicksand', 60)
    normalText = pygame.font.SysFont('dejavusansmono', 35)
    tText = titleText.render(Consts.TITLE_FRAME, True, (255, 255, 255))
    titleTextPos = tText.get_rect()
    titleTextPos.centerx = frame.get_rect().centerx
    titleTextPos.centery = 50

    frame.blit(tText, titleTextPos)

    #AFFICHAGE DES CHOIX
    white = (255, 255, 255)
    green = (55, 255, 55)
    easyLvl = normalText.render("1 - Facile", True, white)
    mediumLvl = normalText.render('2 - Moyen', True, white)
    hardLvl = normalText.render('3 - Difficile', True, white)
    if choice == 1:
        easyLvl = normalText.render("1 - Facile", True, green)
    elif choice == 2:
        mediumLvl = normalText.render('2 - Moyen', True, green)
    elif choice == 3:
        hardLvl = normalText.render('3 - Difficile', True, green)

    easyLvlPos = easyLvl.get_rect() 
    mediumLvlPos = mediumLvl.get_rect() 
    hardLvlPos = hardLvl.get_rect()

    easyLvlPos.topleft = 250, 250
    mediumLvlPos.topleft = 250, 300
    hardLvlPos.topleft = 250, 350

    frame.blit(easyLvl, easyLvlPos)
    frame.blit(mediumLvl, mediumLvlPos)
    frame.blit(hardLvl, hardLvlPos)

    pygame.display.flip()
