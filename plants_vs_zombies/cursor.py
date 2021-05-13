# Pygame template - skeleton for a new pygame project
import pygame as pg
import random
import os
from settings import *
vec = pg.math.Vector2

class Pointer(pg.sprite.Sprite):
    def __init__(self,game):
        self.groups = game.all_sprites,game.mouse_group
        pg.sprite.Sprite.__init__(self,self.groups)
        self.g = game
        self.image = self.g.mouse_img
        # self.image.fill(GREEN)
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 2)
        self.held = False

    def update(self):
        self.rect .topleft = self.g.mouse_pos
        clicked = pg.mouse.get_pressed()



