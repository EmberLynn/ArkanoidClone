import pygame
from PlayerPaddle import PlayerPaddle
from Block import Block
from Ball import Ball

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

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
INITIAL_COLOR = (0, 102, 34)

running = True
clock = pygame.time.Clock()

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

player = PlayerPaddle(SCREEN_WIDTH,SCREEN_HEIGHT)
block = Block(SCREEN_WIDTH,SCREEN_HEIGHT)
block2 = Block(SCREEN_WIDTH,SCREEN_HEIGHT)
block3 = Block(SCREEN_WIDTH,SCREEN_HEIGHT)
block4 = Block(SCREEN_WIDTH,SCREEN_HEIGHT)

ball = Ball()

blocks = pygame.sprite.Group()
blocks.add(block)
blocks.add(block2)
blocks.add(block3)
blocks.add(block4)

all_sprites = pygame.sprite.Group()
all_sprites.add(player)
all_sprites.add(ball)

all_sprites.add(blocks)

while running:
    clock.tick(40)

    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
        elif event.type == QUIT:
            running = False

    player.update(pygame.key.get_pressed())
    ball.update(SCREEN_WIDTH,SCREEN_HEIGHT)

    ## DRAW on screen 
    #in the loop and first or else objects will appear to grow
    screen.fill(INITIAL_COLOR)
    
    for object in all_sprites:
        screen.blit(object.surf, object.rect)

    blocks_hit = pygame.sprite.spritecollide(ball, blocks, False)
    ball_offset_x = ball.rect.x
    ball_offset_y = ball.rect.y 

    for block in blocks_hit:
        # block is 75 X 25

        x_offset = ball_offset_x - block.rect.x
        y_offset = ball_offset_y - block.rect.y
        location = block.mask.overlap(ball.mask,(x_offset,y_offset))
        print(location)
        
        # is okayish -- needs to cover EVERY possibility or else behaviour is wonky
        if(location[1] == 0): # check for y min
            ball.bounce("top_or_bottom")
            print(location)
            print("top hit")
        elif(location[1] >= 20): # check for y max
            ball.bounce("top_or_bottom")
            print(location)
            print("bottom hit")
        elif(location[0] <= 4): # check for x min
            ball.bounce("sides")
            print(location)
            print("right hit")
        elif(location[0] >= 70): # check for x max
            ball.bounce("sides")
            print(location)
            print("left hit")
        # problem still is the above is always checked, so how to detect when it is side hit instead?
        
        # use masks for collision? https://www.pygame.org/docs/ref/mask.html#pygame.mask.Mask.outline

        # overlap = pygame.mask.Mask.overlap(block.mask,ball.rect.bottom)
        # if(overlap[0] == block.top):
        #     ball.bounce()

        #collidepoint?
        
        #<rect(687, 452, 75, 25)> block
        #<rect(751, 445, 10, 10)> ball (when colliding with block)

    # if pygame.sprite.spritecollideany(ball, blocks):
    #     ball.bounce()

    pygame.display.flip()

pygame.quit()