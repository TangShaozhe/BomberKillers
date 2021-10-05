import pygame as pg
from settings import *


class Player(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pg.Surface((TILESIZE, TILESIZE))
        #player 's outlook color etc
        #self.image.fill(YELLOW)
        self.image = game.player_img
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
    # move the player function

    def move(self, dx=0, dy=0):
        self.x += dx
        self.y += dy

    def update(self):
        self.rect.x = self.x * TILESIZE
        self.rect.y = self.y * TILESIZE

    #define the coordinators
    def zuobiaox(self):
        return self.x
    def zuobiaoy(self):
        return self.y

class Wall(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.walls
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pg.Surface((TILESIZE, TILESIZE))
        # self.image.fill(GREEN)
        self.image = game.wall_img
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE

class Box(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.walls
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pg.Surface((TILESIZE, TILESIZE))
        # self.image.fill(GREEN)
        self.image = game.box_img
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE

class Bomb(pg.sprite.Sprite):
    def __init__(self,x,y,screen,ditu):
        self.ditu=ditu
        self.screen=screen
        self.image=pg.image.load("image/bomb.png")
        self.baozhaxiaoguo=pg.image.load("image/fire.png")
        self.time=200#爆炸time
        self.x=x
        self.y=y
        self.fanwei=2
        self.left=-self.fanwei
        self.right=self.fanwei
        self.top=-self.fanwei
        self.down=self.fanwei
        #32x32
    def update(self):
        self.time-=1
        if self.time<=70:
            self.screen.blit(self.baozhaxiaoguo,(self.x*32,self.y*32))
            
        else:
            self.screen.blit(self.image,(self.x*32,self.y*32))
