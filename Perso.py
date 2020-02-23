from constante import Consts
import pygame

class Perso:
    """
    Class représentant le joueur.
    Gère l'affichage du joueur sur la grille
    Gère la position et l'orientation du personnage joueur

    """
    def __init__(self, frame, labyrinth):
        """
        Initialisation de l'instance.
        Prends en paramètre la frame du jeu et l'instance de la class labyrinth
        Initialise les différentes variables nécéssaire au fonctionnement du jeu.
        labyrinth = instance de la classe labyrinth
        start = Position de départ sur le labyrinth
        x, y = Position du joueur sur la grille
        up, down, right, left = l'image chargé du personnage selon son orientation
        direction = orientation du personnage
        """
        self.frame = frame
        self.labyrinth = labyrinth
        self.start = self.labyrinth.findStart()
        self.x = self.start[0]
        self.y = self.start[1]
        self.up = pygame.image.load(Consts.DK_UP).convert_alpha()
        self.down = pygame.image.load(Consts.DK_DOWN).convert_alpha()
        self.right = pygame.image.load(Consts.DK_RIGHT).convert_alpha()
        self.left = pygame.image.load(Consts.DK_LEFT).convert_alpha()
        self.direction = self.down 

    def printPerso(self):
        """
        Méthode permettant le blit du personnage selon son orientation (attr. direction)
        et selon sa position (attr. x et y)
        Nécéssite un appel extérieur de pygame.display.flip()
        """
        self.frame.blit(self.direction, (self.y * Consts.SIZE_SPRITE, self.x * Consts.SIZE_SPRITE))

    def moveDk(self, key, lstEnemy):
        """
        Prend en paramètre la direction (param. key) voulu par le joueur, 
        ainsi que la liste des instances des ennemies.
        La méthode calcul la nouvelle position sur la grille
        et vérifie si le déplacement est possible.
        retourne 0 si le joueur rencontre un ennemie
        retourne -1 dans les autres cas
        """
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
            for enemy in lstEnemy:
                if (i, j) == (enemy.x, enemy.y):
                    return 0
            if self.labyrinth.grille[i][j][0] != self.labyrinth.obstacle:
                self.x = i
                self.y = j
                self.labyrinth.manageBanana((i, j))
                return -1
        return -1
