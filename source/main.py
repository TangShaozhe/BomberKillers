import pygame as pg
import random
import sys
from os import path
from settings import *
from object import *

class Game:
    def __init__(self):
    
        # initialize game window, etc...
        pg.init()
        pg.mixer.init()
        self.music=pg.mixer.music.load("sound/bgm.mp3")
        pg.mixer.music.play(-1)
        self.screen = pg.display.set_mode((WIDTH,HEIGHT))
        pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock()
        # Let the key press down 
        pg.key.set_repeat(500, 100)
        self.load_data()
        self.running = True
        self.bomb = []
        self.cunfang = ""
        #32x24

    def load_data(self):
        game_folder = path.dirname(__file__)
        img_folder = path.join(game_folder,'image')
        self.wall_img = pg.image.load(path.join(img_folder,WALL_IMAGE)).convert_alpha()
        self.background_img = pg.image.load(path.join(img_folder,BACKGROUND_IMAGE)).convert_alpha()
        self.box_img = pg.image.load(path.join(img_folder,BOX_IMAGE)).convert_alpha()
        self.player_img = pg.image.load(path.join(img_folder,PLAYER_IMAGE)).convert_alpha()
        self.bomb_img = pg.image.load(path.join(img_folder,BOMB_IMAGE)).convert_alpha()
        self.map_data = []
        with open(path.join(game_folder, 'map/map.txt'), 'rt') as f:
            for line in f:
                self.map_data.append(line[:-1])
        print(self.map_data)

    def new(self):
        # start a new game
        self.all_sprites = pg.sprite.Group()
        # set location of player
        self.walls = pg.sprite.Group()
        for row, tiles in enumerate(self.map_data):
            for col, tile in enumerate(tiles):
                if tile == '1':
                    Wall(self, col, row)
                if tile == '2':
                    self.player = Box(self, col, row)
                if tile == 'P':
                    self.player = Player(self, col, row)

    def run(self):
        # Game loop
        
        self.playing = True
        while self.playing:
            self.dt=self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()

    def update(self):
        # Game loop - update
        self.all_sprites.update()

    def events(self):
        # Game loop - events
        for event in pg.event.get():
        # check for closing the window
            if event.type == pg.QUIT:
                self.quit()
            if event.type == pg.KEYDOWN:
                for i in self.map_data:
                    print(i)
                if event.key == pg.K_SPACE: # press space for produce bombs 
                    if self.map_data[self.player.zuobiaoy()][self.player.zuobiaox()-1]!="3" and len(self.bomb)<6:#max 5 bombs
                        self.map_data[self.player.zuobiaoy()]=self.map_data[self.player.zuobiaoy()][:self.player.zuobiaox()]+"3"+self.map_data[self.player.zuobiaoy()][self.player.zuobiaox()+1:]
                        print(self.map_data[self.player.zuobiaoy()])
                        self.bomb.append(Bomb(self.player.zuobiaox(),self.player.zuobiaoy(),self.screen,self.map_data))
                if event.key == pg.K_ESCAPE:
                    self.quit() 
                   # deal with the collide problem, set conditions for moving 
                if event.key == pg.K_LEFT: 
                    if self.map_data[self.player.y][self.player.x-1]!="1"and self.map_data[self.player.y][self.player.x-1]!="2" and self.map_data[self.player.y][self.player.x-1]!="3":
                        self.player.move (dx=-1)
                if event.key == pg.K_RIGHT:
                    if self.map_data[self.player.y][self.player.x+1]!="1" and self.map_data[self.player.y][self.player.x+1]!="2"and self.map_data[self.player.y][self.player.x+1]!="3":
                        self.player.move (dx=1)
                if event.key == pg.K_UP:
                    if self.map_data[self.player.y-1][self.player.x]!="1" and self.map_data[self.player.y-1][self.player.x]!="2"and self.map_data[self.player.y-1][self.player.x]!="3":
                        self.player.move (dy=-1)
                if event.key == pg.K_DOWN:
                    if self.map_data[self.player.y+1][self.player.x]!="1"and self.map_data[self.player.y+1][self.player.x]!="2"and self.map_data[self.player.y+1][self.player.x]!="3":
                        self.player.move (dy=1)

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
        self.draw_grid()
        self.all_sprites.draw(self.screen)

        #setting time for bombing
        for i in self.bomb:
            if i.time<=70:
                self.map_data[i.y]=self.map_data[i.y][:i.x]+"."+self.map_data[i.y][i.x+1:]
            if i.time==0:
                self.bomb.remove(i)
            else:
                print(i.left,i.right)
                i.update()
        # * after drawing everything , flip the display
        pg.display.flip()

    def show_start_screen(self):
        # Game start screen
        pass
    def show_go_screen(self):
        # Game over screen
        pass

g = Game()
g.show_start_screen()
while g.running:
    g.new()
    g.run()
    g.sound()
    g.show_go_screen()

pg.quit()

