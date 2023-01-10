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

VERSION_NUM = .5

SCREEN_HEIGHT = 600
SCREEN_WIDTH = 900
SCREEN_COLOR = ((0, 153, 77))

# button location and sizes
# start button
START_BUTTON_LEFT = ((SCREEN_WIDTH/2)-100)
START_BUTTON_TOP = (SCREEN_HEIGHT/2)
START_BUTTON_RIGHT = START_BUTTON_LEFT + 200
START_BUTTON_BOTTOM = START_BUTTON_TOP + 60

# quit button
QUIT_BUTTON_LEFT = ((SCREEN_WIDTH/2)-100)
QUIT_BUTTON_TOP = ((SCREEN_HEIGHT/2)+100)
QUIT_BUTTON_RIGHT = QUIT_BUTTON_LEFT + 200
QUIT_BUTTON_BOTTOM = QUIT_BUTTON_TOP + 60

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
        self.start_button_text = buttonfont.render("Start Game",1,(0,0,0))
        self.quit_button_text = buttonfont.render("Quit",1,(0,0,0))
        self.version_num = tinyfont.render("Version: " + str(VERSION_NUM),1,(0,0,0))

        # position of start button
        self.start_button_dimensions = (START_BUTTON_LEFT,START_BUTTON_TOP,200,60)

        # position of quit button
        self.quit_button_dimensions = (QUIT_BUTTON_LEFT,QUIT_BUTTON_TOP,200,60)

    def draw(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
        self.screen.fill(SCREEN_COLOR)

        # draw title on screen
        title_text_rect = self.title.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT-570))
        self.screen.blit(self.title, title_text_rect)

        # start button
        pygame.draw.rect(self.screen,(77, 148, 255),self.start_button_dimensions)
        start_text_rect = self.start_button_text.get_rect(center=(START_BUTTON_LEFT+100, START_BUTTON_TOP+30))
        self.screen.blit(self.start_button_text, start_text_rect)

        # quit button
        pygame.draw.rect(self.screen,(77, 148, 255),self.quit_button_dimensions)
        quit_text_rect = self.quit_button_text.get_rect(center=(QUIT_BUTTON_LEFT+100, QUIT_BUTTON_TOP+30))
        self.screen.blit(self.quit_button_text, quit_text_rect)

        # version number
        version_num_text_rect = self.version_num.get_rect(center=(SCREEN_WIDTH-50,SCREEN_HEIGHT-10))
        self.screen.blit(self.version_num, version_num_text_rect)
    
    def check_mouse_click(self):

        mouse_x = pygame.mouse.get_pos()[0]
        mouse_y = pygame.mouse.get_pos()[1]

        if(mouse_x >= START_BUTTON_LEFT 
            and mouse_x <= START_BUTTON_RIGHT 
            and mouse_y >= START_BUTTON_TOP 
            and mouse_y <= START_BUTTON_BOTTOM):
            return "start_button"
        elif(mouse_x >= QUIT_BUTTON_LEFT 
            and mouse_x <= QUIT_BUTTON_RIGHT 
            and mouse_y >= QUIT_BUTTON_TOP 
            and mouse_y <= QUIT_BUTTON_BOTTOM):
            return "quit_button"