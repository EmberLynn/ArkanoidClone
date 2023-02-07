import pygame
from Screens.BaseScreen import BaseScreen
from Utilities.Button import Button

# ContinueScreen contains:
# size
# colour
# Completion Message (title)
# clickable Continue button
# displays current score

SCREEN_HEIGHT = 600
SCREEN_WIDTH = 900
SCREEN_COLOR = ((0, 153, 77))

class ContinueScreen(BaseScreen):
    def __init__(self):
        super().__init__()

        buttonfont = pygame.font.SysFont("Good Times Regular", 30, False)

        # create buttons
        self.button_list = []

        # continue button
        continue_button = Button(200, 60, ((SCREEN_WIDTH/2),(SCREEN_HEIGHT/2)), (77, 148, 255), "Continue?", (0,0,0), buttonfont)
        self.button_list.append(continue_button)

    def draw(self, display_flags, level_num, player_score):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT), display_flags)
        self.screen.fill(SCREEN_COLOR)

        # draw title on screen
        # font is created here for rendering level number dynamically
        titlefont = pygame.font.SysFont("Good Times Regular", 50, False)
        title_text = titlefont.render("Level " + str(level_num) + " Complete!",1,(0,0,0))
        title_text_rect = title_text.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT-570))
        self.screen.blit(title_text, title_text_rect)

        # draw current score on screen
        scorefont = pygame.font.SysFont("Good Times Regular", 40, False)
        score_text = scorefont.render("Current Score: " + str(player_score), 1, (255,255,0))
        finalscore_text_rect = score_text.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT-500))
        self.screen.blit(score_text, finalscore_text_rect)

        self.draw_buttons()
