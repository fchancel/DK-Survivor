#!/bin/python3
# -*-coding:utf-8 -*

import os.path
import pickle
from mapClass import Map
from labyrinthClass import Labyrinth
from os import listdir
from pynput import keyboard

def on_press(key):
    global moveKey
    moveKey = 'no'
    if key == keyboard.Key.up:
        moveKey = 'up'
    elif key == keyboard.Key.down:
        moveKey = 'down'
    elif key == keyboard.Key.right:
        moveKey = 'right'
    elif key == keyboard.Key.left:
        moveKey = 'left'
    return False


def choiceMapGame(lstMap):
    """
    Prend en paramètre un dictionnaire comportant les
    noms de la carte ainsi que la carte sous forme de str
    Retourne l'objet mapChoice (instance de la classe Map)
    """
    print('Veuillez choisir quelle carte désirez-vous ?\n')
    for nb, elt in enumerate(lstMap):
        print('{} - {}'.format(nb + 1, elt[0]))
    choice = 0
    sizeMap = len(lstMap)
    while choice < 1 or choice > sizeMap:
        try:
            choice = int(input())
        except ValueError:
            print('Veuillez choisir un chiffre.')
        if choice < 1 or choice > sizeMap:
            print('Veuillez choisir entre 1 et {}.'.format(sizeMap))
    mapName = lstMap[choice - 1][0]
    mapStr = lstMap[choice - 1][1]
    mapChoice = Map(mapName, mapStr)
    os.system('clear')
    return mapChoice


def listFiles(way):
    """
    Prend le nom du dossier ou rechercher les cartes.
    Retourne un dictionnaire comportant le nom de la carte
    ainsi que la carte sous forme str
    """
    lstMap = []
    for fileMap in listdir(way):
        if fileMap.endswith(".txt"):
            nameMap = fileMap[:-4]
            fileWay = os.path.join(way, fileMap)
            with open(fileWay, 'r') as files:
                lstMap.append([nameMap, files.read()])
    return lstMap

def runGame(choiceMap):
    labyrinth = Labyrinth('X', ' ', 'O', 'U', '.' ,choiceMap.returnLabyrinth())
    continueGame = 0
    labyrinth.printColor()
    while continueGame != 1:
        with keyboard.Listener(on_press=on_press) as listener:
            listener.join()
        os.system('clear')
        newPst = labyrinth.newPosition(moveKey)
        continueGame = labyrinth.checkNewPosition(newPst)
        labyrinth.printColor()
