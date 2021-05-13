# Pygame template - skeleton for a new pygame project
import pygame as pg
import random
import os
from settings import *
vec = pg.math.Vector2

class Water(pg.sprite.Sprite):

    def __init__(self,game,x,y,w,h,):
        self.g = game
        self.groups = self.g.water_group
        pg.sprite.Sprite.__init__(self,self.groups)
        self.rect = pg.Rect(x,y,w,h)
        self.x = x
        self.y = y
        self.rect.x = x
        self.rect.y = y