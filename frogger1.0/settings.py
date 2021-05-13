# Pygame template - skeleton for a new pygame project
import pygame as pg
import random
from os import path
vec = pg.math.Vector2


def collide_hit_rect(one,two):
    return one.hit_rect.colliderect(two.rect)

def collide_with_walls(sprite,group, dir):
    if dir == "x":
        hits = pg.sprite.spritecollide(sprite, group, False, collide_hit_rect)
        if hits:
            if hits[0].rect.centerx > sprite.hit_rect.centerx:
                sprite.pos.x = hits[0].rect.left - sprite.hit_rect.width / 2
            if hits[0].rect.centerx < sprite.hit_rect.centerx:
                sprite.pos.x = hits[0].rect.right + sprite.hit_rect.width / 2
            sprite.vel.x = 0
            sprite.hit_rect.centerx = sprite.pos.x
    if dir == "y":
        hits = pg.sprite.spritecollide(sprite, group, False, collide_hit_rect)
        if hits:
            if hits[0].rect.centery > sprite.hit_rect.centery:
                sprite.pos.y = hits[0].rect.top - sprite.hit_rect.width / 2
            if hits[0].rect.centery < sprite.hit_rect.centery:
                sprite.pos.y = hits[0].rect.bottom + sprite.hit_rect.width / 2
            sprite.vel.y = 0
            sprite.hit_rect.centery = sprite.pos.y

# set up asset folders
game_folder = path.dirname(__file__)
img_folder = path.join(game_folder, 'img')
snd_folder = path.join(game_folder, 'snd')
map_folder = path.join(game_folder,"maps")

true = True
false = False

# game window settings
TITLE = "Template"
WIDTH = 768  # width of our game window
HEIGHT =1024 # height of our game window
FPS = 30 # frames per second

# Colors (R, G, B)
# Colors (R, G, B)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
GREY = (128,128,128)
LBLUE = (0,128,255)
DGREEN = (0,102,0)
DGREY = (96,96,96)
BROWN = (139,69,19)

# Grid settings
TILESIZE = 32
GRIDWIDTH = WIDTH/TILESIZE
GRIDHEIGHT = HEIGHT/TILESIZE

# plaYER SETTINGS
PLAYER_IMG ="frog1.png"
PLAYER_ROT_SPEED = .1
PLAYER_HIT_RECT = pg.Rect(0,0,35,35)
PLAYER_SPEED = .1

levelnum = 1
level = "level1.tmx"

