import pygame
from Screens.BaseScreen import BaseScreen
from Utilities.Button import Button
import random

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
        continue_button = Button(200, 60, ((SCREEN_WIDTH/2),(SCREEN_HEIGHT/2)+100), (77, 148, 255), "Continue?", (0,0,0), buttonfont)
        self.button_list.append(continue_button)

    def draw(self, display_flags, level_num, player_score, boon_handler):
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

        # loop through all possible boons and offer the player a boon they don't have
        for boon in boon_handler.boons:
            # if the boon hasn't been selected before
            if boon.get_active() == False:
                boon_description = boon.get_description()
                boon_name = boon.get_name()
                break # only want ONE boon

        # draw boon name on screen
        boon_text = titlefont.render(boon_description, 1,(0,0,0))
        boon_text_rect = boon_text.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT-450))
        self.screen.blit(boon_text, boon_text_rect)

        self.draw_buttons()

        return boon_name