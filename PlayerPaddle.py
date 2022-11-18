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

    def __init__(self, screen_width, screen_height):
        super(PlayerPaddle, self).__init__()
        self.surf = pygame.Surface((75,5))
        self.surf.fill((255,255,255))
        self.rect = self.surf.get_rect(
            center = (
                (screen_width/2),(screen_height-20)
            )
        )
        self.paddlespeed = 10 # starting speed of paddle

    def update(self, pressed_keys, screen_width):
        if(self.rect.left > 0):
            if pressed_keys[K_LEFT]:
                pygame.Rect.move_ip(self.rect,-self.paddlespeed,0)
        if(self.rect.right <= screen_width):
            if pressed_keys[K_RIGHT]:
                pygame.Rect.move_ip(self.rect,self.paddlespeed,0)