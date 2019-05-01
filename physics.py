import pygame
from settings import *
## PHYSICS ##
class Body(object):
    pygame = __import__('pygame')

    def __init__(self, frameName, img, size, mass=0):
        self.size = size
        self.mas = mass
        self.frameName = frameName
        self.image = pygame.transform.scale(img, self.size)


    def getSize(self):
        return self.size

    def getMass(self):
        return self.mas

    def getPos(self):
        return self.posi

    def getImg(self):
        return self.image

    def getframename(self):
        return self.frameName

    def goto(self, newPos):
        self.frameName.blit(self.image , newPos)
        return

    def scale(self, size):
        self.image = pygame.transform.scale(self.image, size)

        return

    def rotate(self, rotation):
        self.image = pygame.transform.rotate(self.image, rotation)
        return

    def drawClipRange (self):
        return self.image.fill(WHITE)
