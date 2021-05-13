import pygame as pg
import random
import os
from settings import *


class Wall(pg.sprite.Sprite):

    def __init__(self,game,x,y,w,h):
        self.g = game
        self.groups = self.g.all_sprites, self.g.walls_group
        pg.sprite.Sprite.__init__(self,self.groups)
        self.image = pg.Surface((w,h))
        self.image.fill(BROWN)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x
        self.rect.y = y


class Obstacle(pg.sprite.Sprite):

    def __init__(self,game,x,y,w,h,):
        self.g = game
        self.groups = self.g.walls_group
        pg.sprite.Sprite.__init__(self,self.groups)
        self.rect = pg.Rect(x,y,w,h)
        self.x = x
        self.y = y
        self.rect.x = x
        self.rect.y = y



class Kill_wall(pg.sprite.Sprite):

    def __init__(self,game,x,y,w,h,):
        self.g = game
        self.groups = self.g.kill_group
        pg.sprite.Sprite.__init__(self,self.groups)
        self.rect = pg.Rect(x,y,w,h)
        self.x = x
        self.y = y
        self.rect.x = x
        self.rect.y = y

class win_wall(pg.sprite.Sprite):

    def __init__(self,game,x,y,w,h,):
        self.g = game
        self.groups = self.g.win_group
        pg.sprite.Sprite.__init__(self,self.groups)
        self.rect = pg.Rect(x,y,w,h)
        self.x = x
        self.y = y
        self.rect.x = x
        self.rect.y = y