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

        # basic info -- doubling up here; might want to change later
        self.set_screen_height(SCREEN_HEIGHT)
        self.set_screen_width(SCREEN_WIDTH)
        self.set_level_color((SCREEN_COLOR))

        # create buttons
        self.button_list = []

        # continue button
        continue_button = Button(200, 60, ((SCREEN_WIDTH/2),(SCREEN_HEIGHT/2)), (77, 148, 255), "Continue?", (0,0,0), buttonfont)
        self.button_list.append(continue_button)

    def draw(self, level_num, player_score):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
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

        # draw buttons
        for button in self.button_list:
            pygame.draw.rect(self.screen, button.button_colour, button.button_dimensions)
            self.screen.blit(button.button_text, button.button_text_rect)

    def check_mouse_click(self):

        mouse_x = pygame.mouse.get_pos()[0]
        mouse_y = pygame.mouse.get_pos()[1]

        for button in self.button_list:
            if button.clicked(mouse_x, mouse_y):
                return button.label_text
