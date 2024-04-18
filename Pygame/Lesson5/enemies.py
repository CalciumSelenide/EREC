import pygame, sprites

class Slime(sprites.Sprite):
    def __init__(self, x, y):
        # Initialize the slime and set his identity
        super().__init__(x, y, 66, 92, sprites.SPRITE_DIR + "/Enemies/slimeWalk1.png")
        self.identity = "SLIME"

    def addSprite(self, view, sprite):
        # The slime needs to show up in our world!
        view.screen.blit(pygame.transform.flip(sprite.spriteImage, sprite.horizontalFlip, sprite.verticalFlip),
                         (sprite.x, sprite.y))

    def identify(self):
        return self.identity

