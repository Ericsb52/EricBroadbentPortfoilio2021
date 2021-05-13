import pygame as pg
from os import path
from settings import *
import pytmx

class TiledMap:
    def __init__(self,filename):
        tm = pytmx.load_pygame(filename,pixelalpha = True)
        self.width = tm.width*tm.tilewidth
        self.height = tm.height * tm.tileheight
        self.tmxdata = tm

    def render (self,surface):
        ti = self.tmxdata.get_tile_image_by_gid
        for layer in self.tmxdata.visible_layers:
            if isinstance(layer,pytmx.TiledTileLayer):
                for x,y,gid in layer:
                    tile = ti(gid)
                    if tile:
                        surface.blit(tile,(x*self.tmxdata.tilewidth,y*self.tmxdata.tileheight))

    def make_map(self):
        temp_surf = pg.Surface((self.width,self.height))
        self.render(temp_surf)
        return temp_surf


class Map:
    def __init__(self, filename):
        self.data = []
        with open(path.join(map_folder, filename), "rt") as f:
            for line in f:
                self.data.append(line.strip())
        self.tileWidth = len(self.data[0])
        self.tileHeight = len(self.data)
        self.width = self.tileWidth * TILESIZE
        self.height = self.tileHeight * TILESIZE

class Camera:
    def __init__(self,width,height):
        self.camera = pg.Rect(0,0,width,height)
        self.w = width
        self.h = height

    def apply(self,entity):
        return entity.rect.move(self.camera.topleft)

    def apply_rect(self,rect):
        return rect.move(self.camera.topleft)

    def update(self,target):
        x = -target.rect.x +int(WIDTH/2)
        y =  -target.rect.y +int(HEIGHT/2)

        # limmit scrolling
        x = min(0, x)
        y = min(0, y)
        x = max(-(self.w - WIDTH), x)
        y = max(-(self.h - HEIGHT), y)

        self.camera = pg.Rect(x,y,self.w,self.h)
