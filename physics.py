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
        self._rocketAnim = ['imgs/Rocket.png', 'imgs/RocketEx1.png', 'imgs/RocketEx2.png', 'imgs/RocketEx3.png']
        self._animObj = []
        if len(self._animA) != 0:
            for im in self._animA:
                self._animObj.append((im, 200))
            self._anim = PygAnimation(self._animObj)
            self._anim.play()
            
    def getSize(self):
        return self._size

    def getMass(self):
        return self._mas

    def getPos(self):
        return self._posi

    def getImg(self):
        return self._image

    def getframename(self):
        return self._frameName

    def goto(self, newPos):
        self._frameName.blit(self._image , newPos)
        return

    def scale(self, size):
        self._image = pygame.transform.scale(self._image, size)
        return

    def rotate(self, rotation):
        self._image = pygame.transform.rotate(self._image, rotation)
        return

    def animate(self):
        self._anim.play()
        return
