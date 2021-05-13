import pygame as pg
import random
import os
from settings import *
vec = pg.math.Vector2


class Log(pg.sprite.Sprite):

    def __init__(self,game,x,y,w,h,dir):
        self.g = game
        self.h = h
        self.w = w
        self.dir = dir
        self.groups = self.g.all_sprites,self.g.logs_group
        pg.sprite.Sprite.__init__(self,self.groups)
        self.image = self.g.log_img
        self.image = pg.transform.scale(self.image,(int(w),int(h)))
        self.image.set_colorkey(BLACK)
        if self.dir == "r":
            self.speedx = -5
        else:
            self.speedx = 5
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x
        self.rect.y = y

    def update(self):
        self.rect.x += self.speedx

        if self.rect.right < -100:
            self.rect.left = WIDTH + random.randint(50,100)
            if self.dir == "r":
                self.speedx = random.randint(-7, -3)
            else:
                self.speedx = random.randint(3, 7)
        if self.rect.left > WIDTH + 100:
            self.rect.right = 0 - random.randint(50, 100)
            if self.dir == "r":
                self.speedx = random.randint(-7, -3)
            else:
                self.speedx = random.randint(3, 7)