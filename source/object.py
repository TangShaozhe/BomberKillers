import random
import pygame as pg
import sys
#from os import path
sys.path.append("..")
from source.settings import *


class Player():
    def __init__(self,game, x, y,screen):
        self.screen = screen
        self.game = game
        self.image = game.player_img_one
        self.image1 = game.player_img_two
        #player 's outlook color etc
        #self.image.fill(YELLOW)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.hp = 2
        self.shanshuo_zhen = 0
        self.cishu = 15
        self.time = 8
        self.fanwei = 1#bomb range
        self.shuliang = 1#bomb number
    # move the player function
    def move(self, dx=0, dy=0):
        self.x += dx
        self.y += dy
    def hurt(self):
        self.shanshuo_zhen = 1
    def update(self):
        self.rect.x = self.x * TILESIZE
        self.rect.y = self.y * TILESIZE
        if self.shanshuo_zhen == 1:
            self.time -= 1
            if self.time == 0:
                self.cishu -= 1
                self.time = 8
                if self.cishu == 0:
                    self.shanshuo_zhen=0
                    self.cishu=15
            if self.cishu % 2 == 1:
                self.screen.blit(self.image,(self.rect.x,self.rect.y))
            else:
                self.screen.blit(self.image1,(self.rect.x,self.rect.y))
        else:
            self.screen.blit(self.image, (self.rect.x, self.rect.y))
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

class Box():
    def __init__(self,game, screen, x, y):
        
        self.screen=screen
        self.game = game
        self.image = game.box_img
        self.x = x
        self.y = y
    def update(self):
        self.screen.blit(self.image,(self.x*32,self.y*32))
    def suiji(self):
        return random.randint(1,4)

class Bomb(pg.sprite.Sprite):
    def __init__(self,game,x,y,screen,ditu):
        self.ditu=ditu
        self.screen=screen
        self.game=game
        self.image=game.bomb_img
        self.baozhaxiaoguo=game.fire_img
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
            #bomb range and effect
            
            for i in range(-1*self.fanwei,1+2*self.fanwei):
                if self.ditu[self.y][self.x+i]=="1":
                    if i<0:
                        self.left=i+1
                    elif i>0:
                        self.right=i
                if i!=0 and self.ditu[self.y+i][self.x]!="1":
                    self.screen.blit(self.baozhaxiaoguo,((self.x)*32,(self.y+i)*32))
            for i in range(self.left, self.right):
                self.screen.blit(self.baozhaxiaoguo, ((self.x + i) * 32, self.y * 32))
            
        else:
            self.screen.blit(self.image,(self.x*32,self.y*32))
