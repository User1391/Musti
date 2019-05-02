import pygame
import tkinter as tk

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

# Variables
SPEED = 4
ROCKETX = 0
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
