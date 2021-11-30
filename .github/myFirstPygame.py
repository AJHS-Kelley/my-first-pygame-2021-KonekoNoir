# My First PyGame, Kenyon Smith, 11/30/2021 ,12:13, v0.0

import pygame, sys
from pygame.locals import* 

# Initialize PyGame
pygame.init()

# Setup the Window to draw on.
windowSurface = pygame.display.set_mode((500, 400), 0, 32)
pygame.display.set_caption ('My First Python') 

# Setup color values. 
BLACK = (0,0,0)
WHITE = (255.255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
EARTHFLAME = (75,45,0)


# Setup the fonts