import pygame as pg
import random
import os
from settings import *
vec = pg.math.Vector2


class LillyPad(pg.sprite.Sprite):

    def __init__(self,game,x,y,w,h):
        self.g = game
        self.h = h
        self.w = w
        self.groups = self.g.all_sprites,self.g.lilly_pad_group
        pg.sprite.Sprite.__init__(self,self.groups)
        self.image = self.g.log_img
        self.image = pg.transform.scale(self.image,(int(w),int(h)))
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x
        self.rect.y = y
        self.frog_on = False
        self.uptime = 3500
        self.lastupdate = 0

    def update(self):
        if self.frog_on:
             now = pg.time.get_ticks()
             if now - self.lastupdate > self.uptime:
                 self.lastupdate = now
             else:
                 self.kill()


