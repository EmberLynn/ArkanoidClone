import pygame
from BaseScreen import BaseScreen

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

# buttons
# restart button
START_BUTTON_LEFT = ((SCREEN_WIDTH/2)-100)
START_BUTTON_TOP = (SCREEN_HEIGHT/2)
START_BUTTON_RIGHT = START_BUTTON_LEFT + 200
START_BUTTON_BOTTOM = START_BUTTON_TOP + 60

# main button
MAIN_BUTTON_LEFT = ((SCREEN_WIDTH/2)-100)
MAIN_BUTTON_TOP = ((SCREEN_HEIGHT/2)+100)
MAIN_BUTTON_RIGHT = MAIN_BUTTON_LEFT + 200
MAIN_BUTTON_BOTTOM = MAIN_BUTTON_TOP + 60

# quit button
QUIT_BUTTON_LEFT = ((SCREEN_WIDTH/2)-100)
QUIT_BUTTON_TOP = ((SCREEN_HEIGHT/2)+200)
QUIT_BUTTON_RIGHT = QUIT_BUTTON_LEFT + 200
QUIT_BUTTON_BOTTOM = QUIT_BUTTON_TOP + 60


class EndScreen(BaseScreen):
    def __init__(self):
        super().__init__()

        buttonfont = pygame.font.SysFont("Good Times Regular", 30, False)
        titlefont = pygame.font.SysFont("Good Times Regular", 50, False)

        # basic info -- doubling up here; might want to change later
        self.set_screen_height(SCREEN_HEIGHT)
        self.set_screen_width(SCREEN_WIDTH)
        self.set_level_color((SCREEN_COLOR))

        # screen text
        self.title = titlefont.render("Game Over!",1,(0,0,0))
        self.start_button_text = buttonfont.render("Restart Game",1,(0,0,0))
        self.main_button_text = buttonfont.render("Main Menu",1,(0,0,0))
        self.quit_button_text = buttonfont.render("Quit",1,(0,0,0))

        # position of start button
        self.start_button_dimensions = (START_BUTTON_LEFT,START_BUTTON_TOP,200,60)

        # position of return to menu button
        self.main_button_dimensions = (MAIN_BUTTON_LEFT,MAIN_BUTTON_TOP,200,60)

        # position of quit button
        self.quit_button_dimensions = (QUIT_BUTTON_LEFT,QUIT_BUTTON_TOP,200,60)

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

        # start button
        pygame.draw.rect(self.screen,(77, 148, 255),self.start_button_dimensions)
        start_text_rect = self.start_button_text.get_rect(center=(START_BUTTON_LEFT+100, START_BUTTON_TOP+30))
        self.screen.blit(self.start_button_text, start_text_rect)

        # main menu button
        pygame.draw.rect(self.screen,(77, 148, 255),self.main_button_dimensions)
        quit_text_rect = self.main_button_text.get_rect(center=(MAIN_BUTTON_LEFT+100, MAIN_BUTTON_TOP+30))
        self.screen.blit(self.main_button_text, quit_text_rect)

        # quit button
        pygame.draw.rect(self.screen,(77, 148, 255),self.quit_button_dimensions)
        quit_text_rect = self.quit_button_text.get_rect(center=(QUIT_BUTTON_LEFT+100, QUIT_BUTTON_TOP+30))
        self.screen.blit(self.quit_button_text, quit_text_rect)

    def chec_mouse_click(self):

        mouse_x = pygame.mouse.get_pos()[0]
        mouse_y = pygame.mouse.get_pos()[1]

        if(mouse_x >= START_BUTTON_LEFT 
            and mouse_x <= START_BUTTON_RIGHT 
            and mouse_y >= START_BUTTON_TOP 
            and mouse_y <= START_BUTTON_BOTTOM):
            return "start_button"
        elif(mouse_x >= MAIN_BUTTON_LEFT 
            and mouse_x <= MAIN_BUTTON_RIGHT 
            and mouse_y >= MAIN_BUTTON_TOP 
            and mouse_y <= MAIN_BUTTON_BOTTOM):
            return "main_button"
        elif(mouse_x >= QUIT_BUTTON_LEFT 
            and mouse_x <= QUIT_BUTTON_RIGHT 
            and mouse_y >= QUIT_BUTTON_TOP 
            and mouse_y <= QUIT_BUTTON_BOTTOM):
            return "quit_button"