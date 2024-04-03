#!/usr/bin/env python3
################# SUPRESS PYGAME SUPPORT MESSAGE ###################
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
####################################################################

# Import our modules
import pygame, time
import sprites, enemies

class Model():
    def __init__(self):
        # Load map
        self.mapLoad()

        # Drop Clyde into our world
        self.clyde = sprites.Clyde(100, 100)
        self.slime = enemies.Slime(300, 300)
        self.grass = sprites.Grass(70, 100)
        pass

    def update(self):
        # Update our world
        self.slime.update()
        self.clyde.update()
        pass

    def mapLoad(self):
        # Load the map
        fyle = open('map.txt', mode='r')
        
        try:
            self.map = eval(fyle.read())
        except:
            self.map = None
        
        fyle.close()

    def mapSave(self):
        # Save the map
        fyle = open('map.txt', mode='w')
        fyle.write(self.map)
        fyle.close()
