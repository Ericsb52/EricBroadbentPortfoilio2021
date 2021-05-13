# Pygame template - skeleton for a new pygame project
import pygame as pg
import random
import os
from settings import *
from bullet import *
vec = pg.math.Vector2



class Tower(pg.sprite.Sprite):

    def __init__(self,game,x,y,name):
        self.groups = game.all_sprites
        pg.sprite.Sprite.__init__(self,self.groups)
        self.g = game
        self.t_type = self.g.towers_selected[name-1]
        self.cost = name*100
        self.image = self.g.towers_dict[self.t_type]
        self.image = pg.transform.rotate(self.image,270)
        self.image = pg.transform.scale(self.image,(80,80))
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 2)
        self.pos = vec(x,y)
        self.placed = False
        self.health = 100
        self.lastshot = pg.time.get_ticks()
        self.shoot_delay = 1500
        self.inlane = False

    def check_inlane(self):
        InvBullet(self.g, self.rect.right,self.rect.centery,self)
        print("checking lane")





    def place_tower(self,x,y):
        self.placed = True
        self.pos = (x,y)
        self.g.towers_group.add(self)

    def shoot(self,game,x,y):
        if self.t_type==self.g.towers_selected[0]:
            b = Bullet(game,x,y+10)
            r = Bullet(game, x, y-10)
            self.shoot_delay = 800
        if self.t_type==self.g.towers_selected[1]:
            b = SmMissile(game,x,y)
            self.shoot_delay = 1500

        if self.t_type==self.g.towers_selected[2]:
            b = SmMissile(game,x,y+10)
            b = SmMissile(game, x, y-10)
            self.shoot_delay = 2500
        if self.t_type==self.g.towers_selected[3]:
            b = LgMissile(game,x,y)
            self.shoot_delay = 3000
        if self.t_type==self.g.towers_selected[4]:
            b = Bullet(game,x,y)
            self.shoot_delay = 400
        if self.t_type==self.g.towers_selected[5]:
            b = Bullet(game,x,y+10)
            r = Bullet(game, x, y-10)
            self.shoot_delay = 200





    def update(self):
        if self.placed == False:
            self.pos = self.g.mouse_pos

        now = pg.time.get_ticks()
        if now - self.lastshot > self.shoot_delay and self.placed:
            self.check_inlane()
            self.lastshot = now
            if self.inlane:
                self.shoot(self.g,self.rect.right,self.rect.centery)


        self.rect.center = self.pos

