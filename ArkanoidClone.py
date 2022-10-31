import pygame
from PlayerPaddle import PlayerPaddle

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

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
INITIAL_COLOR = (0, 102, 34)

running = True
clock = pygame.time.Clock()

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

player = PlayerPaddle(SCREEN_WIDTH,SCREEN_HEIGHT)

while running:
    clock.tick(40)

    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
        elif event.type == QUIT:
            running = False

    player.update(pygame.key.get_pressed())

    ## DRAW on screen 
    #in the loop and first or else objects will appear to grow
    screen.fill(INITIAL_COLOR)
    screen.blit(player.surf, player.rect)

    pygame.display.flip()

pygame.quit()