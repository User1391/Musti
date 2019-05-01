import pygame
## PHYSICS ##
class Body(object):
    pygame = __import__('pygame')
    def __init__(self, frameName, img, name, mass=0):
        self.nam = name
        self.mas = mass
        self.frameName = frameName
        self.image = img

    def name(self):
        return self.nam

    def mass(self):
        return self.mas

    def pos(self):
        return self.posi

    def img(self):
        return self.image

    def framename(self):
        return self.frameName

    def mov(self, newPos):
        self.frameName.blit(self.image , newPos)
        return

    def scaleImg(self, size):
        self.image = pygame.transform.scale(self.image, size)
        return

    def rotate(self, rotation):
        self.image = pygame.transform.rotate(self.image, rotation)
        return
