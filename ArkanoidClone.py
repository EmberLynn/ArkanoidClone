import pygame
from PlayerPaddle import PlayerPaddle
from Block import Block
from Ball import Ball
from LevelRenderer import LevelRenderer

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
pygame.init()

LevelRenderer = LevelRenderer()

SCREEN_WIDTH = LevelRenderer.screen_width
SCREEN_HEIGHT = LevelRenderer.screen_height
INITIAL_COLOR = LevelRenderer.level_color

running = True
clock = pygame.time.Clock()

playerScore = 0
myfont = pygame.font.SysFont("Good Times Regular", 25, True)

screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

player = PlayerPaddle(SCREEN_WIDTH,SCREEN_HEIGHT)
playerGroup = pygame.sprite.GroupSingle(player)

block = Block(SCREEN_WIDTH,SCREEN_HEIGHT)
block2 = Block(SCREEN_WIDTH,SCREEN_HEIGHT)
block3 = Block(SCREEN_WIDTH,SCREEN_HEIGHT)
block4 = Block(SCREEN_WIDTH,SCREEN_HEIGHT)

blocks = pygame.sprite.Group()
blocks.add(block)
blocks.add(block2)
blocks.add(block3)
blocks.add(block4)

ball = Ball()

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

    player.update(pygame.key.get_pressed(), SCREEN_WIDTH)
    ball.update(SCREEN_WIDTH,SCREEN_HEIGHT)

    ## DRAW on screen 
    #in the loop and first or else objects will appear to grow
    screen.fill(INITIAL_COLOR)

    for object in all_sprites:
        screen.blit(object.surf, object.rect)

    score = myfont.render("Score: " + str(playerScore), 1, (255,255,0))
    screen.blit(score, (SCREEN_WIDTH-120, 25))

    #------------------paddle hit-----------------------------------------------
    if(pygame.sprite.spritecollide(ball, playerGroup, False)):
        ball.bounce("top_or_bottom")
    #---------------------------------------------------------------------------

    #------------------block hits-----------------------------------------------
    blocks_hit = pygame.sprite.spritecollide(ball, blocks, False)

    for block in blocks_hit:
       
        x_offset_block = ball.rect.x - block.rect.x
        y_offset_block = ball.rect.y - block.rect.y
        blockhit = block.mask.overlap(ball.mask,(x_offset_block,y_offset_block))
        
        x_offset_ball = block.rect.x - ball.rect.x
        y_offset_ball = block.rect.y - ball.rect.y
        ballhit = ball.mask.overlap(block.mask,(x_offset_ball,y_offset_ball))
        
        # check for zeroes since they are pixel perfect
        # check for velocity to ensure ball bounces in correct direction and doesn't clip
        # corner collisions are still imperfect, but ball no longer clips directly into block
        if(blockhit is not None or ballhit is not None):
            if(blockhit[1] == 0):
                if(ball.velocity[1] >= 0):
                    ball.bounce("top_or_bottom")
            elif(ballhit[0] == 0):
                if(ball.velocity[1] < 0):
                    ball.bounce("top_or_bottom")
            elif(ballhit[1] == 0):
                if(ball.velocity[0] < 0):
                    ball.bounce("sides")
            elif(blockhit[0] == 0):
                if(ball.velocity[0] >= 0):
                    ball.bounce("sides")
            else:
                print("failed to register hit")

            playerScore += 10
            block.kill()
    #------------------------------------------------------------------------------

    pygame.display.flip()

pygame.quit()