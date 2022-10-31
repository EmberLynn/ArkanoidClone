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
        self.surf = pygame.Surface((75,25))
        self.surf.fill((255,255,255))
        self.rect = self.surf.get_rect(
            center = (
                (screen_width/2),screen_height
            )
        )

    def update(self, pressed_keys):
        if pressed_keys[K_LEFT]:
            pygame.Rect.move_ip(self.rect,-5,0)
        if pressed_keys[K_RIGHT]:
            pygame.Rect.move_ip(self.rect,5,0)