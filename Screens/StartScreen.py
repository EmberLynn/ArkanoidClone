import pygame
from BaseScreen import BaseScreen

# StartScreen contains:
# size
# colour
# clickable start button
# options (TBD)
# scores (TBD)
# version number in top left

class StartScreen(BaseScreen):
    def __init__(self):
        super().__init__() 

        self.set_screen_height(600)