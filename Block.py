import pygame
import random

from pygame.locals import (
    RLEACCEL,
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT
)

class Block(pygame.sprite.Sprite):
    def __new__(cls, *args,**kwargs):
        return super().__new__(cls)

    def __init__(self, screen_width, screen_height):
        super(Block,self).__init__()
        self.surf = pygame.Surface((75,25))

        #block to be random colour
        self.colour = [random.randint(0,255),random.randint(0,255),random.randint(0,255)]
        self.surf.fill(self.colour)

        #draw random area for now -- need to implement no overlap with existing
        self.rect = self.surf.get_rect(
            center=(
                random.randint(75, (screen_width-75)),
                random.randint(25, (screen_height-50))
            )
        )
