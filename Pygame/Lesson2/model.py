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
        # Drop Clyde into our world
        self.clyde = sprites.Clyde(100, 100)
        self.slime = enemies.Slime(300, 300)
        pass

    def update(self):
        # Update our world
        self.slime.update()
        self.clyde.update()
        pass
