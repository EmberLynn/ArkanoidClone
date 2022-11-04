import pygame
import random

# reference from here: https://www.101computing.net/pong-tutorial-using-pygame-adding-a-bouncing-ball/
class Ball(pygame.sprite.Sprite):
    def __new__(cls, *args,**kwargs):
        return super().__new__(cls)

    def __init__(self):
        super(Ball,self).__init__()

        self.surf = pygame.Surface((10,10))

        self.colour = [random.randint(0,255),random.randint(0,255),random.randint(0,255)]
        self.surf.fill(self.colour)

        self.velocity = [0,5]

        self.rect = self.surf.get_rect(
            center=((100,100))
        )

    def update(self):
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]