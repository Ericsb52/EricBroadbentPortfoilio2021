# Pygame template - skeleton for a new pygame project
import pygame as pg
import random
vec = pg.math.Vector2
from os import path
from settings import *
from npc import *
from itemBar import *
from cursor import *
from tower import *
from grass import *



class Game(object):

    def __init__(self):
        self.running = True
        # initialize pygame and create window
        pg.init()
        pg.mixer.init()  # for sound
        pg.mouse.set_visible(False)
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock()
        self.towers_dict = {}
        self.itemspots = []
        self.load_data()
        self.can_click_mouse = True
        self.mouse_pos = vec(0,0)
        self.click_timer = pg.time.get_ticks()
        self.cash = 2000
        self.wave_length = 10000
        self.spawntime = 2500
        self.last_spawn = pg.time.get_ticks()


    def load_data(self):
        for i in range(6):
            fn = "tower_img{}.png".format(i)
            try:
                img = pg.image.load(path.join(img_folder, fn)).convert()
                img = pg.transform.scale(img,(100,100))
                self.towers_dict ["tower{}".format(i+1)] = []
                self.towers_dict ["tower{}".format(i+1)] = img
            except:
                print("cant load imgs")
        self.mouse_img = pg.image.load(path.join(img_folder, "fingerpointer.png")).convert()
        self.mouse_img = pg.transform.scale(self.mouse_img,(50,50))
        self.grass_imgs=[]
        for i in range(2):
            fn = "grass{}.png".format(i+1)
            img = pg.image.load(path.join(img_folder, fn)).convert()
            img = pg.transform.scale(img,(128,128))
            self.grass_imgs.append(img)
        self.enemy_imgs = []
        try:
            self.test_img = pg.image.load(path.join(img_folder, "enemy3.png")).convert()
            for i in range(5):
                fn = "enemy{}.png".format(i+1)
                img = pg.image.load(path.join(img_folder, fn)).convert()
                img = pg.transform.scale(img, (100, 100))
                self.enemy_imgs .append(img)
        except:
            print("somthing went wrong")
        self.test_img = pg.image.load(path.join(img_folder, "enemy2.png")).convert()
        self.bullet_img = pg.image.load(path.join(img_folder, "bullet.png")).convert()
        self.smMissile_img = pg.image.load(path.join(img_folder, "smmissile.png")).convert()
        self.lgMissile_img = pg.image.load(path.join(img_folder, "lgmissile.png")).convert()
        self.coin_img = pg.image.load(path.join(img_folder, "coin.png")).convert()
        self.coin_img = pg.transform.scale(self.coin_img,(90,90))



    def create_hud(self):
        for i in range(ITEMSPOTS):
            x = ItemBar(self,15+i*128,15,self.towers_selected[i])
            self.itemspots.append(x)
    def create_grass(self):
        count =0
        for i in range(8):
            for y in range(8):
                print("making grass")
                x = Grass(self,i*128,128+y*128,count)
                count+=1
            count-=1






    def new(self):
        """start a new game"""
        # create sprite groups
        self.all_sprites = pg.sprite.Group()
        self.hud_group = pg.sprite.Group()
        self.mouse_group = pg.sprite.Group()
        self.towers_group = pg.sprite.Group()
        self.player_group = pg.sprite.Group()
        self.enemy_group = pg.sprite.Group()
        self.grass_group = pg.sprite.Group()
        self.bullet_group = pg.sprite.Group()
        self.coin_group = pg.sprite.Group()
        self.inv_group = pg.sprite.Group()
        self.towers_selected = ["tower1","tower2","tower3","tower4","tower5","tower6",]
        self.tower_held = []

        self.create_hud()
        self.create_grass()
        self.pointer = Pointer(self)
        self.spawn_npc()




        self.run()



    def run(self):
        # Game Loop
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()

    def spawn_npc(self):
        self.wave_length -= 1
        self.spawn_points= [192,320,448,576,704,832,960]
        npc = NPC(self,random.randint(WIDTH+50,WIDTH+150),random.choice(self.spawn_points))


    def events(self):
        # Game Loop - events
        # for event in pg.event.get():
        #     # check for closing window
        #     if event.type == pg.QUIT:
        #         self.running  = False

        for event in pg.event.get():
            # check for closing window
            if event.type == pg.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False
            if event.type == pg.MOUSEBUTTONDOWN and self.pointer.held == False and self.can_click_mouse:
                self.pointer.held = True
                self.can_click_mouse = False
            if event.type == pg.MOUSEBUTTONUP:
                self.can_click_mouse = True



        self.clicked = pg.mouse.get_pressed()

        hits = pg.sprite.spritecollide(self.pointer, self.hud_group, False)
        if self.clicked[0] and hits:
            if hits[0] == self.itemspots[0] and not self.tower_held and self.cash >= 100:
                print ("clicked on spot 1")
                t = Tower(self,self.mouse_pos.x,self.mouse_pos.y,1)
                self.tower_held.append(t)

            if hits[0] == self.itemspots[1] and not self.tower_held and self.cash >= 200:
                print("clicked on spot 2")
                t = Tower(self, self.mouse_pos.x, self.mouse_pos.y, 2)
                self.tower_held.append(t)
            if hits[0] == self.itemspots[2] and not self.tower_held and self.cash >= 300:
                print("clicked on spot 3")
                t = Tower(self, self.mouse_pos.x, self.mouse_pos.y, 3)
                self.tower_held.append(t)
            if hits[0] == self.itemspots[3] and not self.tower_held and self.cash >= 400:
                print("clicked on spot 4")
                t = Tower(self, self.mouse_pos.x, self.mouse_pos.y, 4)
                self.tower_held.append(t)
            if hits[0] == self.itemspots[4]and not self.tower_held and self.cash >= 500:
                print("clicked on spot 5")
                t = Tower(self, self.mouse_pos.x, self.mouse_pos.y, 5)
                self.tower_held.append(t)
            if hits[0] == self.itemspots[5]and not self.tower_held and self.cash >= 600:
                print("clicked on spot 6")
                t = Tower(self, self.mouse_pos.x, self.mouse_pos.y, 6)
                self.tower_held.append(t)
            hits = pg.sprite.groupcollide(self.inv_group,self.enemy_group,True,False)
            if hits:
                print(hits)








    def update(self):
        # Game Loop - update
        self.all_sprites.update()
        # destroy tower with out placing it
        if len(self.tower_held) > 0 and self.clicked[2] == True:
            self.tower_held[0].kill()
            temp_list = self.tower_held[:]
            for i in temp_list:
                self.tower_held.remove(i)
            self.pointer.held=False
        # place tower
        if len(self.tower_held) > 0 and self.pointer.held == True and self.can_click_mouse:
            hits = pg.sprite.spritecollide(self.tower_held[0],self.grass_group,False)
            if self.clicked[0] and hits and hits[0].open and self.cash >= self.tower_held[0].cost:
                self.tower_held[0].place_tower(hits[0].rect.centerx,hits[0].rect.centery)
                self.cash -= self.tower_held[0].cost
                temp_list = self.tower_held[:]
                for i in temp_list:
                    self.tower_held.remove(i)
                self.pointer.held=False
                self.can_click_mouse = True
                hits[0].open = False
        if self.wave_length > 0:
            now = pg.time.get_ticks()
            if now - self.last_spawn > self.spawntime:
                self.last_spawn = now
                self.spawn_npc()






        x = pg.mouse.get_pos()
        self.mouse_pos.x = x[0]
        self.mouse_pos.y = x[1]





    def draw_grid(self):
        for x in range(0,WIDTH,TILESIZE):
            pg.draw.line(self.screen,DGREY,(x,0),(x,HEIGHT))
        for y in range (0,HEIGHT,TILESIZE):
            pg.draw.line(self.screen,DGREY,(0,y),(WIDTH,y))

    def draw_text(self,surf, text, size, x, y, color):
        font = pg.font.Font(font_name, size)
        text_surf = font.render(text, True, color)
        text_rect = text_surf.get_rect()
        text_rect.midtop = (x, y)
        surf.blit(text_surf, text_rect)

    def draw(self):
        # Game Loop - draw
        self.screen.fill(BLACK)
        self.draw_grid()
        bg = pg.Rect(0, 0, WIDTH, TILESIZE)
        pg.draw.rect(self.screen, BROWN, bg)
        self.draw_text(self.screen,"$$$: "+str(self.cash), 40,WIDTH-150,30,WHITE)
        self.all_sprites.draw(self.screen)


        # *after* drawing everything, flip the display
        pg.display.flip()

    def show_start_screen(self):
        pass

    def show_GO_screen(self):
        pass

g = Game()
g.show_start_screen()
while g.running:
    g.new()
    g.show_GO_screen()

pg.quit()
