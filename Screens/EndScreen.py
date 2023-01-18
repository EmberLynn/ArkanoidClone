import os
import pygame
from Screens.BaseScreen import BaseScreen
from Utilities.Button import Button

# StartScreen contains:
# size
# colour
# game over (title)
# displays final score
# clickable restart button
# clickable quit button
# clickable start screen button

SCREEN_HEIGHT = 600
SCREEN_WIDTH = 900
SCREEN_COLOR = ((0, 153, 77))

class EndScreen(BaseScreen):
    def __init__(self):
        super().__init__()

        buttonfont = pygame.font.SysFont("Good Times Regular", 30, False)
        titlefont = pygame.font.SysFont("Good Times Regular", 50, False)

        # screen text
        self.title = titlefont.render("Game Over!",1,(0,0,0))
        self.quit_button_text = buttonfont.render("Quit",1,(0,0,0))

        # start button
        start_button = Button(200, 60, ((SCREEN_WIDTH/2),(SCREEN_HEIGHT/2)), (77, 148, 255), "Restart Game", (0,0,0), buttonfont)
        self.button_list.append(start_button)

        # return to menu button
        menu_button = Button(200, 60, ((SCREEN_WIDTH/2),(SCREEN_HEIGHT/2)+100), (77, 148, 255), "Main Menu", (0,0,0), buttonfont)
        self.button_list.append(menu_button)

        # quit button
        quit_button = Button(200, 60, ((SCREEN_WIDTH/2),(SCREEN_HEIGHT/2)+200), (77, 148, 255), "Quit Game", (0,0,0), buttonfont)
        self.button_list.append(quit_button)

    def draw(self, player_score):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
        self.screen.fill(SCREEN_COLOR)

        # draw title on screen
        title_text_rect = self.title.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT-570))
        self.screen.blit(self.title, title_text_rect)

        # draw final score on screen
        scorefont = pygame.font.SysFont("Good Times Regular", 40, False)
        final_score_text = scorefont.render("Final Score: " + str(player_score), 1, (255,255,0))
        finalscore_text_rect = final_score_text.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT-500))
        self.screen.blit(final_score_text, finalscore_text_rect)

        self.draw_buttons()

    # needs high score list and current score
    def check_for_high_score(self, current_score):

        high_score_list = self.get_high_scores()

        # take each item, split it on the ':', make a collection of tuples,
        # sort lowest to highest, remove lowest score from list, save list of scores
        # to the high_scores.txt


