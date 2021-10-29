
import pygame as pg
from pygame.locals import *
import unittest
import os
import sys
#from threading import Thread
import threading
import time
sys.path.append("..")
from source.gameFunction import Game



#black box test
class Test_Game(unittest.TestCase):
    def test_game_load_play_quit(self):
        def runGame():

            import source.runGame
            
        def keyInput():
            print("start try to runGame")
            #keyboard = Controller()
            time.sleep(2.5)
            #keyboard.press('a')
            #keyboard.press(Key.esc)
            #keyboard.release(Key.esc)
            putBomb = pg.event.Event(pg.locals.KEYDOWN, unicode="space", key=pg.locals.K_SPACE, mod=pg.locals.KMOD_NONE)
            moveRight = pg.event.Event(pg.locals.KEYDOWN, unicode="right", key=pg.locals.K_RIGHT, mod=pg.locals.KMOD_NONE)
            moveLeft = pg.event.Event(pg.locals.KEYDOWN, unicode="left", key=pg.locals.K_LEFT, mod=pg.locals.KMOD_NONE)
            moveDown = pg.event.Event(pg.locals.KEYDOWN, unicode="down", key=pg.locals.K_DOWN, mod=pg.locals.KMOD_NONE)
            moveUp = pg.event.Event(pg.locals.KEYDOWN, unicode="up", key=pg.locals.K_UP, mod=pg.locals.KMOD_NONE)
            closeGame = pg.event.Event(pg.locals.KEYDOWN, unicode="escape", key=pg.locals.K_ESCAPE, mod=pg.locals.KMOD_NONE) #create the event
            
            pg.event.post(moveUp)
            time.sleep(0.3)
            pg.event.post(moveUp)
            time.sleep(0.3)
            pg.event.post(moveUp)
            time.sleep(0.3)
            pg.event.post(moveDown)
            time.sleep(0.3)
            pg.event.post(moveLeft)
            time.sleep(0.3)
            pg.event.post(moveRight)
            time.sleep(0.3)
            pg.event.post(moveRight)
            time.sleep(0.3)
            pg.event.post(putBomb)
            time.sleep(3)
            pg.event.post(closeGame) #add the event to the queue
            print("game is working")
        mistake = False
        try:
            #os.system('cd .. && cd source && py runGame.py')
            #import source.runGame
            threading.Thread(target=keyInput).start()
            threading.Thread(target=runGame).start()
            
            time.sleep(10)
            
            
            
        except Exception as e :
            mistake = True
            print(e)
            print("Something is wrong about the game, the error is above")
        
        self.assertNotEqual(mistake, True)

    print("test_loadGame&quitGame")

if __name__ == '__main__':
    unittest.main()
