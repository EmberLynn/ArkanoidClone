import pygame
from Screens.BaseScreen import BaseScreen
from Utilities.Button import Button

# HighScoreScreen contians:
# size
# colour
# High Scores (title)
# List of top ten scores of all time
# Main Menu Button

SCREEN_HEIGHT = 600
SCREEN_WIDTH = 900
SCREEN_COLOR = ((0, 153, 77))

class HighScoreScreen(BaseScreen):
    def __init__(self):
        super().__init__()

        buttonfont = pygame.font.SysFont("Good Times Regular", 30, False)
        titlefont = pygame.font.SysFont("Good Times Regular", 50, False)

        # screen text
        self.title = titlefont.render("Top 10 High Scores:",1,(0,0,0))

        # main menu button
        quit_button = Button(200, 60, ((SCREEN_WIDTH/2),(SCREEN_HEIGHT/2)+210), (77, 148, 255), "Main Menu", (0,0,0), buttonfont)
        self.button_list.append(quit_button)

    def draw(self, display_flags):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT), display_flags)
        self.screen.fill(SCREEN_COLOR)

        # draw title on screen
        title_text_rect = self.title.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT-570))
        self.screen.blit(self.title, title_text_rect)

        # draw scores on screen
        # font is created here for rendering scores dynamically
        scorefont = pygame.font.SysFont("Good Times Regular", 30, False)
        scorepos = 540 # where to draw on scree; needs to be incremented
        high_score_list = self.get_high_scores()
        for score in high_score_list:
            score_text = scorefont.render(score,1,(255,255,0))
            score_text_rect = score_text.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT-scorepos))
            self.screen.blit(score_text, score_text_rect)
            scorepos -= 30

        self.draw_buttons()