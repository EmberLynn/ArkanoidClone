import pygame
from Screens.BaseScreen import BaseScreen

# ContinueScreen contains:
# size
# colour
# Completion Message (title)
# clickable Continue button
# displays current score

SCREEN_HEIGHT = 600
SCREEN_WIDTH = 900
SCREEN_COLOR = ((0, 153, 77))

# button location and sizes
# continue button
CONTINUE_BUTTON_LEFT = ((SCREEN_WIDTH/2)-100)
CONTINUE_BUTTON_TOP = (SCREEN_HEIGHT/2)
CONTINUE_BUTTON_RIGHT = CONTINUE_BUTTON_LEFT + 200
CONTINUE_BUTTON_BOTTOM = CONTINUE_BUTTON_TOP + 60

class ContinueScreen(BaseScreen):
    def __init__(self):
        super().__init__()

        buttonfont = pygame.font.SysFont("Good Times Regular", 30, False)

        # basic info -- doubling up here; might want to change later
        self.set_screen_height(SCREEN_HEIGHT)
        self.set_screen_width(SCREEN_WIDTH)
        self.set_level_color((SCREEN_COLOR))

        # screen text
        self.continue_button_text = buttonfont.render("Continue?",1,(0,0,0))

        # position of continue button
        self.continue_button_dimensions = (CONTINUE_BUTTON_LEFT,CONTINUE_BUTTON_TOP,200,60)

    def draw(self, level_num, player_score):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
        self.screen.fill(SCREEN_COLOR)

        # draw title on screen
        titlefont = pygame.font.SysFont("Good Times Regular", 50, False)
        title_text = titlefont.render("Level " + str(level_num) + " Complete!",1,(0,0,0))
        title_text_rect = title_text.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT-570))
        self.screen.blit(title_text, title_text_rect)

        # draw current score on screen
        scorefont = pygame.font.SysFont("Good Times Regular", 40, False)
        score_text = scorefont.render("Current Score: " + str(player_score), 1, (255,255,0))
        finalscore_text_rect = score_text.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT-500))
        self.screen.blit(score_text, finalscore_text_rect)

        # continue button
        pygame.draw.rect(self.screen,(77, 148, 255),self.continue_button_dimensions)
        continue_text_rect = self.continue_button_text.get_rect(center=(CONTINUE_BUTTON_LEFT+100, CONTINUE_BUTTON_TOP+30))
        self.screen.blit(self.continue_button_text, continue_text_rect)

    def check_mouse_click(self):

        mouse_x = pygame.mouse.get_pos()[0]
        mouse_y = pygame.mouse.get_pos()[1]

        if(mouse_x >= CONTINUE_BUTTON_LEFT 
            and mouse_x <= CONTINUE_BUTTON_RIGHT 
            and mouse_y >= CONTINUE_BUTTON_TOP 
            and mouse_y <= CONTINUE_BUTTON_BOTTOM):
            return "continue_button"
