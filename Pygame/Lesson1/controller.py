#!/usr/bin/env python3
################# SUPRESS PYGAME SUPPORT MESSAGE ###################
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
####################################################################

import pygame, time
from pygame.locals import *

class Controller():
    def __init__(self, model):
        self.model = model

    def update(self):
        # Get events within the frame!
        for event in pygame.event.get():
            if event.type == QUIT:
                exit()

            # Ignore initial button press and ONLY take note on key release
            elif event.type == KEYDOWN:
                # -- Handle all the EXIT/QUIT cases --
                if event.key == K_ESCAPE:
                    exit()
                if event.key == K_q:
                    exit()

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
