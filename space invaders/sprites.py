# Pygame template - skeleton for a new pygame project
import pygame as pg
import random as r
from os import *

from settings import *


class Player(pg.sprite.Sprite):
    def __init__(self,game):
        self.g = game
        pg.sprite.Sprite.__init__(self)
        self.image = self.g.player_imgs[0]
        self.image = pg.transform.scale(self.image, (40, 40))
        # self.image.fill(GREEN)
        # self.image = player_img
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        self.radius = self.rect.width * .75 / 2
        self.rect.center = (WIDTH / 2, HEIGHT -15)
        self.speedx = 0
        self.shoot_delay = 400
        self.last_shot = pg.time.get_ticks()
        self.lives = 3
        self.frame = 0
        self.last_ani_update = pg.time.get_ticks()
        self.framerate = 50

    def animate(self):
        now =pg.time.get_ticks()
        if now - self.last_ani_update >self.framerate:
            self.last_ani_update = now
            self.frame+=1
            if self.frame == len(self.g.player_imgs):
                self.frame = 0
            center = self.rect.center
            self.image = self.g.player_imgs[self.frame]
            self.image = pg.transform.scale(self.image, (40, 40))
            self.image.set_colorkey(WHITE)
            self.rect = self.image.get_rect()
            self.rect.center = center

    def update(self):
        # basic movment side to side

        self.animate()
        self.speedx = 0
        keystate = pg.key.get_pressed()
        if keystate[pg.K_LEFT] or keystate[pg.K_a]:
            self.speedx = -5
        if keystate[pg.K_RIGHT] or keystate[pg.K_d]:
            self.speedx = 5
        if keystate[pg.K_SPACE]:
            self.shoot()

        self.rect.x += self.speedx

    def shoot(self):
        now = pg.time.get_ticks()
        if now - self.last_shot > self.shoot_delay:
            self.last_shot = now
            self.g.player_shoot.play()
            b = Bullet(self.g,self.rect.centerx,self.rect.top+1)
            self.g.all_sprites.add(b)
            self.g.bullet_group.add(b)


class Bullet(pg.sprite.Sprite):
    def __init__(self,game,x,y):
        super(Bullet, self).__init__()
        self.g = game
        self.color = "blue"
        self.image = self.g.bul_img[self.color]
        self.image = pg.transform.scale(self.image, (5, 15))
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.centerx = x
        self.radius = self.rect.width * .75 / 2
        self.speed = -10
        self.spread = 0

    def inc_spred(self,num):
        self.spread = num

    def update(self):
        self.rect.y += self.speed
        self.rect.x += self.spread
        # kill bullet when bottom <0
        if self.rect.bottom < 0:
            self.kill()

class NPC_Bullet(Bullet):
    def __init__(self,game,x,y):
        super(NPC_Bullet, self).__init__(game,x,y)
        self.color ="red"
        self.image = self.g.bul_img[self.color]
        self.image = pg.transform.scale(self.image, (5, 15))
        self.speed = 10


    def update(self):
        self.rect.y += self.speed
        self.rect.x += self.spread
        # kill bullet when bottom <0
        if self.rect.bottom > HEIGHT:
            self.kill()



class NPC(pg.sprite.Sprite):
    count = 0
    movex = 41
    movey = 25
    moving_right = False
    move_down = False
    moveTimer = 800
    shootTimer = pg.time.get_ticks()
    shoot_delay = 1500


    def __init__(self,x,y,game):
        super(NPC, self).__init__()
        self.g = game
        self.image = self.g.npc_imgs[0]
        self.image = pg.transform.scale(self.image, (40, 40))
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        self.radius = self.rect.width * .75 / 2
        self.last_update = pg.time.get_ticks()
        self.rect.top = y
        self.rect.left = x
        self.down_timer = pg.time.get_ticks()
        self.speedx = 0
        self.speedy = 0
        self.points = 100
        self.frame = 0
        self.last_ani_update = pg.time.get_ticks()
        self.framerate = 50


    def animate(self):
        now =pg.time.get_ticks()
        if now - self.last_ani_update >self.framerate:
            self.last_ani_update = now
            self.frame+=1
            if self.frame == len(self.g.npc_imgs):
                self.frame = 0
            center = self.rect.center
            self.image = self.g.npc_imgs[self.frame]
            self.image = pg.transform.scale(self.image, (40, 40))
            self.image.set_colorkey(WHITE)
            self.rect = self.image.get_rect()
            self.rect.center = center

    def moveright(self):
        now = pg.time.get_ticks()
        if now - self.last_update > NPC.moveTimer:
            self.last_update = now
            if NPC.moving_right:
                self.speedx = NPC.movex
            else:
                self.speedx = NPC.movex*-1


    def movedown(self):
        NPC.move_down = False
        for i in self.g.npc_group:
            i.rect.top += NPC.movey
        if NPC.moveTimer > 200:
            NPC.moveTimer -= 25
            print(NPC.moveTimer)

    def shoot(self):
        x=self.rect.centerx
        y=self.rect.bottom
        now = pg.time.get_ticks()
        if now - NPC.shootTimer > NPC.shoot_delay:
            NPC.shootTimer = now
            self.g.npc_shoot.play()
            npc_bullet = NPC_Bullet(self.g,x,y)
            self.g.npc_bullet_group.add(npc_bullet)
            self.g.all_sprites.add(npc_bullet)


    def update(self):
        self.animate()
        NPC.move_down = False
        self.speedx = 0
        shooter = r.choice(self.g.shooterlist)
        shooter.shoot()
        if self.rect.right > WIDTH-5 and NPC.moving_right:
            NPC.moving_right = False
            NPC.move_down = True
        if self.rect.left < 0 and not NPC.moving_right:
            NPC.moving_right = True
            NPC.move_down = True
        if NPC.move_down == True and pg.time.get_ticks()-self.down_timer > 1000:
            self.down_timer = pg.time.get_ticks()
            NPC.move_down = False
            self.movedown()
        self.moveright()
        self.rect.centerx+=self.speedx

        if NPC.moveTimer <= 250:
            NPC.moveTimer = 250

class Bunker(pg.sprite.Sprite):

    def __init__(self,game,x,y):
        super(Bunker, self).__init__()
        self.g = game
        self.image = pg.Surface((10, 10))
        self.image.fill(YELLOW)
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)


