import pygame
import random

# reference from here: https://www.101computing.net/pong-tutorial-using-pygame-adding-a-bouncing-ball/
class Ball(pygame.sprite.Sprite):
    def __init__(self):
        super(Ball,self).__init__()

        # bigger ball appears to perform better during collision
        self.surf = pygame.Surface((13,13))

        self.colour = [255, 71, 26]
        self.surf.fill((102, 102, 102))

        self.velocity = [2,5]

        self.rect = self.surf.get_rect()

        self.mask = pygame.mask.from_surface(self.surf)

        pygame.draw.rect(self.surf, (0,0,0),(0,0,12,12))
        pygame.draw.rect(self.surf, self.colour, (0,0,10,10))

    def update(self, screen_width, screen_height):
        if(self.rect.x>screen_width or self.rect.x<0):
                self.velocity[0] = -self.velocity[0]
        if(self.rect.y<0):
            self.velocity[1] = -self.velocity[1]
        if(self.rect.y>screen_height):
            self.kill()
            return False

        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]

        return True

    # not good for hitting top or side of block
    def bounce(self, area_hit):

        #top or bottom hit
        if(area_hit == "top_or_bottom"):
            self.velocity[1] = -self.velocity[1]
            if(self.velocity[0] < 0):
                self.velocity[0] = -random.randint(2,5)
            else:
                self.velocity[0] = random.randint(2,5)
        if(area_hit == "sides"):
            self.velocity[0] = -self.velocity[0]
            if(self.velocity[1] < 0):
                self.velocity[1] = -random.randint(2,5)
            else:
                self.velocity[1] = random.randint(2,5)