import os
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

        self.buttonfont = pygame.font.SysFont("Good Times Regular", 30, False)
        self.titlefont = pygame.font.SysFont("Good Times Regular", 50, False)

        # screen text
        self.title = self.titlefont.render("Game Over!",1,(0,0,0))
        self.quit_button_text = self.buttonfont.render("Quit",1,(0,0,0))

        # start button
        start_button = Button(200, 60, ((SCREEN_WIDTH/2),(SCREEN_HEIGHT/2)), (77, 148, 255), "Restart Game", (0,0,0), self.buttonfont)
        self.button_list.append(start_button)

        # return to menu button
        menu_button = Button(200, 60, ((SCREEN_WIDTH/2),(SCREEN_HEIGHT/2)+100), (77, 148, 255), "Main Menu", (0,0,0), self.buttonfont)
        self.button_list.append(menu_button)

        # quit button
        quit_button = Button(200, 60, ((SCREEN_WIDTH/2),(SCREEN_HEIGHT/2)+200), (77, 148, 255), "Quit Game", (0,0,0), self.buttonfont)
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

        self.draw_buttons()

    # needs high score list and current score
    def check_for_high_score(self, current_score):

        new_high_score = False

        high_score_list = self.get_high_scores()

        sorted_scores = []

        # create tuple to sort by actual score
        for line in high_score_list:
            temp_tup = line.split(":")
            temp_int = int(temp_tup[1])
            sorted_scores.append((temp_tup[0],temp_int))

        # assume scores won't be sorted in the file, so sort before check
        sorted_scores = sorted(sorted_scores, key=lambda tup: tup[1], reverse=True)
        if(current_score > sorted_scores[len(sorted_scores)-1][1]):
            new_high_score = True

        return new_high_score

    # "popup" -- as in mock popup since everything still needs to be drawn
    def draw_high_score_popup(self):

        # screen text
        popup_title = self.titlefont.render("You got a high score!",1,(0,0,0))
        popup_prompt = self.titlefont.render("Enter you name:",1,(0,0,0))

        # draw popup rect
        popup_rect = pygame.Rect(0,0,500,500)
        popup_rect.center = (self.screen.get_rect().center)
        pygame.draw.rect(self.screen, (102, 204, 255), popup_rect)
        

        # draw input box rect
        input_box_rect = pygame.Rect(0,0,200,50)
        input_box_rect.center = (self.screen.get_rect().center)
        pygame.draw.rect(self.screen, (255,255,255), input_box_rect)

        # draw text 
        popup_title_text_rect = popup_title.get_rect(center=(popup_rect.centerx,popup_rect.centery-200))
        self.screen.blit(popup_title, popup_title_text_rect)

        popup_prompt_rect = popup_prompt.get_rect(center=(popup_rect.centerx,popup_rect.centery-150))
        self.screen.blit(popup_prompt, popup_prompt_rect)

        pygame.display.flip() 

        # this would be more useful as its own class
        prompting_player = True
        input_text = ""
        while prompting_player:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        return
                    elif event.key == pygame.K_RETURN:
                        prompting_player = False
                    elif event.key == pygame.K_BACKSPACE:
                        input_text = input_text[:-1] # strips the last char
                    else:
                        if len(input_text) == 7:
                            input_text = input_text[:-1] 
                        input_text += event.unicode

                    # input box needs to be redraw or else text over laps
                    pygame.draw.rect(self.screen, (255,255,255), input_box_rect)
                    player_name = self.titlefont.render(input_text,1,(0,0,0))
                    self.screen.blit(player_name, player_name.get_rect(center=input_box_rect.center))
                    pygame.display.flip() 

                elif event.type == pygame.QUIT:
                    return  
        # once above loop is complete, write score to file
        # this is going to require some of the above functionality, so might want to write a function

        


