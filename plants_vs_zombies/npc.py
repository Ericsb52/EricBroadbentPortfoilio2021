# Pygame template - skeleton for a new pygame project
import pygame as pg
import random
import os
from settings import *
from coin import *
vec = pg.math.Vector2



class NPC(pg.sprite.Sprite):
    def __init__(self,game,x,y):
        self.groups = game.enemy_group, game.all_sprites
        pg.sprite.Sprite.__init__(self,self.groups)
        self.g = game
        self.choiceList = [0,0,0,0,0,1,1,1,1,2,2,2,3,3,4]
        self.etype = random.choice(self.choiceList)
        self.image = self.g.enemy_imgs[self.etype]
        self.image.set_colorkey(BLUE)
        self.speed = 0
        self.health = 100
        if self.etype == 0:
            self.health = 100
            self.speed = 3
        elif self.etype == 1:
            self.health == 150
            self.speed = 2.5
        elif self.etype == 2:
            self.health == 200
            self.speed = 2
        elif self.etype == 3:
            self.health == 250
            self.speed = 1
        elif self.etype == 4:
            self.health == 300
            self.speed = .5

        self.rect = self.image.get_rect()
        self.rect.center = (x,y)

    def update(self):
        self.rect.x -= self.speed

        hits = pg.sprite.groupcollide(self.g.bullet_group, self.g.enemy_group, True, False)
        for hit in hits:
            print("hit")
            self.health -= hit.dmg

        # if self.rect.left < 0:
        #     self.g.playing = False

        if self.health <= 0:
            x= random.randint(0,100)
            if x >= 75:
                Coin(self.g,self.rect.centerx,self.rect.centery)
            self.kill()