import pygame as pg
import unittest
import os
import sys
sys.path.append("..")
from source.object import Player, Robot


# Test all of game objects etc. Player bomb and so on
class Test_Objects(unittest.TestCase):

    def test_Player_move(self):
        
        # test player move with positive move
        self.x = 1
        self.y = 2
        Player.move(self,1,1)
        self.assertEqual(self.x, 2)
        self.assertEqual(self.y, 3)

        self.x = 12
        self.y = 5
        Player.move(self,8,5)
        self.assertEqual(self.x, 20)
        self.assertEqual(self.y, 10)

        # test player move with negative move
        self.x = 20
        self.y = 10
        Player.move(self,-5,-10)
        self.assertEqual(self.x, 15)
        self.assertEqual(self.y, 0)       

    print('Test player movement')

    def test_Bot_hp(self):
        
        # test player loc in px sample: x=5 y=10 in px is 160px and 320px
        self.shanshuo_zhen = 1
        self.hp = 20
        Robot.hurt(self)
        self.assertEqual(self.hp,19)

        
        self.hp = 39
        Robot.hurt(self)
        self.assertEqual(self.hp,38)

       
        self.hp = 27
        Robot.hurt(self)
        self.assertEqual(self.hp,26)

        
    print('Test bot hp update')

if __name__ == '__main__':
    unittest.main()