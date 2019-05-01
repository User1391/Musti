import pygame
## PHYSICS ##
class Body:
    def __init__(self, name, mass, posX, posY):
        self.name = name
        self.mass = mass
        self.pos = (posX, posY)
    def name(self):
        return self.name
    def mass(self):
        return self.mass
    def pos(self):
        return self.pos
