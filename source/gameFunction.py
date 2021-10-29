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
        
        """
        if pygame.mixer.music.get_busy() == False: #检查是否正在播放音乐
            pygame.mixer.music.play() #开始播放音乐流
        """
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

    def events(self):
        # Game loop - events
        for event in pg.event.get():
        # check for closing the window
            if event.type == pg.QUIT:
                self.running = False
                self.playing = False
                pg.quit()
                #sys.exit()
            if event.type == pg.KEYDOWN:
                if event.key==pg.K_SPACE:
                    if self.map_data[self.player_play.zuobiaoy()][self.player_play.zuobiaox()]!="3" and self.map_data[self.player_play.zuobiaoy()][self.player_play.zuobiaox()]!="4" and self.bomb_shuliang<self.player_play.shuliang:#最大五个炸弹
                        self.bomb_shuliang+=1
                        print(self.player_play.shuliang)
                        self.x+=1
                        print(self.map_data[self.player_play.zuobiaoy()][:self.player_play.zuobiaox()]+"3"+self.map_data[self.player_play.zuobiaoy()][self.player_play.zuobiaox()+1:])
                        self.map_data[self.player_play.zuobiaoy()]=self.map_data[self.player_play.zuobiaoy()][:self.player_play.zuobiaox()]+"3"+self.map_data[self.player_play.zuobiaoy()][self.player_play.zuobiaox()+1:]
                        self.bomb.append(Bomb(self,self.player_play.zuobiaox(),self.player_play.zuobiaoy(),self.screen,self.map_data,self.player_play.fanwei,"123"))
                if event.key == pg.K_ESCAPE:
                    self.running = False
                    self.playing = False
                    pg.quit()
                    #sys.exit()
                if event.key == pg.K_LEFT:
                    if self.map_data[self.player_play.y][self.player_play.x-1]!="1"and self.map_data[self.player_play.y][self.player_play.x-1]!="2" and self.map_data[self.player_play.y][self.player_play.x-1]!="3":
                        self.player_play.move (dx=-1)
                elif event.key == pg.K_RIGHT:
                    if self.map_data[self.player_play.y][self.player_play.x+1]!="1" and self.map_data[self.player_play.y][self.player_play.x+1]!="2"and self.map_data[self.player_play.y][self.player_play.x+1]!="3":
                        self.player_play.move (dx=1)
                elif event.key == pg.K_UP:
                    if self.map_data[self.player_play.y-1][self.player_play.x]!="1" and self.map_data[self.player_play.y-1][self.player_play.x]!="2"and self.map_data[self.player_play.y-1][self.player_play.x]!="3":
                        self.player_play.move (dy=-1)
                elif event.key == pg.K_DOWN:
                    if self.map_data[self.player_play.y+1][self.player_play.x]!="1"and self.map_data[self.player_play.y+1][self.player_play.x]!="2"and self.map_data[self.player_play.y+1][self.player_play.x]!="3":
                         self.player_play.move (dy=1)
                if self.map_data[self.player_play.y][self.player_play.x] == "4":
                    self.player_play.hurt()
                if len(self.daoju_list)>0:
                    for j in self.daoju_list:
                        if self.player_play.x == j.x and self.player_play.y == j.y:
                            if j.id == 1:
                                self.player_play.shuliang+=1
                            elif j.id == 2:
                                self.player_play.fanwei += 1
                            self.daoju_list.remove(j)
    def draw_grid(self):
        for x in range(0,WIDTH,TILESIZE):
            pg.draw.line(self.screen, LIGHTGREY,(x,0),(x,HEIGHT))
        for y in range(0,HEIGHT,TILESIZE):
            pg.draw.line(self.screen, LIGHTGREY,(0,y),(WIDTH,y))

    def draw(self):
        # Game loop - draw
        # Draw / render
        #self.screen.fill(DARKGREY)
        self.screen.blit(self.background_img,[0,0])
        if len(self.box_list)>0:#箱子
            for i in self.box_list:
                if self.map_data[i.y][i.x]=="4":
                    a = i.suiji()
                    if self.player_play.x == i.x and self.player_play.y == i.y:
                        if a == 1:
                            self.player_play.fanwei += 1
                        elif a == 2:
                            self.player_play.shuliang += 1
                    else:
                        if a == 1 or a == 2:
                            self.daoju_list.append(Daoju(self,self.screen, i.x, i.y, a))
                    self.box_list.remove(i)
                else:
                    i.update()
        if len(self.bomb) > 0:#玩家炸弹
            for i in self.bomb:
                if i.time == 70:
                    #self.map_data[i.y] = self.map_data[i.y][:i.x] + "." + self.map_data[i.y][i.x + 1:]
                    self.bomb_shuliang-=1
                if i.time == 0:
                    for x, y in i.list():
                        self.map_data[y] = self.map_data[y][:x] + "." + self.map_data[y][x + 1:]
                else:
                    if i.time == 70:# 时间
                        for x,y in i.list():
                            self.map_data[y]= self.map_data[y][:x] + "4" + self.map_data[y][x + 1:]
                        if self.map_data[self.player_play.y][self.player_play.x] == "4":
                            self.player_play.hurt()
                        for j in self.robot_list:
                            if self.map_data[j.y][j.x] == "4" and j.shanshuo_zhen !=1:
                                j.hurt()
                                if j.hp == 0:
                                    a = j.suiji()
                                    if self.player_play.x == j.x and self.player_play.y == j.y:
                                        if a == 1:
                                            self.player_play.fanwei += 1
                                        elif a == 2:
                                            self.player_play.shuliang += 1
                                    else:
                                        if a == 1 or a == 2:
                                            self.daoju_list.append(Daoju(self,self.screen,j.x,j.y,a))
                                    self.robot_list.remove(j)
                    i.update()
        if len(self.robot_bomb) > 0:#怪兽的炸弹
            for i in self.robot_bomb:
                if i.time == 70:
                    self.map_data[i.y] = self.map_data[i.y][:i.x] + "." + self.map_data[i.y][i.x + 1:]
                if i.time == 0:
                    for x, y in i.list():
                        self.map_data[y] = self.map_data[y][:x] + "." + self.map_data[y][x + 1:]
                    self.robot_bomb.remove(i)
                else:
                    if i.time == 70:
                        for x, y in i.list():
                            self.map_data[y] = self.map_data[y][:x] + "4" + self.map_data[y][x + 1:]
                        if self.map_data[self.player_play.y][self.player_play.x] == "4"  :
                            self.player_play.hurt()
                    i.update()
        self.player_play.update()
        self.draw_grid()
        self.all_sprites.draw(self.screen)
        # * after drawing everything , flip the display
        if len(self.daoju_list)>0:
            for a in self.daoju_list:
                a.update()
        if len(self.robot_list)>0:
            for i in self.robot_list:
                i.update(self.map_data)
                if i.fangzhi_zhadan():
                    self.robot_bomb.append(Bomb(self,i.x,i.y,self.screen,self.map_data,i.fanwei,"guaishou"))
        pg.display.update()

    def show_start_screen(self):
        # Game start screen
        pass
    def show_go_screen(self):
        # Game over screen
        pass





