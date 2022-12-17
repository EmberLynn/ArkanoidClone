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

class StartScreen(BaseScreen):
    def __init__(self):
        super().__init__() 

        myfont = pygame.font.SysFont("Good Times Regular", 25, True)

        # basic info -- doubling up here; might want to change later
        self.set_screen_height(SCREEN_HEIGHT)
        self.set_screen_width(SCREEN_WIDTH)
        self.set_level_color((SCREEN_COLOR))

        # title
        self.title = myfont.render("BARKanoid!",1,(0,0,0))

        # start button
        self.start_button_text = myfont.render("Start Game",1,(0,0,0))
        self.start_button = pygame.Surface((75,25))
        self.start_button.fill((77, 148, 255))

        self.start_button_rect = self.start_button.get_rect(
            center =((SCREEN_WIDTH/2),(SCREEN_HEIGHT-50))
        )

        
    def draw(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
        self.screen.fill(SCREEN_COLOR)