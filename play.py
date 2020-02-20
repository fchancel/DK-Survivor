#!/usr/bin/env python
# -*-coding:utf-8 -*

import os.path
import pickle
from function import *
from pynput import keyboard
from mapClass import Map
from labyrinthClass import Labyrinth
from os import listdir
"""
    LAUNCHING GAME ROBOC
"""

choice = 0

print("Bienvenu sur le jeu Roboc ! \n")
if os.path.exists('save/inProgress'): #check if game is in progress
    print("SOuhaitez vous reprendre la partie en cours?\n\
    1 : OUI\n\
    2 : NON\n")
    while choice != 1 and choice != 2:
        try:
            choice = int(input())
        except ValueError:
            print('Veuillez choisir un chiffre.')
        if choice < 1 or choice > 2:
            print('Veuillez choisir entre 1 (OUI) ou 2 (NON)')
else:
    choice = 2

if choice == 1 :
    with open('save/inprogress', 'rb') as file:
        inprogess = pickle.Unpickler(file)
        mapGame = inprogess.load()
elif choice == 2:
    lstMap = listFiles('maps')
    choiceMap = choiceMapGame(lstMap)
    runGame(choiceMap)


