import pygame

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

class PlayerPaddle(pygame.sprite.Sprite):
    def __new__(cls, *args,**kwargs):
        return super().__new__(cls)

    def __init__(self, SCREEN_WIDTH, SCREEN_HEIGHT):
        super(PlayerPaddle, self).__init__()
        self.surf = pygame.Surface((75,25))
        self.surf.fill((255,255,255))
        self.rect = self.surf.get_rect(
            center = (
                (SCREEN_WIDTH/2),SCREEN_HEIGHT
            )
        )