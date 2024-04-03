#!/usr/bin/env python3
################# SUPRESS PYGAME SUPPORT MESSAGE ###################
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
####################################################################

import pygame, time

SPRITE_DIR = '../imgs/platformerGraphicsDeluxe'

class Sprite():
    def __init__(self, x, y, w, h, img):
        self.identity = None

        # Load the position and size of the sprite
        self.x = x
        self.y = y
        self.w = w
        self.h = h

        # Simple booleans to tell us the direction the sprite is facing
        self.horizontalFlip = False
        self.verticalFlip = False

        # Load the sprite image
        self.spriteImage = pygame.image.load(img)

    def update(self):
        pass

    def identity(self):
        return None

class Clyde(Sprite):
    def __init__(self, x, y):
        # Initialize Clyde and set his identity 
        super().__init__(x, y, 66, 92, SPRITE_DIR + "/Player/p1_front.png")
        self.identity = "CLYDE"

    def addSprite(self, view, sprite):
        # Clyde needs to show up in our world!
        view.screen.blit(pygame.transform.flip(sprite.spriteImage, sprite.horizontalFlip, sprite.verticalFlip),
                         (sprite.x, sprite.y))

    def identify(self):
        return self.identity

class Grass(Sprite):
    def __init__(self, x, y):
        # Initialize
        super().__init__(x, y, 70, 70, SPRITE_DIR + "/Tiles/grass.png")
        self.identity = "GRASS"

    def addSprite(self, view, sprite):
        # Add our block to the world!
        view.screen.blit(pygame.transform.flip(sprite.spriteImage, sprite.horizontalFlip, sprite.verticalFlip), (sprite.x, sprite.y))

    def identify(self):
        return self.identity
