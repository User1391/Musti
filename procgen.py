import pygame
import random
from settings import *
from physics import *


def procgen():
	rockYPos = random.randint(0, screenHeight)
	

	def addObj():
		asteroidL.append(Body(win, images[3], (50,50), 100))

timer = pygame.time.set_timer(addObj, 3000)