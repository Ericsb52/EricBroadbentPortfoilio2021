import pygame as pg
import random
import os
from settings import *
vec = pg.math.Vector2



class Coin(pg.sprite.Sprite):
    def __init__(self,game,x,y):
        self.groups = game.coin_group, game.all_sprites
        pg.sprite.Sprite.__init__(self,self.groups)
        self.g = game
        self.image = self.g.coin_img
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)

    def update(self):
        hits = pg.sprite.groupcollide(self.g.coin_group, self.g.mouse_group, False, False)
        self.clicked = pg.mouse.get_pressed()
        if hits and self.clicked[0]==True:
            self.kill()
            self.g.cash += 100


