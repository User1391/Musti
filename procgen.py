import pygame
import random
from settings import *

obstacleYPos = random.randint(0, HEIGHT)
class Obstacle():
	pygame = __import__('pygame')

	def __init__(self, frameName, x, y, size, img, speed, mass=0 ):
		self.size = size
		self.mas = mass
		self.x, self.y = x, y
		self.speed = spd
		self.image = pygame.transform.scale(img, self.size)

	def getSize(self):
		return self.size

	def getMass(self):
		return self.mas
		
	def getPos(self):
		return self.x, self.y

    def getImg(self):
        return self.image
    def getSpeed(self):
    	return self.spd

    def getframename(self):
        return self.frameName

    def goto(self, newPos):
        self.frameName.blit(self.image , newPos)
        return

    def scale(self, size):
        self.image = pygame.transform.scale(self.image, size)
        return
