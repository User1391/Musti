import random
import sys
from settings import *
from pyganim import *
from physics import *
from intro import *
from procgen import *


# initialize pygame
pygame.init()
# initialize sound - uncomment if you're using sound
# pygame.mixer.init()
# create the game window and set the title200
win = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)
pygame.display.set_caption("Space Create")



# Sprites
images = [pygame.image.load('imgs/Rocket.png'), pygame.image.load('imgs/Asteroid.png'), pygame.image.load('imgs/BlackHole.png')]
images = [pygame.image.load('imgs/Rocket.png'), pygame.image.load('imgs/Asteroid.png'), pygame.image.load('imgs/BlackHole.png')]

## rocket ##
rocketAnim = ['imgs/Rocket.png', 'imgs/RocketEx1.png', 'imgs/RocketEx2.png', 'imgs/RocketEx3.png']
rocket = Body(win, images[0], (60, 35), ROCKET_MASS, (ROCKETX, ROCKETY))

#######
# asteroid
asteroid = Body(win, images[3], (200,200), ASTEROID_MASS)
asteroidL = []
# black hole
#bhole = Body(win, images[2], (100,100), ROCKET_MASS)
bholesL = []




# start the clock
clock = pygame.time.Clock()

menu(win, clock)
# set the 'running' variable to False to end the game
running = True
# start the game loop

while running:
    win.fill(OUTER_SPACE)
    # keep the loop running at 0the right speed

    clock.tick(FPS)

    #rocket.goto((ROCKETX, ROCKETY))



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
        #if event.type == pygame.MOUSE:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
                pygame.quit()
                sys.exit()
            if event.key == pygame.K_LEFT:
                ROTATION = -45
            if event.key == pygame.K_RIGHT:
                ROTATION = 45
        if event.type == pygame.MOUSEBUTTONDOWN:
            bholesL.append(Body(win, images[2], (50,50),  100, (ASTERX, ASTERY)))

    for thing in bholesL:
        thing.gotoBH()
    # after drawing, flip the display

    # update the display


    pygame.display.update()

# close the window
