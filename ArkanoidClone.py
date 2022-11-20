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

pygame.display.set_caption("BARKanoid")
icon = pygame.image.load("Assests/singledog.png")
pygame.display.set_icon(icon)

LevelRenderer = LevelRenderer()

running = True
clock = pygame.time.Clock()

playerScore = 0
myfont = pygame.font.SysFont("Good Times Regular", 25, True)

level_finished = True

while running:

    clock.tick(40)

    # get the new/next level -- levels gets popped -- we don't keep finished levels---
    if(level_finished and LevelRenderer.levels):
        SCREEN_WIDTH = LevelRenderer.levels[0].screen_width
        SCREEN_HEIGHT = LevelRenderer.levels[0].screen_height
        INITIAL_COLOR = LevelRenderer.levels[0].level_color

        screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

        player = PlayerPaddle(SCREEN_WIDTH,SCREEN_HEIGHT)
        playerGroup = pygame.sprite.GroupSingle(player)

        blocks = LevelRenderer.levels[0].blocks

        ball = Ball(SCREEN_WIDTH,SCREEN_HEIGHT)

        all_sprites = pygame.sprite.Group()
        all_sprites.add(player)
        all_sprites.add(ball)
        all_sprites.add(blocks)

        level_finished = False

    elif not LevelRenderer.levels:
        print("Game is over when there are no levels left to render!")
        quit()
    # --------------------------------------------------------------------------------

    # start the game logic after the level has rendered--------------------------------
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
        if(ball.rect.bottom-5 <= player.rect.top and ball.rect.top-5 <= player.rect.top
            and ball.velocity[1] >= 0):
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

    if not blocks:
        LevelRenderer.levels.pop(0)
        level_finished = True

    pygame.display.flip()

    # always check for exit events before continuing the loop    
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
        elif event.type == QUIT:
            running = False

pygame.quit()