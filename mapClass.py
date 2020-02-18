#!/bin/python3
# -*-coding:Utf-8 -*

import pickle

"""Ce module contient la classe Map."""

class Map:

    """Objet de transition entre un fichier et un labyrinthe."""

    def __init__(self, nom, string):
        self.nom = nom
        self.labyrinth = self.createLabyrinth(string)

    def __repr__(self):
        return "<Carte {}>".format(self.nom)

    def createLabyrinth(self, string):
        mapGame = string.split('\n')
        return mapGame

    def returnLabyrinth(self):
        return self.labyrinth



