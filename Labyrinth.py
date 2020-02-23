from constante import Consts
import pygame

class Labyrinth:
    """
    Class représentant un labyrinth.
    Gestion de la création d'une grille labyrinth (list) à partir d'une str
    Affichage du labyrinth
    Gestion du nombre de banane
    Gestion de la fin de partie
    """
    def __init__(self, frame, name, strLabyrinth):
        """
        Initialisation de l'instance labyrinth.
        Prend en paramètre la frame du jeu, le nom du labyrinth 
        et la str permettant la création de la grille
        frame = frame du jeu
        name = nom de la carte du labyrinth
        strLabyrinth = string initial permettant la création de la grille
        grille = triple list représentant le labyrinth
        obstacle, banana, start, perso = représentation des éléments du labyrinth dans la string
        totalBanana = nombre total de banane dans la partie
        nbBanana = nombre de banane récupéré par le joueur
        """
        self.frame = frame
        self.name = name
        self.strLabyrinth = strLabyrinth
        self.grille = list()
        self.createLabyrinth()
        self.obstacle = 'O'
        self.banana = ' '
        self.start = 'X'
        self.perso = 'D'
        self.totalBanana = int()
        self.nbBanana = int()

    def createLabyrinth(self):
        """
        Méthode initialisant une triple liste représentant le labyrinth,
        initialise également le nombre total de banane sur le terrain.
        """
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
        """
        Méthode permettant d'afficher le labyrinth, avec son joueurs et ses ennemies 
        avec l'aide des fonctions printPerso() issu de la class Perso
        et printEnemy() isu de la class Enemy
        Prends en paramètre l'instance de la classe Perso
        ainsi que la list des instances de la class Enemy
        """
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
        """
        Méthode ajustant les bananes sur la grille et calculant le nombre de 
        bananes récupéré par le joueur
        """
        i = pos[0]
        j = pos[1]
        if self.grille[i][j][1] == 1:
            self.grille[i][j][1] = 0
            self.nbBanana += 1

    def finishBanana(self):
        """
        Méthode permettant de vérifier si le joueur à récupérer toutes les bananes
        """
        if self.totalBanana - self.nbBanana == 0:
            return 1 

    def findStart(self):
        """
        Méthode retournant le point de départ du joueur
        """
        for i, elt in enumerate(self.grille):
            for j, char in enumerate(elt):
                if self.start in char:
                    return(i, j)

    def finishGame(self, contactEnemy, noBanana):
        """
        Méthode permettant de savoir si le joueur est gagnant ou perdant.
        Prends en paramètre contactEnemy (0 si le joueur à été en contact avec l'ennemie)
        et noBanana (1 si le joueur récupère toutes les bananes)
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