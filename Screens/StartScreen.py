import pygame
from Screens.BaseScreen import BaseScreen
from Utilities.Button import Button

# StartScreen contains:
# size
# colour
# game name (title)
# clickable start button
# options (TBD)
# scores (TBD)
# version number in top left

VERSION_NUM = "0.1.3"

SCREEN_HEIGHT = 600
SCREEN_WIDTH = 900
SCREEN_COLOR = ((0, 153, 77))

class StartScreen(BaseScreen):
    def __init__(self):
        super().__init__() 

        buttonfont = pygame.font.SysFont("Good Times Regular", 30, False)
        titlefont = pygame.font.SysFont("Good Times Regular", 50, False)
        tinyfont = pygame.font.SysFont("Good Times Regular", 20, False)

        # screen size
        self.screen_height = SCREEN_HEIGHT
        self.screen_width = SCREEN_WIDTH

        # screen text
        self.title = titlefont.render("BARKanoid!",1,(0,0,0))
        self.version_num = tinyfont.render("Version: " + str(VERSION_NUM),1,(0,0,0))

        # start button
        start_button = Button(200, 60, ((SCREEN_WIDTH/2),(SCREEN_HEIGHT/2)), (77, 148, 255), "Start Game", (0,0,0), buttonfont, "start")
        self.button_list.append(start_button)

        # view high scores button
        high_score_button = Button(200, 60, ((SCREEN_WIDTH/2),(SCREEN_HEIGHT/2)+70), (77, 148, 255), "High Scores", (0,0,0), buttonfont, "highscores")
        self.button_list.append(high_score_button)

        # options button
        options_button = Button(200, 60, ((SCREEN_WIDTH/2),(SCREEN_HEIGHT/2)+140), (77, 148, 255), "Options", (0,0,0), buttonfont, "options")
        self.button_list.append(options_button)

        # quit button
        quit_button = Button(200, 60, ((SCREEN_WIDTH/2),(SCREEN_HEIGHT/2)+210), (77, 148, 255), "Quit Game", (0,0,0), buttonfont, "quit")
        self.button_list.append(quit_button)

    def update(self):
        self.screen.fill(SCREEN_COLOR)
        # draw title on screen
        title_text_rect = self.title.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT-570))
        self.screen.blit(self.title, title_text_rect)

        self.draw_buttons()
        
        # version number
        version_num_text_rect = self.version_num.get_rect(center=(SCREEN_WIDTH-50,SCREEN_HEIGHT-10))
        self.screen.blit(self.version_num, version_num_text_rect)