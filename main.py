import pygame
import random
import sys
import os
from settings import *


# initialize pygame
pygame.init()
# initialize sound - uncomment if you're using sound
# pygame.mixer.init()
# create the game window and set the title
win = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
pygame.display.set_caption("My Game")

# Sprites
images = [pygame.image.load('imgs/Rocket.png')]

rocket = images[0]
# start the clock
clock = pygame.time.Clock()

# set the 'running' variable to False to end the game
running = True
# start the game loop
while running:
    # keep the loop running at the right speed
    clock.tick(FPS)
    # Game loop part 1: Events #####
    for event in pygame.event.get():
        win.blit(rocket, (ROCKETX, ROCKETY))
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
    # Game loop part 2: Updates #####

    # Game loop part 3: Draw #####
    win.fill(BGCOLOR)
    rectangle = pygame.Rect(200, 150, 100, 50)
    pygame.draw.rect(win, WHITE, rectangle)

    # after drawing, flip the display
    
    # update the display
    pygame.display.update()

# close the window
