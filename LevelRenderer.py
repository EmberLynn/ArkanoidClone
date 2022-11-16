#a render class that creates groups of objects that don't overlap
#pass in object type you'd like to create and how many you'd like to create
#returns Group of objects to be drawn
#specifically, takes takes script and converts into block level group?

# can fit 10 blocks (x) max based on current screen width
# can fit 20 block (y) max based on current screen height (don't allow anything to render in the 500-600 range)
# reads files from a folder to generate a set of levels that are returned to the main game

import os
import pygame
from Block import Block

absolute_path = os.path.dirname(__file__)
relative_path = "Levels"
full_path = os.path.join(absolute_path, relative_path)

class LevelRenderer:
    def __init__(self):

        self.blocks = pygame.sprite.Group()
        # reading one file for now
        # final intent is to read all levels in the level folder
        block_section = False
        file = open(full_path + "\Level1.txt", "r")
        for line in file:
            
            # handle general properties  
            if('SCREEN_WIDTH' in line):
                self.screen_width = int(''.join(filter(str.isdigit,line)))
            elif('SCREEN_HEIGHT' in line):
                self.screen_height = int(''.join(filter(str.isdigit,line)))
            elif('LEVEL_COLOR' in line):
                var = line.split('=')
                self.level_color = eval(var[1])

            # handle block groups
            if('#blocks_section' in line):
                block_section = True
            if('#end_of_blocks' in line):
                block_section = False

            if(block_section):
                # do some error checking first
                # based on line length, block width and screen width, can this line be rendered?
                print("There was an error")
             
            
