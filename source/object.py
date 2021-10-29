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

class Bomb():
    def __init__(self,game,x,y,screen,ditu,fanwei,msg):
        self.ditu=ditu
        self.screen=screen
        self.msg=msg
        self.game=game
        self.image=game.bomb_img
        self.guaishou_image=game.monster_bomb_img
        
        self.baozhaxiaoguo=game.fire_img
        self.time=200#爆炸time
        self.x=x
        self.y=y
        self.fanwei=fanwei#泡泡范围
        self.left=-self.fanwei
        self.right=self.fanwei+1
        self.top=-self.fanwei
        self.down=self.fanwei+1
        self.jilu_baozha_list=[]
        #32x32
    def list(self):
        return self.jilu_baozha_list
    def update(self):
        #4边检查箱子就不要-1
        self.time-=1
        if self.time<70:
            for i in range(self.top, self.down):
                if i != 0:
                    self.screen.blit(self.baozhaxiaoguo, ((self.x) * 32, (self.y + i) * 32))
            for i in range(self.left, self.right):
                self.screen.blit(self.baozhaxiaoguo, ((self.x + i) * 32, self.y * 32))
        elif self.time==70:
            self.screen.blit(self.baozhaxiaoguo,(self.x*32,self.y*32))
            for i in range(-1,-1*self.fanwei-1,-1):
                if self.ditu[self.y][self.x+i] == "1":
                    self.left = i+1
                    break
                elif self.ditu[self.y][self.x+i] == "2":
                    self.left= i
                    break
            for i in range(0,1*self.fanwei+1):
                if self.ditu[self.y][self.x+i] == "1" :
                    self.right = i
                    break
                elif self.ditu[self.y][self.x+i] == "2":
                    self.right= i+1
                    break
            for i in range(-1,-1*self.fanwei-1,-1):
                if self.ditu[self.y+i][self.x] == "1":
                    self.top = i+1
                    break
                elif self.ditu[self.y+i][self.x] == "2":
                    self.top= i
                    break
            for i in range(0,1*self.fanwei+1):
                if self.ditu[self.y+i][self.x] == "1" :
                    self.down = i
                    break
                elif self.ditu[self.y+i][self.x] == "2":
                    self.down= i+1
                    break
            for i in range(self.top,self.down):
                    if i!=0:
                        self.jilu_baozha_list.append([self.x,self.y+i])
                        self.screen.blit(self.baozhaxiaoguo,((self.x)*32,(self.y+i)*32))
            for i in range(self.left, self.right):
                self.jilu_baozha_list.append([self.x+i, self.y])
                self.screen.blit(self.baozhaxiaoguo, ((self.x + i) * 32, self.y * 32))
        else:
            if self.msg == "guaishou":
                self.screen.blit(self.guaishou_image,(self.x*32,self.y*32))
            else:
                self.screen.blit(self.image,(self.x*32,self.y*32))

class Robot():
    def __init__(self,game,screen,ditu):#人机自带x,y不需要
        self.screen=screen
        self.ditu=ditu
        self.game = game
        
        
        self.image=game.monster_img_one
        self.image1=game.monster_img_two
        self.hp=2#代表血量
        self.fx=0#表示方向
        self.time=100
        self.shanshuo_zhen = 0
        self.cishu = 15
        self.time1 = 8
        self.fanwei=2
        self.shuliang=1
        while True:
            self.y=random.randint(1,len(self.ditu)-1)
            self.x=random.randint(1,len(self.ditu)-1)
            if self.ditu[self.y][self.x] == ".":
                break
    def move(self,ditu):
        self.time-=1
        if self.time==0:
            self.time=random.randint(50,120)
            self.fx=random.randint(1,4)
        if self.fx>0:
            self.ditu=ditu
            if self.fx==1:
                if self.ditu[self.y][self.x-1]==".":
                    self.x-=1
            elif self.fx==2:
                if self.ditu[self.y-1][self.x] == ".":
                    self.y -= 1
            elif self.fx==3:
                if self.ditu[self.y][self.x+1] == ".":
                    self.x += 1
            elif self.fx==4:
                if self.ditu[self.y+1][self.x] == ".":
                    self.y += 1
            self.fx=0
    def suiji(self):
        return random.randint(1,4)
    def fangzhi_zhadan(self):
        a=random.randint(1,1000)
        if a == 1:
            return True
    def hurt(self):
        self.shanshuo_zhen=1
        self.hp-=1
    def update(self,ditu):
        self.move(ditu)
        if self.shanshuo_zhen == 1:
            self.time1 -= 1
            if self.time1 == 0:
                self.cishu -= 1
                self.time1 = 8
                if self.cishu == 0:
                    self.shanshuo_zhen=0
                    self.cishu=15
            if self.cishu % 2 == 1:
                self.screen.blit(self.image,(self.x*32,self.y*32))
            else:
                self.screen.blit(self.image1,(self.x*32,self.y*32))
        else:
            self.screen.blit(self.image, (self.x*32, self.y*32))
