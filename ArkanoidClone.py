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
from Screens.OptionsScreen import OptionsScreen

from Utilities.BoonHandler import BoonHandler

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

# required setup before rendering
pygame.init()
pygame.display.set_caption("BARKanoid")
icon = pygame.image.load("Assests/singledog.png")
pygame.display.set_icon(icon)
display_flags = pygame.NOFRAME

# helper functions
def check_for_quit(event):
    if event.type == KEYDOWN:
        if event.key == K_ESCAPE:
            pygame.quit()
            sys.exit()
    elif event.type == QUIT:
        pygame.quit()
        sys.exit()

# main game logic
def main(new_game):
    global display_flags

    if(new_game):
        runningStart = True
        runningMain = False
    else:
        runningStart = False
        runningMain = True

    runningGameOver = False

    levelRenderer = LevelRenderer()

    # main sprites
    player = PlayerPaddle() 
    playerGroup = pygame.sprite.GroupSingle(player)

    ballGroup = pygame.sprite.Group()
    ball = Ball()
    ballGroup.add(ball)

    boonHandler = BoonHandler(player,ballGroup)

    clock = pygame.time.Clock()

    playerScore = 0
    displayScore = 0
    myfont = pygame.font.SysFont("Good Times Regular", 25, True)

    level_finished = True
    currentLevel = 0

    # ----------START of Start Screen Loop-------------
    while runningStart:
        startScreen = StartScreen()
        startScreen.draw(display_flags)
        pygame.display.flip()

        # always check for exit events before continuing the loop    
        for event in pygame.event.get():
            check_for_quit(event)
            if event.type == MOUSEBUTTONDOWN:
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
                            highScoreScreen.draw(display_flags)
                            pygame.display.flip()

                            for event in pygame.event.get():
                                check_for_quit(event)
                                if pygame.mouse.get_pressed(num_buttons=3) == (1,0,0):
                                    result = highScoreScreen.check_mouse_click()
                                    if result == "Main Menu":
                                        runningHighScore = False
                        # ----------END of High Score Loop-------------

                    elif result == "Options":
                        # ----------START of Options Loop-------------
                        runningOptions = True
                        optionsScreen = OptionsScreen()
                        while runningOptions:
                            optionsScreen.draw(display_flags)
                            pygame.display.flip()
                            # runningOptions = False
                            for event in pygame.event.get():
                                check_for_quit(event)
                                if pygame.mouse.get_pressed(num_buttons=3) == (1,0,0):
                                    result = optionsScreen.check_mouse_click()
                                    if result == "Main Menu":
                                        runningOptions = False
                                    elif result == "ON":
                                        display_flags = 0
                                    elif result == "OFF":
                                        display_flags = pygame.NOFRAME
                        # ----------END of Options Loop-------------

    # ----------END of Start Screen Loop-------------

    # ----------START of Main Game Loop-------------
    while runningMain:

        clock.tick(40)

        # always check for exit events before continuing the loop    
        for event in pygame.event.get():
            check_for_quit(event)

        # get the new/next level -- levels gets popped -- we don't keep finished levels---
        for level in levelRenderer.levels:
            if level_finished:
                currentLevel += 1
                current_difficulty = level.get_difficulty()

                SCREEN_WIDTH = level.get_screen_width()
                SCREEN_HEIGHT = level.get_screen_height()
                INITIAL_COLOR = level.get_level_color()

                screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT), display_flags)

                all_sprites = pygame.sprite.Group()

                # set balls
                for ball in ballGroup:
                    ball.rect.x = (SCREEN_WIDTH/2)
                    ball.rect.y = (SCREEN_HEIGHT-45)
                    all_sprites.add(ball)

                # set paddle
                player.rect.x = ((SCREEN_WIDTH/2)-25)
                player.rect.y = (SCREEN_HEIGHT-20)
                all_sprites.add(player)

                # create function that applies block boons
                blocks = level.blocks


                level_finished = False
            break

        if not levelRenderer.levels:
            displayScore = playerScore
            runningGameOver = True
            runningMain = False
            break
        # --------------------------------------------------------------------------------

        # start the game logic after the level has rendered--------------------------------
        player.update(pygame.key.get_pressed(), SCREEN_WIDTH)

        for ball in ballGroup:
            endGame = ball.update(SCREEN_WIDTH,SCREEN_HEIGHT)
            if endGame == False and len(ballGroup) == 0:
                displayScore = playerScore
                runningMain = False
                runningGameOver = True
                break
        
        ## DRAW on screen 
        #in the loop and first or else objects will appear to grow
        screen.fill(INITIAL_COLOR)

        for block in blocks:
            block.draw(screen, current_difficulty)

        for object in all_sprites:
            screen.blit(object.surf, object.rect)

        score = myfont.render("Score: " + str(playerScore), 1, (255,255,0))
        screen.blit(score, (SCREEN_WIDTH-120, 25))

        #------------------paddle hit-----------------------------------------------
        for ball in ballGroup:
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
                block.block_hit(screen)
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
                    boon_name = continueScreen.draw(display_flags, currentLevel, playerScore, boonHandler)
                    pygame.display.flip()

                    for event in pygame.event.get():
                        check_for_quit(event)
                        if event.type == MOUSEBUTTONDOWN:
                            if event.button == 1:
                                result = continueScreen.check_mouse_click()
                                if result == "Continue?":
                                    boonHandler.handle_boon(boon_name)
                                    runningContinue = False
            # ----------END of Continue Loop-------------

        pygame.display.flip()

    # ----------END of Main Game Loop-------------

    # ----------START of Game Over Loop-------------
    while runningGameOver:
        endScreen = EndScreen()
        endScreen.draw(display_flags, playerScore)
        pygame.display.flip()

        # ----------START of Enter High Score Loop-------------
        is_highscore = endScreen.check_for_high_score(displayScore)
        if(is_highscore):
            runningEnterHighScore = True
            while runningEnterHighScore:
                
                    for event in pygame.event.get():
                        check_for_quit(event)

                    player_name = endScreen.draw_high_score_popup()
                    endScreen.save_high_score(player_name, playerScore)
                    displayScore = 0

                    runningEnterHighScore = False
        # ----------START of Enter High Score Loop-------------

        for event in pygame.event.get():
                check_for_quit(event)
                if pygame.mouse.get_pressed(num_buttons=3) == (1,0,0):
                    result = endScreen.check_mouse_click()
                    if result == "Restart Game":
                        # start new game from main
                        runningGameOver = False
                        main(False)
                    elif result == "Main Menu":
                        runningGameOver = False
                        main(True)
                    elif result == "Quit Game":
                        pygame.quit()
                        sys.exit()
    # ----------END of Game Over Loop-------------

main(True)
# pygame.quit()
# sys.exit()
