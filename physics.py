import pygame
from settings import *
from pyganim import *
from functions import *
import math

## PHYSICS ##
class Body(object):
    pygame = __import__('pygame')
    def __init__(self, frameName, img, size, mass, loc, animArr = []):
        self._size = size
        self._mas = mass
        self._animA = animArr
        self.stLoc = loc
        self._frameName = frameName
        self._image = pygame.transform.scale(img, self._size)
        self._animObj = []
        self._rotAng = 0
        self._bhVect = (BHSPEED, 0)
        self.dist = 0
        if len(self._animA) != 0:
            for im in self._animA:
                self._animObj.append((im, 200))
            self._anim = PygAnimation(self._animObj)


    def getSize(self):
        return self._size

    def getMass(self):
        return self._mas

    def getPos(self):
        return self.stLoc

    def getImg(self):
        return self._image

    def getframename(self):
        return self._frameName.name()

    def goto(self, newPos):
        self._frameName.blit(self._image , newPos)
        self.stLoc = newPos
        return

    def scale(self, size):
        self._image = pygame.transform.scale(self._image, size)
        return

    def rotate(self, rotation):
        #self._rotAng +=
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

    def gotoBH(self):
        self.stLoc = tuplengine(self.stLoc, self._bhVect, '-')
        self._frameName.blit(self._image , self.stLoc)
        print("loc: ",self.stLoc)
        return

    def dest(self):
        del self
        return

    def overlaps(self, other):
        r1 = int(self._size[1]/2)
        r2 = int(other.getSize()[0]/2)
        c1 = self.stLoc
        c2 = other.getPos()
        self.dist = math.sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)
        if self.dist <= r1 + r2 and self.dist!=0:
            return True
        else:
            return False

    def update(self, accel):
        self._bhVect = (accel[0], accel[1]*-1)
        return

    def distance(self, other):
        c1 = self.stLoc
        c2 = other.getPos()
        return math.sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

    def xdist(self, other):
        c1 = self.stLoc
        c2 = other.getPos()
        return int(c1[0] - c2[0])

    def ydist(self, other):
        c1 = self.stLoc
        c2 = other.getPos()
        return int(c1[1] - c2[1])
