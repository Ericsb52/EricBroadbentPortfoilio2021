# Pygame template - skeleton for a new pygame project
import pygame as pg
import random
import os
from settings import *
vec = pg.math.Vector2

class InvBullet(pg.sprite.Sprite):
    def __init__(self,game,x,y,tower):
        self.groups = game.inv_group,game.all_sprites
        pg.sprite.Sprite.__init__(self,self.groups)
        self.g = game
        self.tower = tower
        self.image = pg.Surface((5,5))
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.centery = y
        self.rect.left = x
        self.speedx = 50


    def update(self):
        self.rect.x += self.speedx
        if self.rect.left > WIDTH:
            self.tower.inlane = False
            self.kill()
        hits = pg.sprite.spritecollide(self,self.g.enemy_group,False)
        if hits:
            print(self.tower.inlane)
            self.tower.inlane = True
            print(self.tower.inlane)

            self.kill()


class Bullet(pg.sprite.Sprite):
    def __init__(self,game,x,y):
        self.groups = game.bullet_group, game.all_sprites
        pg.sprite.Sprite.__init__(self,self.groups)
        self.g = game
        self.image = self.g.bullet_img
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.centery = y
        self.rect.left = x
        self.speedx = 30
        self.dmg = 5

    def update(self):
        self.rect.x += self.speedx
        if self.rect.right > WIDTH:
            self.kill()

class SmMissile(pg.sprite.Sprite):
    def __init__(self,game,x,y):
        self.groups = game.bullet_group, game.all_sprites
        pg.sprite.Sprite.__init__(self,self.groups)
        self.g = game
        self.image =self.g.smMissile_img
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.centery = y
        self.rect.left = x
        self.speedx = 15
        self.dmg = 25

    def update(self):
        self.rect.x += self.speedx
        if self.rect.left > WIDTH:
            self.kill()

class LgMissile(pg.sprite.Sprite):
    def __init__(self,game,x,y):
        self.groups = game.bullet_group, game.all_sprites
        pg.sprite.Sprite.__init__(self,self.groups)
        self.g = game
        self.image = self.g.lgMissile_img
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.centery = y
        self.rect.left = x
        self.speedx = 5
        self.dmg = 100

    def update(self):
        self.rect.x += self.speedx
        if self.rect.left > WIDTH:
            self.kill()