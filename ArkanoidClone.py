import sys
import pygame
from Sprites.PlayerPaddle import PlayerPaddle
from Sprites.Block import Block
from Sprites.Ball import Ball
from Levels.LevelRenderer import LevelRenderer
from Screens.StartScreen import StartScreen
from Screens.EndScreen import EndScreen
from Screens.ContinueScreen import ContinueScreen
from Screens.HighScoreScreen import HighScoreScreen

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

def main(new_game):

    if(new_game):
        runningStart = True
        runningMain = False
    else:
        runningStart = False
        runningMain = True

    runningGameOver = False

    levelRenderer = LevelRenderer()

    clock = pygame.time.Clock()

    playerScore = 0
    myfont = pygame.font.SysFont("Good Times Regular", 25, True)

    level_finished = True
    currentLevel = 0

    # ----------START of Start Screen Loop-------------
    while runningStart:
        startScreen = StartScreen()
        startScreen.draw()
        pygame.display.flip()

        # always check for exit events before continuing the loop    
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            elif event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed(num_buttons=3) == (1,0,0):
                    result = startScreen.check_mouse_click()
                    if result == "Start Game":
                        runningStart = False
                        runningMain = True
                    elif result == "Quit Game":
                        runningStart = False
                    elif result == "High Scores":
                        # ----------START of High Score Screen Loop-------------
                        runningHighScore = True
                        while runningHighScore:
                            highScoreScreen = HighScoreScreen()
                            highScoreScreen.draw()
                            pygame.display.flip()

                            for event in pygame.event.get():
                                if event.type == KEYDOWN:
                                    if event.key == K_ESCAPE:
                                        pygame.quit()
                                        sys.exit()
                                elif event.type == QUIT:
                                    pygame.quit()
                                    sys.exit()
                                elif pygame.mouse.get_pressed(num_buttons=3) == (1,0,0):
                                    result = highScoreScreen.check_mouse_click()
                                    if result == "Main Menu":
                                        runningHighScore = False
            # ----------END of High Score Loop-------------
                    elif result == "Options":
            # ----------START of Options Loop-------------
                        runningOptions = True
                        while runningOptions:
                            runningOptions = False
                            print("To be implemented")
            # ----------END of Options Loop-------------

    # ----------END of Start Screen Loop-------------

    # ----------START of Main Game Loop-------------
    while runningMain:

        clock.tick(40)

        # always check for exit events before continuing the loop    
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            elif event.type == QUIT:
                pygame.quit()
                sys.exit()

        # get the new/next level -- levels gets popped -- we don't keep finished levels---
        for level in levelRenderer.levels:
            if(level_finished):
                currentLevel += 1
                SCREEN_WIDTH = level.get_screen_width()
                SCREEN_HEIGHT = level.get_screen_height()
                INITIAL_COLOR = level.get_level_color()

                screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

                player = PlayerPaddle(SCREEN_WIDTH,SCREEN_HEIGHT)
                playerGroup = pygame.sprite.GroupSingle(player)

                blocks = level.blocks

                ball = Ball(SCREEN_WIDTH,SCREEN_HEIGHT)

                all_sprites = pygame.sprite.Group()
                all_sprites.add(player)
                all_sprites.add(ball)
                all_sprites.add(blocks)

                level_finished = False
            break

        if not levelRenderer.levels:
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
        if pygame.sprite.spritecollide(ball, playerGroup, False):
            if(ball.rect.bottom-5 <= player.rect.top 
                and ball.rect.top-5 <= player.rect.top
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
            if(ball.rect.bottom-5 <= block.rect.top 
                and ball.rect.top-5 <= block.rect.top
                and ball.velocity[1] >= 0):
                ball.bounce("top_or_bottom")
            # bottom bounce
            elif(ball.rect.bottom+5 >= block.rect.bottom 
                and ball.rect.top+5 >= block.rect.bottom
                and ball.velocity[1] < 0):
                ball.bounce("top_or_bottom")

            # left bounce
            elif(ball.rect.left-5 <= block.rect.left
                and ball.rect.right-5 <= block.rect.left):
                ball.bounce("sides")

            # right bounce
            elif(ball.rect.left+5 >= block.rect.right 
                and ball.rect.right+5 >= block.rect.right):
                ball.bounce("sides")

            playerScore += 10
            block.kill()
            break
        #------------------------------------------------------------------------------

        if not blocks:
            levelRenderer.levels.pop(0)
            level_finished = True

            # ----------START of Continue Loop-------------
            if(len(levelRenderer.levels) > 0):
                runningContinue = True
                while runningContinue:
                    continueScreen = ContinueScreen()
                    continueScreen.draw(currentLevel, playerScore)
                    pygame.display.flip()

                    for event in pygame.event.get():
                        if event.type == KEYDOWN:
                            if event.key == K_ESCAPE:
                                pygame.quit()
                                sys.exit()
                        elif event.type == QUIT:
                            pygame.quit()
                            sys.exit()
                        elif pygame.mouse.get_pressed(num_buttons=3) == (1,0,0):
                            result = continueScreen.check_mouse_click()
                            if result == "Continue?":
                                runningContinue = False
            # ----------END of Continue Loop-------------

        pygame.display.flip()

    # ----------END of Main Game Loop-------------

    # ----------START of Game Over Loop-------------
    while runningGameOver:
        endScreen = EndScreen()
        endScreen.draw(playerScore)
        pygame.display.flip()

        for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        pygame.quit()
                        sys.exit()
                elif event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                elif pygame.mouse.get_pressed(num_buttons=3) == (1,0,0):
                    result = endScreen.check_mouse_click()
                    if result == "Restart Game":
                        # start new game from main
                        runningGameOver = False
                        main(False)
                    elif result == "Main Menu":
                        
                        endScreen.check_for_high_score(current_score=9)
                        runningGameOver = False
                        main(True)
                    elif result == "Quit Game":
                        pygame.quit()
                        sys.exit()
    # ----------END of Game Over Loop-------------

main(True)
# pygame.quit()
# sys.exit()