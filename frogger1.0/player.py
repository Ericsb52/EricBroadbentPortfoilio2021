# Pygame template - skeleton for a new pygame project
import pygame as pg
import random
import os
from settings import *
vec = pg.math.Vector2


class Player(pg.sprite.Sprite):
    def __init__(self,game,x,y):
        self.groups = game.all_sprites
        pg.sprite.Sprite.__init__(self,self.groups)
        self.g = game
        self.dir = "IDLE"
        self.pn_log = False
        self.image = self.g.Jump_animation[0]
        self.frame = 0
        self.last_update = pg.time.get_ticks()
        self.frame_rate = 120
        self.rect = self.image.get_rect()
        self.hit_rect = PLAYER_HIT_RECT
        self.hit_rect.center = self.rect.center
        self.vel = vec(0, 0)
        self.pos = vec(x, y)
        self.rot = 0



    def update(self):



        self.pos += self.vel * self.g.dt
        if self.dir == "IDLE":
            self.rot = 0
        if self.dir == "LEFT":
            self.rot = 90
        if self.dir == "RIGHT":
            self.rot = 270
        if self.dir == "DOWN":
            self.rot = 180
        self.image = pg.transform.rotate(self.g.player_img, self.rot)
        self.rect = self.image.get_rect()
        self.rect.center = self.pos
        self.hit_rect.centerx = self.pos.x
        collide_with_walls(self, self.g.walls_group, "x")
        self.hit_rect.centery = self.pos.y
        collide_with_walls(self, self.g.walls_group, "y")
        self.rect.center = self.hit_rect.center
        hits = pg.sprite.spritecollide(self, self.g.logs_group, False)
        if hits:
            self.on_log = True
        else:
            self.on_log = False
        if self.on_log:
            self.pos.x = hits[0].rect.centerx




