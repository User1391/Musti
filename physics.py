import pygame
from settings import *
from pyganim import *
## PHYSICS ##
class Body(object):
    pygame = __import__('pygame')
    def __init__(self, frameName, img, size, mass, animArr = []):
        self._size = size
        self._mas = mass
        self._animA = animArr
        self._frameName = frameName
        self._image = pygame.transform.scale(img, self._size)
        self._animObj = []
        if len(self._animA) != 0:
            for im in self._animA:
                self._animObj.append((im, 200))
            self._anim = PygAnimation(self._animObj)


    def getSize(self):
        return self._size

    def getMass(self):
        return self._mas

    def getPos(self):
        return self._posi

    def getImg(self):
        return self._image

    def getframename(self):
        return self._frameName.name()

    def goto(self, newPos):
        self._frameName.blit(self._image , newPos)
        return

    def scale(self, size):
        self._image = pygame.transform.scale(self._image, size)
        return

    def rotate(self, rotation):
        self._image = pygame.transform.rotate(self._image, rotation)
        return

    def stopAnim(self):
        if len(self._animA) != 0:
            self._anim.stop()
        return

    def pausAnim(self):
        if len(self._animA) != 0:
            self._anim.pause()
        return

    def playAnim(self):
        return self._anim.stop()


    def blit(self, loc):
        return self._anim.blit(self._frameName, loc)
