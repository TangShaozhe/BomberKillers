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





