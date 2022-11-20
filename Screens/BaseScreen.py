# a class of commonalities that all screens share
# All screens have size (height and width) and colour, at the least 
# has similarities to Level, but I'll keep them seperate for now
import pygame

class BaseScreen:
    def __init__(self):

        self.__screen_width = 0
        self.__screen_height = 0
        self.__level_color = (0,0,0)

    def set_screen_width(self, screen_width):
        self.__screen_width=screen_width
    def get_screen_width(self):
        return self.__screen_width
    screen_width=property(get_screen_width, set_screen_width)

    def set_screen_height(self, screen_height):
        self.__screen_height=screen_height
    def get_screen_height(self):
        return self.__screen_height
    screen_height=property(get_screen_height, set_screen_height)

    def set_level_color(self, level_color):
        self.__level_color=level_color
    def get_level_color(self):
        return self.__level_color
    level_color=property(get_level_color, set_level_color)