# Pygame template - skeleton for a new pygame project
import pygame as pg
import random
import os
vec = pg.math.Vector2

# set up asset folders
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, 'img')
snd_folder = os.path.join(game_folder, 'snd')


TITLE = "tower defence"


font_name = pg.font.match_font('arial')

WIDTH = 1025  # width of our game window
HEIGHT = 1025 # height of our game window
FPS = 30 # frames per second

TILESIZE = 128
GRIDWIDTH = WIDTH / TILESIZE
GRIGHEIGHT= HEIGHT/TILESIZE

# Colors (R, G, B)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
YELLOW = (255,255,0)
BLUE = (0, 0, 255)
GREY = (128,128,128)
LBLUE = (0,128,255)
DGREEN = (0,102,0)
DGREY = (96,96,96)
BROWN = (139,69,19)

ITEMSPOTS = 6





