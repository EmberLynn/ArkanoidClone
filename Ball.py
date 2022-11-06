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

        self.velocity = [2,5]

        self.rect = self.surf.get_rect(
            center=((100,100))
        )

    def update(self, screen_width, screen_height):
        if(self.rect.x>screen_width or self.rect.x<0):
                self.velocity[0] = -self.velocity[0]
        if(self.rect.y>screen_height or self.rect.y<0):
            self.velocity[1] = -self.velocity[1]

        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]

    # not good for hitting top or side of block
    def bounce(self):
        self.velocity[0] = -self.velocity[0]
        self.velocity[1] = random.randint(4,6)