import pygame
from BaseScreen import BaseScreen

# StartScreen contains:
# size
# colour
# game name (title)
# clickable start button
# options (TBD)
# scores (TBD)
# version number in top left

SCREEN_HEIGHT = 600
SCREEN_WIDTH = 900
SCREEN_COLOR = ((0, 153, 77))

# buttons
# start button
START_BUTTON_LEFT = ((SCREEN_WIDTH/2)-100)
START_BUTTON_TOP = (SCREEN_HEIGHT/2)
START_BUTTON_RIGHT = START_BUTTON_LEFT + 200
START_BUTTON_BOTTOM = START_BUTTON_TOP + 60

class StartScreen(BaseScreen):
    def __init__(self):
        super().__init__() 

        buttonfont = pygame.font.SysFont("Good Times Regular", 30, False)
        titlefont = pygame.font.SysFont("Good Times Regular", 50, False)

        # basic info -- doubling up here; might want to change later
        self.set_screen_height(SCREEN_HEIGHT)
        self.set_screen_width(SCREEN_WIDTH)
        self.set_level_color((SCREEN_COLOR))

        # screen text
        self.title = titlefont.render("BARKanoid!",1,(0,0,0))
        self.start_button_text = buttonfont.render("Start Game",1,(0,0,0))

        # position of start button
        self.start_button_dimensions = (((SCREEN_WIDTH/2)-100),(SCREEN_HEIGHT/2),200,60)

    def draw(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
        self.screen.fill(SCREEN_COLOR)

        # draw title on screen
        self.screen.blit(self.title, (((SCREEN_WIDTH/2)-100),20))

        # start button
        pygame.draw.rect(self.screen,(77, 148, 255),self.start_button_dimensions)
        self.screen.blit(self.start_button_text, (((SCREEN_WIDTH/2)-55),(SCREEN_HEIGHT/2)+20))
    
    def check_mouse_click(self):

        mouse_x = pygame.mouse.get_pos()[0]
        mouse_y = pygame.mouse.get_pos()[1]

        if mouse_x >= START_BUTTON_LEFT and mouse_x <= START_BUTTON_RIGHT and mouse_y >= START_BUTTON_TOP and mouse_y <= START_BUTTON_BOTTOM:
            return "start_button"
