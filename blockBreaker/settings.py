# Pygame template - skeleton for a new pygame project
import pygame
import random
import os


# set up asset folders
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, 'img')
snd_folder = os.path.join(game_folder, 'snd')


TITLE = "Block Breaker"

WIDTH = 480  # width of our game window
HEIGHT = 600 # height of our game window
FPS = 30 # frames per second

# Colors (R, G, B)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
GREY = (64,64,64)



