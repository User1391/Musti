import random
import sys
import pygame
from settings import *
from pyganim import *
from physics import *
from intro import *
#from procgen import *
from functions import *

# initialize pygame
pygame.init()
# initialize sound - uncomment if you're using sound
# pygame.mixer.init()
# create the game window and set the title200
win = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)
pygame.display.set_caption("Space Create")



# Sprites
images = [pygame.image.load('imgs/Rocket.png'), pygame.image.load('imgs/Asteroid.png'), pygame.image.load('imgs/BlackHole.png'),pygame.image.load('imgs/BackgroundTile.png')]


## rocket ##
rocketAnim = ['imgs/Rocket.png', 'imgs/RocketEx1.png', 'imgs/RocketEx2.png', 'imgs/RocketEx3.png']
rocket = Body(win, images[0], (60, 35), ROCKET_MASS, (ROCKETX, ROCKETY))

#######

# black hole

bholesL = []



run= True


while run:

    clock = pygame.time.Clock()
    #fillScreen(win)
    # keep the loop running at 0the right speed

    menu(win, clock)
    # set the 'running' variable to False to end the game
    running = True
    # start the game loop
    # start the clock

    rocketAccel = []

    while running:
        win.fill(OUTER_SPACE)
        # keep the loop running at the right speed

        clock.tick(FPS)

        rocket.goto(((30), int(HEIGHT/2)))


        #movement
        #ROCKETX += SPEED
        #rocketRotate = pygame.transform.rotate(rocket, ROTATION)

        # Game loop part 1: Events #####
        for event in pygame.event.get():

        # this one checks for the window being closed
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()
                # add any other events here (keys, mouse, etc.)
                #if event.type == pygame.MOUSE:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    bholesL = []
                    running = False
                    pygame.quit()
                    sys.exit()
                if event.key == pygame.K_LEFT:
                    ROTATION = -45

                if event.key == pygame.K_RIGHT:
                    ROTATION = 45


            if event.type == pygame.MOUSEBUTTONDOWN:
                bholesL.append(Body(win, images[2], (50,50),  100, pygame.mouse.get_pos()))


        for thing in bholesL:
            if thing.overlaps(rocket):

                bholesL.remove(thing)
                del thing
                running = False
            elif thing.stLoc[0] <= 0 or thing.stLoc[1] <= 0 or thing.stLoc[0] >= WIDTH or thing.stLoc[1] >= HEIGHT:
                bholesL.remove(thing)
                del thing


        for thing in bholesL:
            thing.gotoBH()
    # after drawing, flip the display

    # update the display

        rocket.rotate(ROTATION)
        pygame.display.update()
    bholesL = []

# close the window
