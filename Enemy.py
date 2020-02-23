from random import randrange
from constante import Consts
import pygame
import time
from threading import Thread

class Enemy(Thread):
    """
    Class représentant un ennemie.
    Permet de lancer les différents Thread.
    Gestion des thread.
    Gestion des mouvements de l'ennemie sur la grille.
    """
    def __init__(self, frame, labyrinth, perso, enemy):
        """
        Initialisation de l'instance.
        Prend en paramètre la frame du jeu, l'instance de la classe labyrinth,
        l'instance de la class perso, ainsi que le symbole représentant l'ennemi
        sur la grille.
        frame = frame du jeu
        labyrinth = instance de la class labyrinth
        perso = instance de la class perso
        enemy = symbole representant l'ennemie sur la grille
        cross = symbole representant les croisements sur la grille (nécéssaire pour la gestion des mouvements de l'ennemi)
        loose = booléen permettant de savoir si l'ennemi est rentré en contact avec le joueur
        continuedThread = booléen gérant la fin du thread
        haltThread = booléen permettant de mettre en pause le thread (nécéssaire pour le mode Pause durant la partie)
        enemyPos = position initial de l'ennemie
        x, y = position actuel de l'ennemie
        up, down, right, left = image chargé de l'ennemie selon son orientation
        direction = orientation de l'ennemie
        way = Chiffre entre 0 et 3, permettant de créer un mouvement aléatoire de l'ennemie (chaque chiffre correspondant à une destination)
        """
        Thread.__init__(self)
        self.frame = frame
        self.labyrinth = labyrinth
        self.perso = perso
        self.enemy = enemy
        self.cross = 'C'
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
        """
        Méthode permettant le lancement du thread, permettant le déplacement de l'ennemie 
        en appelant la méthode moveEnemy().
        """
        while self.continueThread == True:
            while self.haltThread == True:
                time.sleep(0.15)
                self.moveEnemy()

    def breakThread(self):
        """
        Méthode permettant de mettre en pause le thread
        """
        self.haltThread = False

    def againThread(self):
        """
        Méthode permettant de mettre en reprendre le thread après une mise en pause
        """
        self.haltThread = True

    def stopThread(self):
        """
        Méthode permettant de stopper le thread
        """
        self.haltThread = False
        self.continueThread = False

    def printEnemy(self):
        """
        Méthode permettamt le blit de l'image de l'ennemie.
        Nécéssite l'appelle extérieur de pygame.display.flip()
        """
        self.frame.blit(self.direction, (self.y * Consts.SIZE_SPRITE, self.x * Consts.SIZE_SPRITE))

    def moveEnemy(self):
        """
        Méthode permettant le mouvement aléatoire de l'ennemie.
        Récursif, la méthode se rappel si l'ennemie rencontre
        un obstacle ou un croisemment.
        """
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
        """
        Méthode permettant de connaitre la position initiale de l'ennemi sur la grille
        """
        for i, elt in enumerate(self.labyrinth.grille):
            for j, char in enumerate(elt):
                if self.enemy in char[0]:
                    return (i, j)
