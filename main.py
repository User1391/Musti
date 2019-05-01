import pygame
import random
import sys
from settings import *
from pyganim import *
from physics import *



# initialize pygame
pygame.init()
# initialize sound - uncomment if you're using sound
# pygame.mixer.init()
# create the game window and set the title200
win = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)

pygame.display.set_caption("Space Create")

rocket = Body(win, pygame.image.load('imgs/Rocket.png'), "Rocket", 124, 12, 15)

# Sprites
images = [pygame.image.load('imgs/Rocket.png'), pygame.image.load('imgs/Asteroid.png')]
## rocket ##
# rocket = pygame.transform.scale(images[0], (200,200))
rocket.scaleImg((200,200))
#######
# asteroid
asteroid = pygame.transform.scale(images[1], (200,200))


# start the clock
clock = pygame.time.Clock()


# set the 'running' variable to False to end the game
running = True
# start the game loop

while running:
    # keep the loop running at the right speed
    clock.tick(FPS)
    # fill in background color
    rocket.mov((ROCKETX, ROCKETY))
    win.blit(asteroid, (ASTERX, ASTERY))

    #movement
    ROCKETX += SPEED
    #rocketRotate = pygame.transform.rotate(rocket, ROTATION)

    # Game loop part 1: Events #####
    for event in pygame.event.get():

        # this one checks for the window being closed
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            sys.exit()
        # add any other events here (keys, mouse, etc.)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
                pygame.quit()
                sys.exit()
            if event.key == pygame.K_LEFT:
                ROTATION = -45
            if event.key == pygame.K_RIGHT:
                ROTATION = 45

    # after drawing, flip the display

    # update the display


    pygame.display.update()
    win.fill(OUTER_SPACE)
# close the window
