# Pygame template - skeleton for a new pygame project
import sys

import pygame as pg
import random
from os import path
from settings import *
from player import *
from wall import *
from tilemap import *
from Cars import *
from people import *
from logs import *
from water import *
from lilypad import *


class Game(object):

    def __init__(self):
        self.running = True 
        # initialize pygame and create window
        pg.init()
        pg.mixer.init()  # for sound
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock()
        # key repeat rate
        pg.key.set_repeat(250,150)
        self.levelnum = levelnum
        self.level = level



    def loadData(self):
        self.map = TiledMap(path.join(map_folder, self.level))
        self.map_img = self.map.make_map()
        self.map_rect = self.map_img.get_rect()
        self.player_img = pg.image.load(path.join(img_folder,PLAYER_IMG)).convert_alpha()
        self.player_img = pg.transform.scale(self.player_img, (TILESIZE,TILESIZE)).convert_alpha()
        self.log_img = pg.image.load(path.join(img_folder, "log.PNG")).convert_alpha()

        cars_list = ["car1_blue.png","car2_green.png","car3_orange.png","car4_purple.png",
                     "car5_red.png","car6_yellow.png","car7_green.png",]
        self.cars_img = []
        for car in cars_list:
            img = pg.image.load(path.join(img_folder,car)).convert_alpha()
            self.cars_img.append(img)

        people_list = ["manBlue_hold.png", "manBrown_stand.png", "manOld_stand.png", "soldier1_hold.png",
                     "survivor1_hold.png", "survivor1_stand.png" ]
        self.people_img = []
        for people in people_list:
            img = pg.image.load(path.join(img_folder, people)).convert_alpha()
            self.people_img.append(img)




        self.Jump_animation = []
        for i in range(7):
            fn = "frog{}.png".format(i+1)
            img = pg.image.load(path.join(img_folder, fn))
            img = pg.transform.scale(img,(TILESIZE,TILESIZE))
            self.Jump_animation.append(img)






    def new(self):
        self.loadData()
        self.debug = False
        """start a new game"""
        # create sprite groups
        self.all_sprites = pg.sprite.Group()
        self.player_group = pg.sprite.Group()
        self.cars_group = pg.sprite.Group()
        self.walls_group = pg.sprite.Group()
        self.logs_group = pg.sprite.Group()
        self.people_group = pg.sprite.Group()
        self.water_group = pg.sprite.Group()
        self.kill_group = pg.sprite.Group()
        self.win_group = pg.sprite.Group()
        self.lilly_pad_group = pg.sprite.Group()

        # create game objects

        for tile_object in self.map.tmxdata.objects:
            if tile_object.name == "water":
                Water(self, tile_object.x, tile_object.y, tile_object.width, tile_object.height)
            if tile_object.name == "wallkill":
                Kill_wall(self, tile_object.x, tile_object.y, tile_object.width, tile_object.height)
            if tile_object.name == "win":
                win_wall(self, tile_object.x, tile_object.y, tile_object.width, tile_object.height)
            if tile_object.name == "wall":
                Obstacle(self,tile_object.x,tile_object.y,tile_object.width,tile_object.height)
            if tile_object.name == "car_r":
                Car(self,tile_object.x,tile_object.y,tile_object.width,tile_object.height,"r")
            if tile_object.name == "car_l":
                Car(self,tile_object.x,tile_object.y,tile_object.width,tile_object.height,"l")
            if tile_object.name == "people_r":
                People(self,tile_object.x,tile_object.y,tile_object.width,tile_object.height,True)
            if tile_object.name == "people_l":
                People(self,tile_object.x,tile_object.y,tile_object.width,tile_object.height,False)
            if tile_object.name == "log_r":
                Log(self, tile_object.x, tile_object.y, tile_object.width, tile_object.height, "r")
            if tile_object.name == "log_l":
                Log(self, tile_object.x, tile_object.y, tile_object.width, tile_object.height, "l")
            if tile_object.name == "lilly_pad":
                LillyPad(self, tile_object.x, tile_object.y, tile_object.width, tile_object.height)
            if tile_object.name == "player":
                self.player = Player(self, tile_object.x, tile_object.y)




        # create camera
        self.camera = Camera(self.map.width,self.map.height)




        self.run()



    def run(self):
        # Game Loop
        self.playing = True
        while self.playing:
            self.dt = self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()



    def events(self):
        # Game Loop - events

        for event in pg.event.get():
            # check for closing window clicking x
            if event.type == pg.QUIT:
                self.quit()
                # checking keyboard inputs
            if event.type == pg.KEYDOWN:
                # quiting game not program
                if event.key == pg.K_ESCAPE:
                    self.playing = False
                if event.key == pg.K_LEFT or event.key ==pg.K_a:
                    self.player.pos += vec(-16, 0)
                    self.player.dir = "LEFT"
                if event.key == pg.K_RIGHT or event.key == pg.K_d:
                    self.player.pos += vec(16, 0)
                    self.player.dir = "RIGHT"
                if event.key == pg.K_UP or event.key == pg.K_w:
                    self.player.pos += vec(0, -16)
                    self.player.dir = "IDLE"
                if event.key == pg.K_DOWN or event.key == pg.K_s:
                    self.player.pos += vec(0, 16)
                    self.player.dir = "DOWN"

                    # if keys[pg.K_LEFT] or keys[pg.K_a]:
                    #     self.pos += vec(-3, 0)
                    # if keys[pg.K_RIGHT] or keys[pg.K_d]:
                    #     self.pos += vec(3, 0)
                    # if keys[pg.K_UP] or keys[pg.K_w]:
                    #     self.pos += vec(0, -3)
                    # if keys[pg.K_DOWN] or keys[pg.K_s]:
                    #     self.pos += vec(0, 3)

    def next(self):
        self.levelnum += 1
        self.level = str.format("level{}.tmx",self.levelnum)
        self.new()
    def update(self):
        # Game Loop - update
        self.all_sprites.update()
        self.camera.update(self.player)

        hits = pg.sprite.spritecollide(self.player,self.cars_group,False)
        if hits:
            print("killed by car")
            self.playing = False
        hits = pg.sprite.spritecollide(self.player, self.people_group, False)
        if hits:
            print("killed by person")
            self.playing = False
        hits = pg.sprite.spritecollide(self.player, self.kill_group, False)
        if hits:
            print("killed wall on water")
            self.playing = False
        hits = pg.sprite.spritecollide(self.player, self.win_group, False)
        if hits:
            print("win")
            self.next()

        hits = pg.sprite.spritecollide(self.player,self.water_group,False)
        if hits and not self.player.on_log:
            print("killed by water")
            self.playing = False
        hits = pg.sprite.spritecollide(self.player,self.lilly_pad_group,false)
        if hits:
            print("on pad")
            hits[0].frog_on = True









    def draw(self):
        # Game Loop - draw
        self.screen.blit(self.map_img, self.camera.apply_rect(self.map_rect))

        for sprite in self.all_sprites:
            self.screen.blit(sprite.image, self.camera.apply(sprite))
            if self.debug:
                pg.draw.rect(self.screen,BLUE,self.camera.apply_rect(sprite.rect),1)
        if self.debug:
            self.draw_grid()
            for wall in self.walls_group:
                pg.draw.rect(self.screen, BLUE, self.camera.apply_rect(wall.rect), 1)

        # *after* drawing everything, flip the display
        pg.display.flip()

    def draw_grid(self):
        for x in range (0,WIDTH,TILESIZE):
            pg.draw.line(self.screen,DGREY,(x,0),(x,HEIGHT))
        for y in range (0,HEIGHT,TILESIZE):
            pg.draw.line(self.screen,DGREY,(0,y),(WIDTH,y))

    def show_start_screen(self):
        pass

    def show_GO_screen(self):
        pass

    def quit(self):
        pg.quit()
        sys.exit()

g = Game()
g.show_start_screen()
while g.running:
    g.new()
    g.show_GO_screen()

pg.quit()
