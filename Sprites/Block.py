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
    def __init__(self, block_x, block_y, width, height):
        super(Block,self).__init__()
        self.surf = pygame.Surface((width,height))

        # block to be random colour
        colour = [random.randint(0,255),random.randint(0,255),random.randint(0,255)]
        self.surf.fill((102, 102, 102))

        self.rect = self.surf.get_rect(
            x=block_x,
            y=block_y
        )

        self.mask = pygame.mask.from_surface(self.surf)

        pygame.draw.rect(self.surf, (0,0,0), (2,2,width-5,height-5))
        pygame.draw.rect(self.surf, colour, (0,0,width-5,height-5))