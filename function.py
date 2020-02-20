#!/bin/python3
# -*-coding:utf-8 -*

import os.path
import pickle
import tkinter
from mapClass import Map
from labyrinthClass import Labyrinth
from os import listdir

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
    labyrinth.print()
    while continueGame != 1:
        move = input()
        os.system('clear')
        newPst = labyrinth.newPosition(move)
        continueGame = labyrinth.checkNewPosition(newPst)
        labyrinth.print()

# from pynput import keyboard

# def on_press(key):
#     if key == keyboard.Key.esc:
#         return False  # stop listener
#     try:
#         k = key.char  # single-char keys
#     except:
#         k = key.name  # other keys
#     if k in ['1', '2', 'left', 'right']:  # keys of interest
#         # self.keys.append(k)  # store it in global-like variable
#         print('Key pressed: ' + k)
#         return False  # stop listener; remove this if want more keys

# listener = keyboard.Listener(on_press=on_press)
# listener.start()  # start to listen on a separate thread
# listener.join()  # remove if main thread is polling self.keys