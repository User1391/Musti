import pygame
import tkinter as tk
import random


# fullscreenmode stuff
root = tk.Tk()

screenWidth = root.winfo_screenwidth()
screenHeight = root.winfo_screenheight()

# Colors
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
FUCHSIA = (255, 0, 255)
GRAY = (128, 128, 128)
LIME = (0, 128, 0)
MAROON = (128, 0, 0)
NAVYBLUE = (0, 0, 128)
OLIVE = (128, 128, 0)
PURPLE = (128, 0, 128)
RED = (255, 0, 0)
SILVER = (192, 192, 192)
TEAL = (0, 128, 128)
YELLOW = (255, 255, 0)
ORANGE = (255, 128, 0)
CYAN = (0, 255, 255)
OUTER_SPACE = (13, 5, 14)

# Constants
WIDTH = screenWidth
HEIGHT = screenHeight
SCREENTYPE = pygame.FULLSCREEN
FPS = 60
BGCOLOR = BLACK
#GRAVCONST = 6.673*(10**-11)

# Variables
SPEED = 3
BHSPEED = 7
ROCKETX = 100
ROCKETY = 100
GRAVITY = 0
ASTERX = 0
ASTERY = 25
ROTATION = 45
# Edited Variables
ROCKETX += SPEED

# Masses

ROCKET_MASS = 125
ASTEROID_MASS = 10



#background function:

BACKGROUNDX = 0
BACKGROUNDY= 0
TILEWIDTH = 64
TILEHEIGHT = 64
AMNTX = WIDTH // TILEWIDTH
AMNTY = HEIGHT // TILEHEIGHT
ROTATIONVAR = 0

def rotation():
	RANDOM = random.randint(1,4)
	if RANDOM == 1:
		ROTATIONVAR = 0
	elif RANDOM == 2:
		ROTATIONVAR = 90
	elif RANDOM == 3:
		ROTATIONVAR = 180
	else:
		ROTATIONVAR = 270



def createImage(self, screen):
	display = self.screen
	rotation()
	display.blit(images[4], (BACKGROUNDX, BACKGROUNDY))
	pygame.transform.rotate(ROTATIONVAR)

def fillScreen():
	for y in range(AMNTY):
		createImage()
		BACKGROUNDY += TILEHEIGHT
		for x in range(AMNTX):
			createImage()
			BACKGROUNDX += TILEWIDTH


ROCKET_MASS = 1000
ASTEROID_MASS = 10000
