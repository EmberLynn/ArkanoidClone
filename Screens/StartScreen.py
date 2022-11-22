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

myfont = pygame.font.SysFont("Good Times Regular", 25, True)

class StartScreen(BaseScreen):
    def __init__(self):
        super().__init__() 

        # basic info
        self.set_screen_height(600)
        self.set_screen_width(900)
        self.set_level_color((0, 153, 77))

        # title
        self.title = myfont.render("BARKanoid!",1,(0,0,0))

        # start button
        self.start_button_text = myfont.render("Start Game",1,(0,0,0))
        self.start_button = pygame.Surface((75,25))
        self.start_button.fill(77, 148, 255)

        self.start_button_rect = self.start_button.get_rect(
            center =((self.get_screen_width/2),(self.get_screen_height-50))
        )

        # add draw function that returns screen?