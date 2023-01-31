import pygame
import random

from pygame.locals import (
    RLEACCEL,
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT
)

class Block(pygame.sprite.Sprite):
    def __init__(self, block_x, block_y, width, height, health):
        super(Block,self).__init__()
        self.surf = pygame.Surface((width,height))

        # block to be random colour
        self.colour = [random.randint(0,255),random.randint(0,255),random.randint(0,255)]
        self.surf.fill((102, 102, 102))

        self.rect = self.surf.get_rect(
            x=block_x,
            y=block_y
        )

        self.health = health

        self.mask = pygame.mask.from_surface(self.surf)

        pygame.draw.rect(self.surf, (0,0,0), (2,2,width-5,height-5))
        pygame.draw.rect(self.surf, self.colour, (0,0,width-5,height-5))

    def block_hit(self, screen):
        if self.health <= 0:
            self.kill()
        else:
            self.health -= 1

        if self.health == 0:
            # need to set surface again and draw damage image on top? Could have blocks in control of drawing themselves.
            pygame.draw.rect(self.surf, (255,255,255), self.rect)

    def draw(self, screen, difficulty):
        # draw thyself
        screen.blit(self.surf, self.rect)

        # control block damage appearance based on the levels difficulty
        if(difficulty == 0 or
            difficulty == 1 and self.health == 1 or
            difficulty == 2 and self.health == 2):
            return
        
        img_test_render = self.show_damage()
        screen.blit(img_test_render, self.rect)


    # helper functions
    def show_damage(self):
        if self.health == 0:
            img_test = pygame.image.load("./Assests/block_dmg_2.png").convert() # one more hit to kill
        else:
            img_test = pygame.image.load("./Assests/block_dmg_1.png").convert() # two more hits to kill

        img_test.set_colorkey((255,255,255))
        return pygame.transform.scale(img_test, (self.rect.width-5,self.rect.height-5))

    


            

