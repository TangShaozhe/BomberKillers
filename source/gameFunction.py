import pygame as pg
#import random
import sys
#import time
from os import path
sys.path.append("..")
from source.settings import *
from source.object import *

class Game:
    def __init__(self):
        # initalize game window, etc...
        pg.init()
        pg.mixer.init()
        game_folder = path.dirname(__file__)
        music_folder = path.join(game_folder,'sound')
        self.music=pg.mixer.music.load(path.join(music_folder,MUSIC_FIRST))
        pg.mixer.music.play(-1)
        self.screen = pg.display.set_mode((WIDTH,HEIGHT))
        pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock()
        # Let the key press down 
        pg.key.set_repeat(500, 100)

        
        self.load_data()
        self.running = True

        self.cunfang=""
        self.bomb_shuliang=0
        #self.player_play=Player(self,3,21,self.screen)
        self.x=0
        #32x24
def load_data(self):
        game_folder = path.dirname(__file__)
        img_folder = path.join(game_folder,'image')
        self.wall_img = pg.image.load(path.join(img_folder,WALL_IMAGE)).convert_alpha()
        self.background_img = pg.image.load(path.join(img_folder,BACKGROUND_IMAGE)).convert_alpha()
        self.box_img = pg.image.load(path.join(img_folder,BOX_IMAGE)).convert_alpha()
        self.player_img_one = pg.image.load(path.join(img_folder,PLAYER_IMAGE_ONE)).convert_alpha()
        self.player_img_two = pg.image.load(path.join(img_folder,PLAYER_IMAGE_TWO)).convert_alpha()
        self.bomb_img = pg.image.load(path.join(img_folder,BOMB_IMG)).convert_alpha()
        self.monster_bomb_img = pg.image.load(path.join(img_folder,MONSTER_BOMB_IMG)).convert_alpha()
        self.fire_img =pg.image.load(path.join(img_folder,FIRE_IMG)).convert_alpha()
        self.props_img =pg.image.load(path.join(img_folder,PROPS_IMG)).convert_alpha()
        self.yaoshui_img =pg.image.load(path.join(img_folder,YAOSHUI_IMG)).convert_alpha()
        self.monster_img_one =pg.image.load(path.join(img_folder,MONSTER_IMG_ONE)).convert_alpha()
        self.monster_img_two =pg.image.load(path.join(img_folder,MONSTER_IMG_TWO)).convert_alpha()
        self.map_data = []
        self.bomb=[]#玩家炸弹
        self.daoju_list=[]# 道具
        self.robot_list=[]# 机器人
        self.robot_bomb=[]# 机器人炸弹
        self.box_list=[]# 箱子
        with open(path.join(game_folder, 'map/map.txt'), 'rt') as f:
            for line in f:
                self.map_data.append(line[:-1])
        print(self.map_data)




