#a render class that creates groups of objects that don't overlap
#pass in object type you'd like to create and how many you'd like to create
#returns Group of objects to be drawn
#specifically, takes takes script and converts into block level group?

# can fit 10 blocks (x) max based on current screen width
# can fit 20 block (y) max based on current screen height (don't allow anything to render in the 500-600 range)
# reads files from a folder to generate a set of levels that are return to the main game

import pygame

class LevelRenderer:
    def __init__(self) -> None:
        pass