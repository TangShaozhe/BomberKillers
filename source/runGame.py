import pygame as pg
import random
import sys
from os import path
sys.path.append("..")
from source.gameFunction import *


g = Game()
g.show_start_screen()
while g.running:

    g.new()
    g.run()
    #g.sound()
    g.show_go_screen()


pg.quit()