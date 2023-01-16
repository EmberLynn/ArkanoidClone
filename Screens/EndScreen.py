import pygame
from Screens.BaseScreen import BaseScreen
from Utilities.Button import Button

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
        self.quit_button_text = buttonfont.render("Quit",1,(0,0,0))

        # create buttons
        self.button_list = []

        # start button
        start_button = Button(200, 60, ((SCREEN_WIDTH/2),(SCREEN_HEIGHT/2)), (77, 148, 255), "Restart Game", (0,0,0), buttonfont)
        self.button_list.append(start_button)

        # return to menu button
        menu_button = Button(200, 60, ((SCREEN_WIDTH/2),(SCREEN_HEIGHT/2)+100), (77, 148, 255), "Main Menu", (0,0,0), buttonfont)
        self.button_list.append(menu_button)

        # quit button
        quit_button = Button(200, 60, ((SCREEN_WIDTH/2),(SCREEN_HEIGHT/2)+200), (77, 148, 255), "Quit Game", (0,0,0), buttonfont)
        self.button_list.append(quit_button)

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