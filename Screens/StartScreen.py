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

VERSION_NUM = .1

SCREEN_HEIGHT = 600
SCREEN_WIDTH = 900
SCREEN_COLOR = ((0, 153, 77))

class StartScreen(BaseScreen):
    def __init__(self):
        super().__init__() 

        buttonfont = pygame.font.SysFont("Good Times Regular", 30, False)
        titlefont = pygame.font.SysFont("Good Times Regular", 50, False)
        tinyfont = pygame.font.SysFont("Good Times Regular", 20, False)

        # basic info -- doubling up here; might want to change later
        self.set_screen_height(SCREEN_HEIGHT)
        self.set_screen_width(SCREEN_WIDTH)
        self.set_level_color((SCREEN_COLOR))

        # screen text
        self.title = titlefont.render("BARKanoid!",1,(0,0,0))
        self.version_num = tinyfont.render("Version: " + str(VERSION_NUM),1,(0,0,0))

        # create buttons
        self.button_list = []

        # start button
        start_button = Button(200, 60, ((SCREEN_WIDTH/2),(SCREEN_HEIGHT/2)+50), (77, 148, 255), "Start Game", (0,0,0), buttonfont)
        self.button_list.append(start_button)

        # quit button
        quit_button = Button(200, 60, ((SCREEN_WIDTH/2),(SCREEN_HEIGHT/2)+130), (77, 148, 255), "Quit Game", (0,0,0), buttonfont)
        self.button_list.append(quit_button)

    def draw(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
        self.screen.fill(SCREEN_COLOR)

        # draw title on screen
        title_text_rect = self.title.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT-570))
        self.screen.blit(self.title, title_text_rect)

        # draw buttons
        for button in self.button_list:
            pygame.draw.rect(self.screen, button.button_colour, button.button_dimensions)
            self.screen.blit(button.button_text, button.button_text_rect)

        # version number
        version_num_text_rect = self.version_num.get_rect(center=(SCREEN_WIDTH-50,SCREEN_HEIGHT-10))
        self.screen.blit(self.version_num, version_num_text_rect)
    
    def check_mouse_click(self):

        mouse_x = pygame.mouse.get_pos()[0]
        mouse_y = pygame.mouse.get_pos()[1]

        for button in self.button_list:
            if button.clicked(mouse_x, mouse_y):
                return button.label_text