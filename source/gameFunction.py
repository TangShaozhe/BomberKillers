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

def new(self):
        # start a new game
        self.playing = True
        self.all_sprites = pg.sprite.Group()
        # set location of player
        self.walls = pg.sprite.Group()
        for row, tiles in enumerate(self.map_data):
            for col, tile in enumerate(tiles):
                if tile == '1':
                    Wall(self, col, row)
                # 其他的用不到的我不用继承了,1麻烦2写不出太突出的东西
                if tile == "2":
                    self.box_list.append(Box(self,self.screen,col,row))
                
                #if tile == 'P':
                    #self.player_play= Player(self,3,21,self.screen)
                
        for i in range(0,10):
            self.robot_list.append(Robot(self,self.screen,self.map_data))
        self.player_play=Player(self,3,21,self.screen)

    def run(self):
        # Game loop

        self.playing = True
        while self.playing:
            self.dt=self.clock.tick(FPS)
            

            self.update()
            
            self.draw()
            
            self.events()

    def update(self):
        # Game loop - update
        self.all_sprites.update()





