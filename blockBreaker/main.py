# Pygame template - skeleton for a new pygame project
import pygame as pg
import random
from os import path
from settings import *
from block import *
from Ball import *



class Game(object):

    def __init__(self):
        self.running = True
        # initialize pygame and create window
        pygame.init()
        pygame.mixer.init()  # for sound
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption(TITLE)
        self.clock = pg.time.Clock()
        self.block_imgs = []
        self.loadData()

    def create_blocks(self):
        for x in range (6):
            for i in range(8):
                Block(self,(i*60+30),25*x+12.5)

    def loadData(self):
        self.block_List=["blue.png","green.png","purple.png","red.png","yellow.png"]

        for i in range(len(self.block_List)):
            img = pg.image.load(path.join(img_folder,self.block_List[i])).convert()
            img = pg.transform.scale(img,(60,25))
            self.block_imgs.append(img)

        self.ball_img = pg.image.load(path.join(img_folder,"ball.png"))
        self.ball_img = pg.transform.scale(self.ball_img,(25,25))
        self.paddle_img = pg.image.load(path.join(img_folder,"paddle.png"))
        self.paddle_img = pg.transform.scale(self.paddle_img,(150,25))


    def new(self):
        """start a new game"""

        # create sprite groups
        self.all_sprites = pg.sprite.Group()
        self.ball_group = pg.sprite.Group()
        self.block_group = pg.sprite.Group()

        self.create_blocks()
        self.player = Paddle(self,WIDTH/2,HEIGHT-25)
        self.ball = Ball(self)




        # add game objects to groups
        # self.all_sprites.add(self.player)
        self.run()



    def run(self):
        # Game Loop
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()



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

    def update(self):
        # Game Loop - update
        self.all_sprites.update()

    def draw(self):
        # Game Loop - draw
        self.screen.fill(GREY)
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
