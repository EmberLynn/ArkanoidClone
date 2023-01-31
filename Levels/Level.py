import pygame

class Level:
    def __init__(self):
        self.blocks = pygame.sprite.Group()

        self.__screen_width = 0
        self.__screen_height = 0
        self.__level_color = (0,0,0)
        self.__block_width = 0
        self.__block_height = 0
        self.__difficulty = 0

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

    def set_block_width(self, block_width):
        self.__block_width=block_width
    def get_block_width(self):
        return self.__block_width
    block_width=property(get_block_width, set_block_width)

    def set_block_height(self, block_height):
        self.__block_height=block_height
    def get_block_height(self):
        return self.__block_height
    block_height=property(get_block_height, set_block_height)

    def set_difficulty(self, difficulty):
        self.__difficulty=difficulty
    def get_difficulty(self):
        return self.__difficulty
    difficulty=property(set_difficulty,get_difficulty)