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
    def __init__(self, block_x, block_y):
        super(Block,self).__init__()
        self.surf = pygame.Surface((75,25))

        # block to be random colour
        self.colour = [random.randint(0,255),random.randint(0,255),random.randint(0,255)]
        self.surf.fill(self.colour)

        self.rect = self.surf.get_rect(
            x=block_x,
            y=block_y
        )

        self.mask = pygame.mask.from_surface(self.surf)
