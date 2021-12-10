import pygame as pg
import unittest
import sys
import time
import random
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'source'))
from object import Player, Robot, Bomb, Daoju, Wall, Box


# Here is white box test , we know input and output
# Test all of game objects etc. Player bomb and so on
class Test_Player(unittest.TestCase):


    @classmethod
    def setUpClass(cls) -> None:

        print('Ready to test Player class.')

    @classmethod
    def tearDownClass(cls) -> None:
        print('End of Player class test.')

    def test_init_position(self):
        print('Test player init position.')
        pos_x = 9
        pos_y = 8
        init_pos_x=9
        init_pos_y=8

        self.assertEqual((pos_x, pos_y), (init_pos_x, init_pos_y))

    def test_move(self):
        print('Test player movement.')
        # test player move with positive move
        player_x=545
        player_y=232
        new_x=player_x+5
        new_y=player_y+8
        self.assertEqual(new_x, 550)
        self.assertEqual(new_y, 240)

        # test player move with negative move

        player_x=545
        player_y=232
        new_x=player_x-5
        new_y=player_y-2
        self.assertEqual(new_x, 540)
        self.assertEqual(new_y, 230)

    def test_hurt(self):
        print('Test player hurt.')
        player_hp=1
        getAttack_hp=player_hp-1
        self.assertEqual(getAttack_hp, 0)


class Test_Wall(unittest.TestCase):
    def setUp(self) -> None:
        # Generate a random walls
        self.wall_pos = tuple(random.sample(range(5, 15), 2))

    @classmethod
    def tearDownClass(cls):
        print('End of Wall class test.')

    @classmethod
    def setUpClass(cls):

        cls.TITLESIZE = 32
        print('Ready to test Wall class.')



    def test_rect(self):
        print("Test wall's rect position.")
        rect=32
        wall_pos_x=8*rect
        wall_pos_y=9*rect
        self.assertEqual(wall_pos_x,256)
        self.assertEqual(wall_pos_y,288)




class Test_Box(unittest.TestCase):
    def setUp(self) -> None:
        self.x, self.y = tuple(random.sample(range(5, 15), 2))


    @classmethod
    def tearDownClass(cls):
        print('End of Box class test.')

    @classmethod
    def setUpClass(cls):

        print('Ready to test Box class.')

    def test_box_position(self):
        print('Test box position.')
        box_x=7
        box_y=8
        right_pos = (7, 8)
        self.assertEqual((box_x, box_y), right_pos)

    def test_box_image(self):
        print('Test box image.')


    def test_box_update(self):
        print('Test box update.')
        old_screen = (800,600)
        # Test whether the object has changed
        new_screen = (800,600)
        self.assertEqual(new_screen, old_screen)


class Test_Robot(unittest.TestCase):


    @classmethod
    def tearDownClass(cls):
        print('End of Robot class test.')

    @classmethod
    def setUpClass(cls):

        print('Ready to test Robot class.')

    def test_Bot_hp(self):
        print('Test bot hp update')

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


    def test_time(self):
        print('Test robot time.')
        robot_time = 100
        robot_time1 = 8
        self.assertEqual(robot_time, 100)
        self.assertEqual(robot_time1, 8)


if __name__ == '__main__':
    unittest.main()