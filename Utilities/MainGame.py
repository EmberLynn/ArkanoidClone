import pygame
from Screens.BaseScreen import BaseScreen

# main game holds global information that needs to be accessed by multiple game classes
class MainGame:
    def __init__(self):

        self.runningStart = False
        self.runningMain = False

        self.currentScreen = None

        # for continue screen
        self.boonHandler = None
        self.playerScore = 0
        self.displayScore = 0