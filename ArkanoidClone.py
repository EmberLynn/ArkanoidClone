import pygame
from PlayerPaddle import PlayerPaddle
from Block import Block
from Ball import Ball

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
block = Block(SCREEN_WIDTH,SCREEN_HEIGHT)
block2 = Block(SCREEN_WIDTH,SCREEN_HEIGHT)
ball = Ball()

while running:
    clock.tick(40)

    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
        elif event.type == QUIT:
            running = False

    player.update(pygame.key.get_pressed())
    ball.update()
    ## DRAW on screen 
    #in the loop and first or else objects will appear to grow
    screen.fill(INITIAL_COLOR)
    screen.blit(player.surf, player.rect)
    screen.blit(block.surf, block.rect)
    screen.blit(block2.surf, block2.rect)
    screen.blit(ball.surf, ball.rect)

    pygame.display.flip()

pygame.quit()