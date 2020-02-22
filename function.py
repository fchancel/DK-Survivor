#!/usr/bin/env python
# -*-coding:utf-8 -*

import pygame
from pygame.locals import *
from constante import Consts

def printBgMenu(frame):
    i = Consts.FRAME_SIZE
    j = 0
    while i < Consts.FRAME_SIZE + 400:
        while j < Consts.FRAME_SIZE:
            bg = pygame.image.load(Consts.OBSTACLE).convert()
            frame.blit(bg, (i, j))
            j += Consts.SIZE_SPRITE
        j = 0
        i += Consts.SIZE_SPRITE
    

def printMenu(frame, choice):
    #MENU
    #AFFICHAGE DU TITRE

    printBgMenu(frame)
    titleText = pygame.font.Font('police/BBB.ttf', 70)
    normalText = pygame.font.Font('police/SuperMario256.ttf', 35)
    tText = titleText.render(Consts.TITLE_FRAME, True, (255, 255, 255))
    titleTextPos = tText.get_rect()
    titleTextPos.topleft = 860, 20

    frame.blit(tText, titleTextPos)

    #AFFICHAGE DES CHOIX
  
    easyLvl = normalText.render("1 - Facile", True, Consts.WHITE)
    mediumLvl = normalText.render('2 - Moyen', True, Consts.WHITE)
    hardLvl = normalText.render('3 - Difficile', True, Consts.WHITE)
    if choice == 0:
        easyLvl = normalText.render("1 - Facile", True, Consts.YELLOW)
    elif choice == 1:
        mediumLvl = normalText.render('2 - Moyen', True, Consts.YELLOW)
    elif choice == 2:
        hardLvl = normalText.render('3 - Difficile', True, Consts.YELLOW)

    easyLvlPos = easyLvl.get_rect() 
    mediumLvlPos = mediumLvl.get_rect() 
    hardLvlPos = hardLvl.get_rect()

    easyLvlPos.topleft = 875, 250
    mediumLvlPos.topleft = 875, 300
    hardLvlPos.topleft = 875, 350

    frame.blit(easyLvl, easyLvlPos)
    frame.blit(mediumLvl, mediumLvlPos)
    frame.blit(hardLvl, hardLvlPos)
    pygame.display.flip()


def printBreak(frame):
    titleText = pygame.font.Font('police/SuperMario256.ttf', 80)
    tText = titleText.render("PAUSE", True, (255, 255, 255))
    titleTextPos = tText.get_rect()
    titleTextPos.topleft = 300, 300

    frame.blit(tText, titleTextPos)

    pygame.display.flip()

def stopEnemyThread(lstEnemy):
    for enemy in lstEnemy:
        enemy.stopThread()
        enemy.join()

def printInGame(frame, labyrinth, lvl):
    lstLvl = ['Facile', 'Moyen', 'Difficile']
    printBgMenu(frame)

    text = pygame.font.Font('police/SuperMario256.ttf', 35)

    #AFFICHAGE DU NIVEAU
    textLvl = text.render(lstLvl[lvl], True, Consts.WHITE)
    textLvlPos = textLvl.get_rect()
    textLvlPos.topleft = 930, 20
    frame.blit(textLvl, textLvlPos)

    #AFFICHAGE NB BANANE RESTANTE
    bananaImg = pygame.image.load(Consts.BANANA_MENU).convert_alpha()
    frame.blit(bananaImg, (850 , 100))

    nbstay = str(labyrinth.totalBanana - labyrinth.nbBanana) + '/' + str(labyrinth.totalBanana)
    bananaStay = text.render(nbstay, True, Consts.WHITE)
    bananaStayPos = bananaStay.get_rect()
    bananaStayPos.topleft = 930, 120
    frame.blit(bananaStay, bananaStayPos)

    #AFFICHAGE DU SCORE
    textScore = text.render("Score : ", True, Consts.WHITE)
    textScorePos = textScore.get_rect()
    textScorePos.topleft = 850, 200
    frame.blit(textScore, textScorePos)

    score = text.render(str(labyrinth.nbBanana * 10), True, Consts.WHITE)
    scorePos = score.get_rect()
    scorePos.topleft = 1000, 200
    frame.blit(score, scorePos)