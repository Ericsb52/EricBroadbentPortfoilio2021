import pygame as pg
import random
import os
from settings import *
vec = pg.math.Vector2

class ItemBar(pg.sprite.Sprite):
    def __init__(self,game,x,y,name):
        self.groups = game.all_sprites,game.hud_group
        self.g = game
        pg.sprite.Sprite.__init__(self,self.groups)
        self.item = name
        self.image = self.g.towers_dict[self.item]
        # self.image.fill(BROWN)
        self.rect = self.image.get_rect()
        self.pos = vec(x,y)
        self.rect.topleft = self.pos



