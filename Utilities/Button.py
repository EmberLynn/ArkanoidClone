# what does a button have?
# position -- left, top, right, bottom
# size -- width, height
# color -- optional (default is black)
# text
# font
# clicked event?

# what do we want to give a button and what does a button need?
# Give it: size (width, height [tuple]), co-ordinates (center [tuple]), button colour (optional), text,
# text colour (optional), text size (optional), text font (optional)
# It needs: top, bottom, left, right (based on size and co-ordinates),
# if the button has been clicked, to draw itself(?)

# buttons could have been treated as Sprites, but NOPE; I just had to make
# my own class instead...

import pygame

class Button:
    def __init__(self, width, height, center, button_colour, button_label, label_colour, label_font):

        # take Y and subtract half the height to get top
        self.__top = center[1] - (height/2)
        # get bottom from top and height
        self.__bottom = self.__top + height
        # take X and subtract half the width to get right
        self.__left = center[0] - (width/2)
        # get left from right and width
        self.__right = self.__left + width

        # optional (default is white)
        self.button_colour = button_colour # needs getter

        # text attributes
        self.__label_text = button_label
        # optional (default is black)
        self.__label_colour = label_colour
        # optional (default is pygame.font.SysFont("Good Times Regular", 30, False))
        self.__label_font = label_font

        # dimensions for drawing button
        self.button_dimensions = (self.__left, self.__top, width, height)

        # set and center the text
        self.button_text = label_font.render(button_label, 1, label_colour)
        self.button_text_rect = self.button_text.get_rect(center=center)

    @classmethod
    def make_default_button(cls, width, height, center, button_label):

        # defaults for optional params
        button_colour = (0,0,0)
        label_colour = (255,255,255)
        label_font = pygame.font.SysFont("Good Times Regular", 30, False)

        return cls(width, height, center, button_colour, button_label, label_colour, label_font)

    def clicked(self, mouse_x, mouse_y):

        if(mouse_x >= self.__left
            and mouse_x <= self.__right
            and mouse_y >= self.__top
            and mouse_y <= self.__bottom):
            return True
        else:
            return False