import pygame
from Screens.BaseScreen import BaseScreen

# main game holds global information that needs to be accessed by multiple game classes
class MainGame:
    def __init__(self):

        # default is to show the main menu -- start screen
        self.runningStart = True
        self.runningMain = False

        self.currentScreen = None

        # for continue screen
        self.boonHandler = None
        self.playerScore = 0
        self.displayScore = 0
        self.boon_name = ""