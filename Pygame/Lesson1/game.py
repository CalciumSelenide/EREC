#!/usr/bin/env python3
################# SUPRESS PYGAME SUPPORT MESSAGE ###################
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
####################################################################

# Import all of our modules!
import pygame, time
import sprites, model, view, controller

if __name__ == "__main__":
    print("Welcome to EREC's PyGame!")
    time.sleep(1)
    
    # Initialize the game, then start bringing in our Model, View, and Controller
    pygame.init()
    model = model.Model()
    view = view.View(model)
    controller = controller.Controller(model)

    while True:
        # Always update out screen!
        controller.update()
        model.update()
        view.update()

        time.sleep(0.04)

    print("Thanks for playing!")
