
import pygame as pg
import random
import os
from settings import *


class Ball(pg.sprite.Sprite):

    def __init__(self,game):

        self.g = game
        self.groups = self.g.all_sprites,self.g.ball_group
        pg.sprite.Sprite.__init__(self,self.groups)
        self.image = self.g.ball_img
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH /2, HEIGHT * .85)
        self.dx = 10
        self.dy = -10


    def update(self):
        self.rect.x += self.dx
        self.rect.y += self.dy
        if self.rect.right >= WIDTH or self.rect.left<=0:
            self.dx*=-1
        if self.rect.top <=0:
            self.dy*=-1
        hits = pg.sprite.spritecollide(self.g.player,self.g.ball_group,False)
        if hits:
            self.dy*=-1
            if self.g.player.speedx < 0:
                self.dx*=-1
            if self.g.player.speedx > 0:
                self.dx = 10
        if self.rect.top >= HEIGHT:
            self.kill()
        hits = pg.sprite.groupcollide(self.g.ball_group,self.g.block_group,False,True)
        if hits:
            self.dy*=-1


