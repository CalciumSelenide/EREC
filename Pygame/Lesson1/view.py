#!/usr/bin/env python3
################# SUPRESS PYGAME SUPPORT MESSAGE ###################
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
####################################################################

# Import our modules!
import pygame, time

class View():
    def __init__(self, model):
        # Create the screen
        self.screenSize = (800, 600)
        self.screen = pygame.display.set_mode(self.screenSize, 32)
        self.model = model

    def update(self):
        # Set the background color using RGB colors
        self.rgbBlue = (37, 150, 190)
        self.screen.fill(self.rgbBlue)

        # Import Clyde into our model
        self.model.clyde.addSprite(self, self.model.clyde)

        pygame.display.flip()
        pass
