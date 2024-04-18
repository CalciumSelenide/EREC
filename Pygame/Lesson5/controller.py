#!/usr/bin/env python3
################# SUPRESS PYGAME SUPPORT MESSAGE ###################
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
####################################################################

import pygame, time
from pygame.locals import *

class Controller(): 
    def __init__(self, model):
        # Initialize the model!
        self.model = model

    def update(self):
        # Get events within the frame!
        for event in pygame.event.get():
            if event.type == QUIT:
                exit()

            # Ignore button holds and ONLY take note on key press
            elif event.type == KEYDOWN:
                # -- Handle all the EXIT/QUIT cases --
                if event.key == K_ESCAPE:
                    exit()
                if event.key == K_q:
                    exit()

            # Ignore initial button press and ONLY take note on key release
            elif event.type == KEYUP:
                if event.key == K_e:
                    self.model.toggleWorldEdit()

            elif (event.type == pygame.MOUSEBUTTONUP and self.model.worldEdit):
                print("Add a sprite here: " + str(pygame.mouse.get_pos()))
                self.model.forceAddSprite(pygame.mouse.get_pos(), "environment") 

        # We want Clyde to move! So find key presses
        keys = pygame.key.get_pressed()

        # If left arrow key is pushed ...
        if keys[K_LEFT]:
            # ... Clyde goes left!
            self.model.clyde.x -= 2

        # If right arrow key is pushed ...
        if keys[K_RIGHT]:
            # ... Clyde goes right!
            self.model.clyde.x +=2

        if (self.model.slime.x > self.model.clyde.x):
            self.model.slime.x = self.model.slime.x - 1

        if (self.model.slime.x < self.model.clyde.x):
            self.model.slime.x = self.model.slime.x + 1

        if (self.model.slime.y > self.model.clyde.y):
            self.model.slime.y = self.model.slime.y - 1

        if (self.model.slime.y < self.model.clyde.y):
            self.model.slime.y = self.model.slime.y + 1
