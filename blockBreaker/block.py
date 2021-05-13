# Pygame template - skeleton for a new pygame project
import pygame as pg
import random
import os
from settings import *



class Block(pg.sprite.Sprite):
    def __init__(self,game,x,y):
        self.groups = game.all_sprites,game.block_group
        pg.sprite.Sprite.__init__(self,self.groups)
        self.g = game
        self.image = random.choice(self.g.block_imgs)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.destroyed = False

    def update(self):
        if self.destroyed == True:
            self.kill()


class Paddle(pg.sprite.Sprite):
    def __init__(self,game,x,y):
        self.g = game
        self.groups = game.all_sprites
        pg.sprite.Sprite.__init__(self,self.groups)
        self.image = self.g.paddle_img
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)
        self.speedx = 0

    def update(self):
        self.speedx = 0
        keystate = pg.key.get_pressed()
        if keystate[pg.K_RIGHT] or keystate[pg.K_d]:
            self.speedx = 15
        if keystate[pg.K_LEFT] or keystate[pg.K_a]:
            self.speedx = -15
        self.rect.x += self.speedx
        if self.rect.centerx >= WIDTH:
            self.rect.centerx = WIDTH
        if self.rect.centerx < 0:
            self.rect.centerx = 0