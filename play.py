#!/usr/bin/env python
# -*-coding:utf-8 -*

import pygame
from pygame.locals import *
from random import randrange
from constante import Consts
from function import *
from Enemy import *
from Labyrinth import *
from Perso import *

#INITIALISATION FENETRE
pygame.init()
frame = pygame.display.set_mode((Consts.FRAME_SIZE + 400, Consts.FRAME_SIZE))
pygame.display.set_caption(Consts.TITLE_FRAME)

keepFrame = True #MAINTIENT LA FENETRE ACTIVE
menu = True #VERIFIE SI NOUS SOMMES DANS LE MENU
game = False #VERIFIE SI NOUS SOMMES DANS UNE PARTIE
lvl = 0 #CHOIX DU LEVEL
firstTime = True #VERIFIE SI C'EST LE PREMIER LANCEMENT DE LA PARTIE AFIN D'INITIALISER LES ENNEMIES
returnToBreak = False #VERIFIE SI LE JOUEUR REVIENT DE PAUSE
lstLabyrinth = list() #LIST CONTENANT LES LABYRINTH
nbFile = 3 #NOMBRE DE FICHIER LABYRINTH DISPONIBLE
count = 0 #COMPTEUR GÉNÉRAL
contactEnemy = -1 #VALEUR POUR SAVOIR SI VICTOIRE OU DÉFAITE

#AJOUTE DANS LA LISTE DES LABYRINTH, LES OBJECTS CLASS CONTENANT CHACUN UN LABYRINTH
while count < nbFile:
    with open('maps/n_' + str(count) + '.txt', 'r') as fileMap:
        lstLabyrinth.append(Labyrinth(frame, 'n_' + str(nbFile), fileMap.read()))
    count += 1

lstLabyrinth[lvl].printLabyrinth(None, None)

pygame.key.set_repeat(100, 50)
while keepFrame == True: #BOUCLE FENETRE
    print(' ')            
    #BOUCLE UTILISATION DU MENU
    while menu == True: 
        pygame.time.Clock().tick(30)
        printMenu(frame, lvl)
        for event in pygame.event.get():
            if event.type == QUIT:
                keepFrame = False
                menu = False
            if event.type == KEYDOWN:
                #GESTION DE L'AFFICHAGE ET DU CHOIX DE LEVEL
                if event.key == K_DOWN and lvl < 2:
                    lvl += 1
                    lstLabyrinth[lvl].printLabyrinth(None, None)
                elif event.key == K_UP and lvl > 0:
                    lvl -= 1
                    lstLabyrinth[lvl].printLabyrinth(None, None)
                elif event.key == K_1:
                    lvl = 0 
                    lstLabyrinth[lvl].printLabyrinth(None, None)
                elif event.key == K_2:
                    lvl = 1 
                    lstLabyrinth[lvl].printLabyrinth(None, None)
                elif event.key == K_3:
                    lvl = 2
                    lstLabyrinth[lvl].printLabyrinth(None, None) 
                #GESTION ENTRE MENU ET JEU
                elif event.key == K_RETURN:
                    menu = False
                    game = True
                elif event.key == K_ESCAPE:
                    game = False
                    menu = False
                    keepFrame = False
    
    #BOUCLE UTILISATION DU JEU
    while game == True: 
        pygame.time.Clock().tick(8)
        printInGame(frame, lstLabyrinth[lvl], lvl)

        #INITIALISATION DU PERSO, DES ENNEMIES ET DU MULTI THREAD
        if firstTime == True:
            firstTime = False
            perso = Perso(frame, lstLabyrinth[lvl])
            count = 0
            lstEnemy = []
            while count <= lvl: #INITIALISATION DU NOMBRE D'ENNEMI SELON LE NIVEAU
                lstEnemy.append(Enemy(frame, lstLabyrinth[lvl], perso, str(count + 1)))
                count += 1
            for enemy in lstEnemy: #INITIALISATION DU MULTI THREAD
                enemy.way = randrange(0, 4)
                enemy.start()

        if returnToBreak == True:
            for enemy in lstEnemy:
                enemy.againThread()
            returnToBreak == False

        #GESTION AFFICHAGE DE LA PARTIE
        lstLabyrinth[lvl].printLabyrinth(perso, lstEnemy)

        #VERIFICATION VICTOIRE OU DÉFAITE
        for enemy in lstEnemy:
            if enemy.loose == True :
                contactEnemy = 0
        #GESTION DES EVENEMENT
        
        for event in pygame.event.get():
            if event.type == QUIT:
                keepFrame = False
                game = False
            if event.type == KEYDOWN:
                #GESTION DU MOUVEMENT DU PERSO
                if event.key == K_DOWN:
                    contactEnemy = perso.moveDk('down', lstEnemy)
                    direction = 'down'
                    lstLabyrinth[lvl].printLabyrinth(perso, lstEnemy)
                elif event.key == K_UP:
                    contactEnemy = perso.moveDk('up', lstEnemy)
                    direction = 'up'
                    lstLabyrinth[lvl].printLabyrinth(perso, lstEnemy)
                elif event.key == K_LEFT:
                    contactEnemy = perso.moveDk('left', lstEnemy)
                    direction = 'left'
                    lstLabyrinth[lvl].printLabyrinth(perso, lstEnemy)
                elif event.key == K_RIGHT:
                    contactEnemy = perso.moveDk('right', lstEnemy)
                    direction = 'right'
                    lstLabyrinth[lvl].printLabyrinth(perso, lstEnemy)    
                #GESTION DU MODE PAUSE
                elif event.key == K_SPACE:
                    game = False
                    returnToBreak = False
                    for enemy in lstEnemy:
                        enemy.breakThread()
                    printBreak(frame)
                #GESTION DE LA SORTIE DE PARTIE
                elif event.key == K_ESCAPE:
                    game = False
                    menu = True
                    firstTime = True
                    stopEnemyThread(lstEnemy)
                    lstLabyrinth[lvl].createLabyrinth()
                    lstLabyrinth[lvl].printLabyrinth(None, None)
        noBanana = lstLabyrinth[lvl].finishBanana()
        if contactEnemy == 0 or noBanana == 1:
            stopEnemyThread(lstEnemy)
            game = 0
            lstLabyrinth[lvl].finishGame(contactEnemy, noBanana)
    #GESTION MODE PAUSE
    for event in pygame.event.get():
        if event.type == QUIT:
            keepFrame = False
            stopEnemyThread(lstEnemy)
        if event.type == KEYDOWN:
            if event.key == K_SPACE:
                if contactEnemy == -1:
                    game = True
                    returnToBreak = True
            elif event.key == K_ESCAPE:
                stopEnemyThread(lstEnemy)
                menu = True
                firstTime = True
                contactEnemy = -1
                lstLabyrinth[lvl].createLabyrinth()
                lstLabyrinth[lvl].printLabyrinth(None, None)
