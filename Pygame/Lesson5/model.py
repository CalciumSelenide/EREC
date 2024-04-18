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
        self.worldMap = {"ENVIRONMENT": []}
        # Load map
        self.mapLoad()
        self.worldEdit = False

        # Drop Clyde into our world
        self.clyde = sprites.Clyde(100, 100)
        self.slime = enemies.Slime(300, 300)
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

        # Now we try to place all the objects in our map
        count = 0
        for key, value in self.map.items():
            print("Loading: " + key)
            if (key == "ENVIRONMENT"):
                for secondKey, secondValue in value.items():
                    print(secondKey, secondValue)
                    envObj = getattr(sprites, secondValue[0])
                    envObj = envObj(secondValue[1][0], secondValue[1][1])
                    self.worldMap["ENVIRONMENT"].append(envObj)
                    count += 1
    
    def mapSave(self):
        # Save the map
        fyle = open('map.txt', mode='w')
        fyle.write(self.map)
        fyle.close()

    def toggleWorldEdit(self):
        self.worldEdit = not self.worldEdit
        print("World edit: " + str(self.worldEdit))

    def forceAddSprite(self, coords:tuple, entity:str=""):
        spriteHere = False

        # Update the world Map
        if entity:
            # Make our entitiy ...
            grassBlock = sprites.Grass(coords[0], coords[1])
            
            # ... now lets do some math so it snaps to a grid ...
            grassBlockWidth = (int(grassBlock.x / 70) * 70)
            grassBlockHeight = (int(grassBlock.y / 70) * 70)

            grassBlock.x = grassBlockWidth
            grassBlock.y = grassBlockHeight

            self.worldMap[entity.upper()].append(grassBlock)
            #print(self.worldMap)

