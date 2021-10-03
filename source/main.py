import pygame as pg
import random
import sys
from os import path
from settings import *
from object import *

class Game:
    def __init__(self):
        # initalize game window, etc...
        pg.init()
        pg.mixer.init()
        self.screen = pg.display.set_mode((WIDTH,HEIGHT))
        pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock()
        # Let the key press down 
        pg.key.set_repeat(500, 100)
        self.load_data()
        self.running = True

    def load_data(self):
        game_folder = path.dirname(__file__)
        img_folder = path.join(game_folder,'image')
        self.wall_img = pg.image.load(path.join(img_folder,WALL_IMAGE)).convert_alpha()
        self.background_img = pg.image.load(path.join(img_folder,BACKGROUND_IMAGE)).convert_alpha()
        self.box_img = pg.image.load(path.join(img_folder,BOX_IMAGE)).convert_alpha()
        self.player_img = pg.image.load(path.join(img_folder,PLAYER_IMAGE)).convert_alpha()
        self.map_data = []
        with open(path.join(game_folder, 'map/map.txt'), 'rt') as f:
            for line in f:
                self.map_data.append(line)

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
                if event.key == pg.K_ESCAPE:
                    self.quit()
                if event.key == pg.K_LEFT:
                    self.player.move (dx=-1)
                if event.key == pg.K_RIGHT:
                    self.player.move (dx=1)
                if event.key == pg.K_UP:
                    self.player.move (dy=-1)
                if event.key == pg.K_DOWN:
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
    g.show_go_screen()

pg.quit()

