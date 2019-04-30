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
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
pygame.display.set_caption("My Game")
rocket = pygame.image.load("imgs/Rocket.png")
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
        screen.blit(rocket, (2,2))
        # this one checks for the window being closed
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            sys.exit()
        # add any other events here (keys, mouse, etc.)

    # Game loop part 2: Updates #####

    # Game loop part 3: Draw #####
    # screen.fill(BGCOLOR)
    rectangle = pygame.Rect(200, 150, 100, 50)
    pygame.draw.rect(screen, WHITE, rectangle)

    # after drawing, flip the display
    pygame.display.flip()
    # update the display
    pygame.display.update()

# close the window
