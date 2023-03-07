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
    def __init__(self):
        super(PlayerPaddle, self).__init__()

        self.paddle_length = 75

        self.surf = pygame.Surface((self.paddle_length,9))
        self.surf.fill((102, 102, 102))
        self.rect = self.surf.get_rect()

        self.paddlespeed = 5 # starting speed of paddle

        pygame.draw.rect(self.surf, (0,0,0),(0,0,self.paddle_length-2,7))
        pygame.draw.rect(self.surf, (255,255,255),(0,0,self.paddle_length-4,5))

    def update(self, pressed_keys, screen_width):
        if(self.rect.left > 0):
            if pressed_keys[K_LEFT]:
                pygame.Rect.move_ip(self.rect,-self.paddlespeed,0)
        if(self.rect.right <= screen_width):
            if pressed_keys[K_RIGHT]:
                pygame.Rect.move_ip(self.rect,self.paddlespeed,0)

    def redraw_paddle(self):
        self.surf = pygame.Surface((self.paddle_length,9))
        self.surf.fill((102, 102, 102))
        self.rect = self.surf.get_rect()

        pygame.draw.rect(self.surf, (0,0,0),(0,0,self.paddle_length-2,7))
        pygame.draw.rect(self.surf, (255,255,255),(0,0,self.paddle_length-4,5))