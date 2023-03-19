import sys
import pygame
import random
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
from Utilities.MainGame import MainGame

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
main = True
new_game = True

# music and effects
pygame.mixer.init()
pygame.mixer.music.load("Assests/vastness.mp3")
pygame.mixer.music.play(-1)

# main game class
mg = MainGame()

# ------------------------  helper functions -----------------------------------
# ------------------------------------------------------------------------------
def check_for_quit(event):
    if event.type == KEYDOWN:
        if event.key == K_ESCAPE:
            pygame.quit()
            sys.exit()
    elif event.type == QUIT:
        pygame.quit()
        sys.exit()

# takes a button action and preforms it -- all button actions must be implemented here
def call_button_function(action):
    mg.currentScreen = None
    match action:
        case "start": # starts the game
            mg.runningStart = False
            mg.runningMain = True
        case "main": # goes to main screen -- start screen
            mg.runningStart = True
            mg.runningMain = False
        case "highscores":
            run_high_score_screen()
        case "options":
            run_options_screen()
        case "quit":
            pygame.quit()
            sys.exit()

        # option functions
        case "music_on":
            pygame.mixer.music.play(-1)
        case "music_off":
            pygame.mixer.music.stop()

def run_high_score_screen():
    runningHighScore = True
    while runningHighScore:

        if mg.currentScreen is None:
            mg.currentScreen = HighScoreScreen()
            mg.currentScreen.draw()
        mg.currentScreen.update()

        for event in pygame.event.get():
            check_for_quit(event)
            if event.type == MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed(num_buttons=3) == (1,0,0):
                    for button in mg.currentScreen.button_list:
                        if pygame.Rect.collidepoint(button.rect, pygame.mouse.get_pos()):
                            # get button action and call required method
                            call_button_function(button.button_action)
                            break
                    runningHighScore = False

        pygame.display.flip()

def run_options_screen():
    runningOptions = True
    while runningOptions:

        if mg.currentScreen is None:
            mg.currentScreen = OptionsScreen()
            mg.currentScreen.draw()
        mg.currentScreen.update()

        for event in pygame.event.get():
            check_for_quit(event)
            if event.type == MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed(num_buttons=3) == (1,0,0):
                    for button in mg.currentScreen.button_list:
                        if pygame.Rect.collidepoint(button.rect, pygame.mouse.get_pos()):
                            # get button action and call required method
                            call_button_function(button.button_action)
                            break
                    runningOptions = False

        pygame.display.flip()        

def run_continue_screen():
    runningContinue = True
    while runningContinue:

        if mg.currentScreen is None:
            mg.currentScreen = ContinueScreen()
            mg.currentScreen.draw()
            boon_number = random.randint(0,len(mg.boonHandler.boons)-1)
        boon_name = mg.currentScreen.update(mg.currentLevel, mg.playerScore, mg.boonHandler, boon_number)

        for event in pygame.event.get():
            check_for_quit(event)
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    result = mg.currentScreen.check_mouse_click()
                    if result == "Continue?":
                        mg.boonHandler.handle_boon(boon_name)
                        runningContinue = False
                        mg.currentScreen = None

        pygame.display.flip()

# -----------------------------------------------------------------------------
# ------------------------ end of helper functions ----------------------------

# ------------------------------  main game logic
while main:

    mg.currentScreen = None

    runningGameOver = False

    levelRenderer = LevelRenderer()

    # main sprites
    player = PlayerPaddle() 
    playerGroup = pygame.sprite.GroupSingle(player)

    ballGroup = pygame.sprite.Group()
    ball = Ball()
    ballGroup.add(ball)

    mg.boonHandler = BoonHandler(player,ballGroup)

    clock = pygame.time.Clock()

    mg.playerScore = 0
    displayScore = 0
    myfont = pygame.font.SysFont("Good Times Regular", 25, True)

    level_finished = True
    mg.currentLevel = 0

    # ----------START of Start Screen Loop-------------
    while mg.runningStart:

        if mg.currentScreen is None:
            mg.currentScreen = StartScreen()
            mg.currentScreen.draw()
        mg.currentScreen.update()

        # always check for exit events before continuing the loop    
        for event in pygame.event.get():
            check_for_quit(event)
            if event.type == MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed(num_buttons=3) == (1,0,0):
                    for button in mg.currentScreen.button_list:
                        if pygame.Rect.collidepoint(button.rect, pygame.mouse.get_pos()):
                            # get button action and call required method
                            call_button_function(button.button_action)
                            break
        pygame.display.flip()

    # ----------END of Start Screen Loop-------------

    # ----------START of Main Game Loop-------------
    while mg.runningMain:

        clock.tick(60)

        # always check for exit events before continuing the loop    
        for event in pygame.event.get():
            check_for_quit(event)

        # get the new/next level -- levels gets popped -- we don't keep finished levels---
        for level in levelRenderer.levels:
            if level_finished:
                mg.currentLevel += 1
                current_difficulty = level.get_difficulty()

                SCREEN_WIDTH = level.get_screen_width()
                SCREEN_HEIGHT = level.get_screen_height()
                INITIAL_COLOR = level.get_level_color()

                screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
                print("Drawing main screen!")

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
            displayScore = mg.playerScore
            runningGameOver = True
            mg.runningMain = False
            break
        # --------------------------------------------------------------------------------

        # start the game logic after the level has rendered--------------------------------
        player.update(pygame.key.get_pressed(), SCREEN_WIDTH)

        for ball in ballGroup:
            endGame = ball.update(SCREEN_WIDTH,SCREEN_HEIGHT)
            if endGame == False and len(ballGroup) == 0:
                displayScore = mg.playerScore
                mg.runningMain = False
                runningGameOver = True
                break
        
        ## DRAW on screen 
        #in the loop and first or else objects will appear to grow
        screen.fill(INITIAL_COLOR)

        for block in blocks:
            block.draw(screen, current_difficulty)

        for object in all_sprites:
            screen.blit(object.surf, object.rect)

        score = myfont.render("Score: " + str(mg.playerScore), 1, (255,255,0))
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

                mg.playerScore += 10
                block.block_hit(screen)
                break
        #------------------------------------------------------------------------------

        if not blocks:
            levelRenderer.levels.pop(0)
            level_finished = True

            # ----------START of Continue Loop-------------
            if(len(levelRenderer.levels) > 0):
                run_continue_screen()
            # ----------END of Continue Loop-------------

        pygame.display.flip()

    # ----------END of Main Game Loop-------------

    # ----------START of Game Over Loop-------------
    while runningGameOver:

        if mg.currentScreen is None:
            mg.currentScreen = EndScreen()
            mg.currentScreen.draw()
        mg.currentScreen.update(mg.playerScore)

        # ----------START of Enter High Score Loop-------------
        is_highscore = mg.currentScreen.check_for_high_score(displayScore)
        if(is_highscore):
            runningEnterHighScore = True
            while runningEnterHighScore:
                    
                for event in pygame.event.get():
                    check_for_quit(event)

                player_name = mg.currentScreen.draw_high_score_popup()
                mg.currentScreen.save_high_score(player_name, mg.playerScore)
                displayScore = 0

                runningEnterHighScore = False
        # ----------START of Enter High Score Loop-------------

        for event in pygame.event.get():
                check_for_quit(event)
                if event.type == MOUSEBUTTONDOWN:
                    if pygame.mouse.get_pressed(num_buttons=3) == (1,0,0):
                        for button in mg.currentScreen.button_list:
                            if pygame.Rect.collidepoint(button.rect, pygame.mouse.get_pos()):
                                # get button action and call required method
                                call_button_function(button.button_action)
                                break
                        runningGameOver = False

        pygame.display.flip()
    # ----------END of Game Over Loop-------------

pygame.quit()
sys.exit()
