#a render class that creates groups of objects that don't overlap
#pass in object type you'd like to create and how many you'd like to create
#returns Group of objects to be drawn
#specifically, takes takes script and converts into block level group?

# can fit 10 blocks (x) max based on current screen width
# can fit 20 block (y) max based on current screen height (don't allow anything to render in the 500-600 range)
# reads files from a folder to generate a set of levels that are returned to the main game

import os
import sys
import math
from Sprites.Block import Block
from Levels.Level import Level

absolute_path = os.path.dirname(__file__)
relative_path = "LevelMaps"
# relative_path = "LevelMaps"
full_path = os.path.join(absolute_path, relative_path)
files = os.listdir(full_path)

class LevelRenderer:
    def __init__(self):

        self.levels = []

        # read all files in Level folder
        for file in files:

            new_level = Level()
            block_section = False
            rows = 0 # rows start at 0

            file = open(os.path.join(full_path,file),'r')
            for linenum, line in enumerate(file, 1):
                # handle general properties  
                if('SCREEN_WIDTH' in line):
                    new_level.set_screen_width(int(''.join(filter(str.isdigit,line))))
                elif('SCREEN_HEIGHT' in line):
                    new_level.set_screen_height(int(''.join(filter(str.isdigit,line))))
                elif('LEVEL_COLOR' in line):
                    var = line.split('=')
                    new_level.set_level_color(eval(var[1]))
                elif('BLOCK_WIDTH' in line):
                    new_level.set_block_width(int(''.join(filter(str.isdigit,line))))
                elif('BLOCK_HEIGHT' in line):
                    new_level.set_block_height(int(''.join(filter(str.isdigit,line))))
                elif('DIFFICULTY' in line):
                    new_level.set_difficulty(int(''.join(filter(str.isdigit,line))))

                # handle block groups
                if('#blocks_section' in line):
                    block_section = True
                    continue
                if('#end_of_blocks' in line):
                    block_section = False
                    continue
                try:
                    if block_section:
                        linelength = len(line)-1
                        maxrows = math.trunc(((new_level.get_screen_height()-50)/new_level.get_block_height())-1) # subtract 1 because rows start at 0

                        # do some error checking first
                        # based on line length, block width and screen width, can this line be rendered?
                        if(new_level.get_block_width ()> (new_level.get_screen_width()/linelength)):
                            raise Exception("Your blocks are too wide given the screen width and column request!")
                        
                        # based on row total, block height, and screen heigth, can anything be rendered?
                        if(rows > maxrows):
                            raise Exception("You've defined too many rows based on screen height and block height!") 

                        # calculate where to draw the block and add it to blocks group
                        # need to calculate where we start drawing the block based on current line
                        # block rule: rendering always starts at 0,0
                        column = 0
                        for char in line:
                            if "B" in char:
                                block_x = (column*new_level.get_block_width())
                                block_y = (rows*new_level.get_block_height())

                                new_block = Block(block_x,block_y,new_level.get_block_width(),new_level.get_block_height(),new_level.get_difficulty())
                                new_level.blocks.add(new_block)

                            column += 1

                        # move to next row
                        rows += 1
                            
                except Exception as e:
                    print(e)
                    print("Problem located in" + file.name + " at " + line + " Line number:" + str(linenum))
                    sys.exit() # we can't go on!
            
            # add level to levels
            self.levels.append(new_level)
            file.close()


             
            
