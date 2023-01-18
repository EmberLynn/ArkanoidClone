import os
import pygame

class BaseScreen:
    def __init__(self):

        self.button_list = []

    def check_mouse_click(self):

        mouse_x = pygame.mouse.get_pos()[0]
        mouse_y = pygame.mouse.get_pos()[1]

        for button in self.button_list:
            if button.clicked(mouse_x, mouse_y):
                return button.label_text

    def draw_buttons(self):
        for button in self.button_list:
            pygame.draw.rect(self.screen, button.button_colour, button.button_dimensions)
            self.screen.blit(button.button_text, button.button_text_rect)

    # because EndScreen and HighScoreScreen need access to this
    def get_high_scores(self):

        absolute_path = os.path.dirname(__file__)
        relative_path = "..\\Assests"
        full_path = os.path.join(absolute_path, relative_path)
        file = os.path.join(full_path,"high_scores.txt")

        # get the saved high scores
        high_score_list = []
        f = open(file,'r')
        for line in f:
            high_score_list.append(line.rstrip('\n'))

        return high_score_list