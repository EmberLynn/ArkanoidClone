# boon handler takes a boon and decides what changes the game need to make to fulfill the boon
# for now, the BoonHandler will hold the list of boons, but I'd like to create a game object that handles it
# BoonHandler can manipulate sprite objects: Block, Ball, and PlayerPaddle
import random
import pygame
from Utilities.Boon import Boon

class BoonHandler:
    def __init__(self, player, ball):
        print("To be implemented")

        self.player = player
        self.ball = ball
        self.boons = []

        # boonHandler creates all boons
        self.paddle_speed_boon = Boon("paddle_speed", False, "Paddle speed has been increased!")
        self.boons.append(self.paddle_speed_boon)

        self.paddle_length_boon = Boon("longer_paddle", False, "Paddle has become longer!")
        self.boons.append(self.paddle_length_boon)

        # self.second_ball_boon = Boon("second_ball", False, "A second ball has been added!")
        # self.boons.append(self.second_ball_boon)

        random.shuffle(self.boons)

    def handle_boon(self, boon_name):

        if boon_name == "paddle_speed":
            self.player.paddlespeed += 5
        elif boon_name == "longer_paddle":
            self.player.paddle_length += 10
            self.player.redraw_paddle()
            
            
        for boon in self.boons:
            if boon.name == boon_name:
                boon.set_active(True)

    def handle_block_boon(self, block):
        print("To be implemented")