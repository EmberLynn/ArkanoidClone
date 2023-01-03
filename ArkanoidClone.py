import sys

# C:\Users\ember\OneDrive\Desktop\Projects\PyGame\ArkanoidClone\Screens
# this is gross and I dislike it. Look into something better...
sys.path.insert(0,'/Users/ember/OneDrive/Desktop/Projects/PyGame/ArkanoidClone/Screens')

import pygame
from PlayerPaddle import PlayerPaddle
from Block import Block
from Ball import Ball
from LevelRenderer import LevelRenderer
from Screens.StartScreen import StartScreen

from pygame.locals import (
    RLEACCEL,
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    MOUSEBUTTONDOWN,
    QUIT
)
pygame.init()

pygame.display.set_caption("BARKanoid")
icon = pygame.image.load("Assests/singledog.png")
pygame.display.set_icon(icon)

levelRenderer = LevelRenderer()

runningStart = True
runningMain = False
runningGameOver = False
clock = pygame.time.Clock()

playerScore = 0
myfont = pygame.font.SysFont("Good Times Regular", 25, True)

level_finished = True
# startscreen_loaded = False -- can we only draw the screen when needed?

# ----------Start Screen Loop-------------
while runningStart:
    startScreen = StartScreen()
    startScreen.draw()
    pygame.display.flip()

    # always check for exit events before continuing the loop    
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                runningStart = False
        elif event.type == QUIT:
            runningStart = False
        elif event.type == MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed(num_buttons=3) == (1,0,0):
                if startScreen.check_mouse_click() == "start_button":
                    runningStart = False
                    runningMain = True
# ----------END of Start Screen Loop-------------

# ----------Main Game Loop-------------
while runningMain:

    clock.tick(40)

    # get the new/next level -- levels gets popped -- we don't keep finished levels---
    if(level_finished and levelRenderer.levels):
        SCREEN_WIDTH = levelRenderer.levels[0].get_screen_width()
        SCREEN_HEIGHT = levelRenderer.levels[0].get_screen_height()
        INITIAL_COLOR = levelRenderer.levels[0].get_level_color()

        screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

        player = PlayerPaddle(SCREEN_WIDTH,SCREEN_HEIGHT)
        playerGroup = pygame.sprite.GroupSingle(player)

        blocks = levelRenderer.levels[0].blocks

        ball = Ball(SCREEN_WIDTH,SCREEN_HEIGHT)

        all_sprites = pygame.sprite.Group()
        all_sprites.add(player)
        all_sprites.add(ball)
        all_sprites.add(blocks)

        level_finished = False

    elif not levelRenderer.levels:
        print("Game is over when there are no levels left to render!")
        runningGameOver = True
        runningMain = False
        break
    # --------------------------------------------------------------------------------

    # start the game logic after the level has rendered--------------------------------
    player.update(pygame.key.get_pressed(), SCREEN_WIDTH)
    
    if ball.update(SCREEN_WIDTH,SCREEN_HEIGHT) == False:
        runningMain = False
        runningGameOver = True
        break

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
        levelRenderer.levels.pop(0)
        level_finished = True

    pygame.display.flip()

    # always check for exit events before continuing the loop    
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                runningMain = False
        elif event.type == QUIT:
            runningMain = False

# ----------END of Main Game Loop-------------

# ----------Game Over Loop-------------
while runningGameOver:
    print("Game Over!")
    runningGameOver = False
# ---------- END of Game Over Loop-------------

pygame.quit()