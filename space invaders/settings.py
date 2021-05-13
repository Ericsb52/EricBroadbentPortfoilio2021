# Pygame template - skeleton for a new pygame project
import pygame as pg
import random as r
from os import *

game_folder = path.dirname(__file__)
img_folder = path.join(game_folder, 'img')
snd_folder = path.join(game_folder, 'snd')

TITLE = "Invaders"

WIDTH = 705 # width of our game window
HEIGHT = 680 # height of our game window
FPS = 30 # frames per second

font_name = pg.font.match_font("arial")

# Colors (R, G, B)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255,255,0)