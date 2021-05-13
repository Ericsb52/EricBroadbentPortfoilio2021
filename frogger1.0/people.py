import pygame as pg
import random
import os
from settings import *
vec = pg.math.Vector2


class People(pg.sprite.Sprite):

    def __init__(self,game,x,y,w,h,dir):
        self.g = game
        self.h = h
        self.w = w
        self.dir = dir
        self.groups = self.g.all_sprites,self.g.people_group
        pg.sprite.Sprite.__init__(self,self.groups)
        self.image = random.choice(self.g.people_img)
        self.image = pg.transform.scale(self.image,(int(h),int(w)))
        if self.dir:
            self.image = pg.transform.rotate(self.image,180)
            self.speedx = -5
        else:
            self.image = pg.transform.rotate(self.image, 0)
            self.speedx = 5
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x
        self.rect.y = y
        self.lasthit = 0

    def update(self):
        self.rect.x += self.speedx

        if self.rect.right < -100:
            self.rect.left = WIDTH + random.randint(25,50)
            self.image = random.choice(self.g.people_img)
            self.image = pg.transform.scale(self.image, (int(self.h), int(self.w)))
            if self.dir:
                self.image = pg.transform.rotate(self.image, 180)
                self.speedx = random.randint(-10, -5)
            else:
                self.image = pg.transform.rotate(self.image, 0)
                self.speedx = random.randint(5, 10)
        if self.rect.left > WIDTH + 100:
            self.rect.right = 0 - random.randint(25, 50)
            self.image = random.choice(self.g.people_img)
            self.image = pg.transform.scale(self.image, (int(self.h), int(self.w)))
            if self.dir:
                self.image = pg.transform.rotate(self.image, 180)
                self.speedx = random.randint(-10, -5)
            else:
                self.image = pg.transform.rotate(self.image, 0)
                self.speedx = random.randint(5, 10)


