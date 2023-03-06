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

class OptionsScreen(BaseScreen):
    def __init__(self):
        super().__init__()

        # going to use button font for options font, too
        buttonfont = pygame.font.SysFont("Good Times Regular", 30, False)
        titlefont = pygame.font.SysFont("Good Times Regular", 50, False)

        # screen size
        self.screen_height = SCREEN_HEIGHT
        self.screen_width = SCREEN_WIDTH

        # screen text
        self.title = titlefont.render("Options",1,(0,0,0))
        self.option_1 = buttonfont.render("Toggle Game Music",1,(0,0,0))

        # create button list
        self.button_list = []

        # option 1 on button
        self.option1_on_button = Button(100, 60, ((SCREEN_WIDTH/2)+100, (SCREEN_HEIGHT-480)), (77, 148, 255), "ON", (0,0,0), buttonfont, "")
        self.button_list.append(self.option1_on_button)
        # option 1 off button
        self.option1_off_button = Button(100, 60, ((SCREEN_WIDTH/2)+200, (SCREEN_HEIGHT-480)), (77, 148, 255), "OFF", (0,0,0), buttonfont, "")
        self.button_list.append(self.option1_off_button)

        # return to menu button
        menu_button = Button(200, 60, ((SCREEN_WIDTH/2),(SCREEN_HEIGHT/2)+100), (77, 148, 255), "Main Menu", (0,0,0), buttonfont, "")
        self.button_list.append(menu_button)

    def update(self):
        self.screen.fill(SCREEN_COLOR)
        # need to be able to set button colour
        # all this method needs to do is set the button colour and draw the screen

        # draw to title and options
        title_text_rect = self.title.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT-570))
        self.screen.blit(self.title, title_text_rect)

        option_1_text_rect = self.option_1.get_rect(center=((SCREEN_WIDTH/2)-200, SCREEN_HEIGHT-480))
        self.screen.blit(self.option_1, option_1_text_rect)

        # (0, 71, 179) inactive colour
        # (77, 148, 255) active colour

        self.draw_buttons()
