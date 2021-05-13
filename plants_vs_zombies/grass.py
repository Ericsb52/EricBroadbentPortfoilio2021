import pygame as pg
import random
import os
from settings import *
vec = pg.math.Vector2


class Grass(pg.sprite.Sprite):
    def __init__(self, game, x, y, color):
        self.groups = game.all_sprites, game.grass_group
        self.g = game
        pg.sprite.Sprite.__init__(self, self.groups)
        self.image = self.image = pg.Surface((TILESIZE, TILESIZE))
        self.open = True
        if color % 2 == 0:
            self.image = self.g.grass_imgs[0]
        else:
            self.image = self.g.grass_imgs[1]

        self.rect = self.image.get_rect()
        self.pos = vec(x, y)
        self.rect.topleft = self.pos