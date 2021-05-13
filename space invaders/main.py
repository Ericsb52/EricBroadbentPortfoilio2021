# Pygame template - skeleton for a new pygame project
import pygame as pg
import random as r
from os import *
from settings import *
from sprites import *

class Game(object):

    def __init__(self):
        self.running = True
        # initialize pygame and create window
        pg.init()
        pg.mixer.init()  # for sound
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock()
        self.score = 0



    def add_to_score(self ,points):
        self.score += points

    def load_music(self):
        pg.mixer.music.load(path.join(snd_folder,"Wave After Wave! v0_9.ogg"))
        self.player_shoot = pg.mixer.Sound(path.join(snd_folder,"SFX1.wav"))
        self.npc_shoot = pg.mixer.Sound(path.join(snd_folder, "Airshot3.wav"))
        self.new_level = pg.mixer.Sound(path.join(snd_folder, "Alert1.wav"))
        self.exp_snd = pg.mixer.Sound(path.join(snd_folder, "Explosion 4.wav"))
        self.exp_snd.set_volume(.2)
        self.npc_shoot.set_volume(.2)
        self.player_shoot.set_volume(.2)

    def load_imgs(self):
        self.player_imgs = []
        self.npc_imgs = []
        for i in range (16):
            if i < 10:
                i = "0{}".format(i)
            fn = "player00{}.png".format(i)

            img = pg.image.load(path.join(img_folder,fn)).convert()
            self.player_imgs.append(img)
        for i in range (16):
            if i < 10:
                i = "0{}".format(i)
            fn = "slicer00{}.png".format(i)

            img = pg.image.load(path.join(img_folder,fn)).convert()
            self.npc_imgs.append(img)

        red = pg.image.load(path.join(img_folder,"laserRed16.png")).convert()
        blue = pg.image.load(path.join(img_folder,"laserBlue16.png")).convert()
        self.bul_img ={"red":red,"blue":blue}



    def new(self):
        # create sprite groups
        NPC.count = 0

        self.all_sprites = pg.sprite.Group()
        self.player_group = pg.sprite.Group()
        self.bullet_group = pg.sprite.Group()
        self.npc_group = pg.sprite.Group()
        self.npc_bullet_group = pg.sprite.Group()
        self.bunker_group  = pg.sprite.Group()

        self.shooterlist=[]

        self.load_music()
        self.load_imgs()
        pg.mixer.music.set_volume(.5)
        pg.mixer.music.play(loops=-1)

        # create game objects
        self.player = Player(self)
        self.spawn_wave()
        self.spawn_bunkers()

        # add game objects to groups
        self.all_sprites.add(self.player)

        self.player_group.add(self.player)


        #start running game loop
        self.run()
    def spawn_bunkers(self):
        #left bunker
        x = 100
        y = HEIGHT -50
        for i in range (4):
            for z in range(5):
                self.bunker = Bunker(self,x,y)
                self.bunker_group.add(self.bunker)
                self.all_sprites.add(self.bunker)
                x += 10
            y -= 10
            x = 100

        # mid bunker
        x = WIDTH/2 - 25
        y = HEIGHT - 50
        for i in range(4):
            for z in range(5):
                self.bunker = Bunker(self, x, y)
                self.bunker_group.add(self.bunker)
                self.all_sprites.add(self.bunker)
                x += 10
            y -= 10
            x = WIDTH/2 - 25

        # right bunker
        x = WIDTH - 150
        y = HEIGHT - 50
        for i in range (4):
            for z in range(5):
                self.bunker = Bunker(self,x,y)
                self.bunker_group.add(self.bunker)
                self.all_sprites.add(self.bunker)
                x += 10
            y -= 10
            x = WIDTH - 150

    def spawn_wave(self):
        self.bullet_group = pg.sprite.Group()
        self.npc_group = pg.sprite.Group()
        self.npc_bullet_group = pg.sprite.Group()
        NPC.count = 0
        NPC.moving_right = True
        NPC.moveTimer = 800
        x = -2
        y = 45
        for i in range(5):
            for z in range(10):
                self.npc = NPC(x, y, self)
                self.all_sprites.add(self.npc)
                self.npc_group.add(self.npc)
                self.shooterlist.append(self.npc)
                x += 45
                NPC.count += 1
            y += 45
            x = -2

    def draw_text(self,surf, text, size, x, y, color):
        font = pg.font.Font(font_name, size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x, y)
        surf.blit(text_surface, text_rect)

    def run(self):
        # Game Loop
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()

    def events(self):
        for event in pg.event.get():
            # check for closing window
            if event.type == pg.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False
        # if bullet his npc
        hits = pg.sprite.groupcollide(self.npc_group, self.bullet_group, True, True,pg.sprite.collide_circle)
        for hit in hits:
            self.exp_snd.play()
            NPC.count-=1
            NPC.moveTimer -= 10
            self.shooterlist.remove(hit)
            self.add_to_score(hit.points)

        #  if player bullet hits bunker
        hits = pg.sprite.groupcollide(self.bunker_group, self.bullet_group, True, True,pg.sprite.collide_circle)
        if hits:
            self.exp_snd.play()
        # if enemy bullet hits bunker
        hits = pg.sprite.groupcollide(self.bunker_group, self.npc_bullet_group, True, True,pg.sprite.collide_circle)
        if hits:
            self.exp_snd.play()
        # if npc hits bunker
        hits = pg.sprite.groupcollide(self.bunker_group, self.npc_group, True, False,pg.sprite.collide_circle)
        # if npc bullet hits player
        hits = pg.sprite.spritecollide(self.player, self.npc_bullet_group, True,pg.sprite.collide_circle)
        if hits:
            self.exp_snd.play()
            self.playing = False

        for i in self.shooterlist:
            if i.rect.bottom >=HEIGHT:
                self.playing = False

        if NPC.count <= 0:
            self.new_level.play()
            self.spawn_wave()





    def update(self):

        self.all_sprites.update()

    def draw(self):
        self.screen.fill(BLACK)
        self.draw_text(self.screen, str(self.score), 25, WIDTH / 2, 20, WHITE)
        self.all_sprites.draw(self.screen)
        # *after* drawing everything, flip the display
        pg.display.flip()

    def show_start_screen(self):
        self.draw_text(self.screen, TITLE, 64, WIDTH / 2, HEIGHT / 4, RED)
        self.draw_text(self.screen, "Arrow keys move, Space to fire", 22,
                       WIDTH / 2, HEIGHT / 2, WHITE)
        self.draw_text(self.screen, "Press a key to begin", 18, WIDTH / 2, HEIGHT * 3 / 4, WHITE)
        pg.display.flip()
        waiting = True
        while waiting:
            self.clock.tick(FPS)
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                if event.type == pg.KEYUP:
                    waiting = False

    def show_GO_screen(self):

        pg.mixer.music.fadeout(500)
        self.draw_text(self.screen, "GAME OVER", 100, WIDTH / 2, HEIGHT / 4, BLUE)

        self.draw_text(self.screen, "Press a key to Play Again", 18, WIDTH / 2, HEIGHT * 3 / 4, WHITE)
        pg.display.flip()
        waiting = True
        while waiting:
            self.clock.tick(FPS)
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                if event.type == pg.KEYUP:
                    waiting = False

g = Game()
g.show_start_screen()
while g.running:
    g.new()
    g.show_GO_screen()

pg.quit()
