import pygame
from PlayerPaddle import PlayerPaddle
from Block import Block
from Ball import Ball
from LevelRenderer import LevelRenderer

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
pygame.init()

LevelRenderer = LevelRenderer()

SCREEN_WIDTH = LevelRenderer.screen_width
SCREEN_HEIGHT = LevelRenderer.screen_height
INITIAL_COLOR = LevelRenderer.level_color

running = True
clock = pygame.time.Clock()

playerScore = 0
myfont = pygame.font.SysFont("Good Times Regular", 25, True)

screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

player = PlayerPaddle(SCREEN_WIDTH,SCREEN_HEIGHT)
playerGroup = pygame.sprite.GroupSingle(player)

blocks = LevelRenderer.blocks

ball = Ball()

all_sprites = pygame.sprite.Group()
all_sprites.add(player)
all_sprites.add(ball)
all_sprites.add(blocks)

while running:
    clock.tick(40)

    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
        elif event.type == QUIT:
            running = False

    player.update(pygame.key.get_pressed(), SCREEN_WIDTH)
    running = ball.update(SCREEN_WIDTH,SCREEN_HEIGHT)
    ## DRAW on screen 
    #in the loop and first or else objects will appear to grow
    screen.fill(INITIAL_COLOR)

    for object in all_sprites:
        screen.blit(object.surf, object.rect)

    score = myfont.render("Score: " + str(playerScore), 1, (255,255,0))
    screen.blit(score, (SCREEN_WIDTH-120, 25))

    #------------------paddle hit-----------------------------------------------
    if(pygame.sprite.spritecollide(ball, playerGroup, False)):
        ball.bounce("top_or_bottom")
    #---------------------------------------------------------------------------

    #------------------block hits-----------------------------------------------
    blocks_hit = pygame.sprite.spritecollide(ball, blocks, False)

    for block in blocks_hit:

        # keeping hit logic seperate for easier readability
        # -5 and +5 is for offset from imperfect pixel collision on rects
        # check velocity on top and bottom bounce eliminates sometimes registering top or bottom bounce when it should be side bounce
        
        # top bounce
        if(ball.rect.bottom-5 <= block.rect.top and ball.rect.top-5 <= block.rect.top
            and ball.velocity[1] >= 0):
            ball.bounce("top_or_bottom")
        # bottom bounce
        elif(ball.rect.bottom+5 >= block.rect.bottom and ball.rect.top+5 >= block.rect.bottom
            and ball.velocity[1] < 0):
            ball.bounce("top_or_bottom")

        # left bounce
        elif(ball.rect.left-5 <= block.rect.left and ball.rect.right-5 <= block.rect.left):
            ball.bounce("sides")

        # right bounce
        elif(ball.rect.left+5 >= block.rect.right and ball.rect.right+5 >= block.rect.right):
            ball.bounce("sides")

        playerScore += 10
        block.kill()
        break
    #------------------------------------------------------------------------------

    pygame.display.flip()

pygame.quit()