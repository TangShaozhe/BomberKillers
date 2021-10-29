import pygame as pg
import unittest
import sys
import random

sys.path.append("..")
from source.object import Player, Robot, Bomb, Daoju, Wall, Box
from source.gameFunction import Game


# Here is white box test , we know input and output
# Test all of game objects etc. Player bomb and so on
class Test_Player(unittest.TestCase):
    def setUp(self) -> None:
        self.player = Player(self.game, self.init_pos_x, self.init_pos_y, pg.display.set_mode((1024, 768)))

    @classmethod
    def setUpClass(cls) -> None:
        cls.game = Game()
        cls.game.new()
        cls.init_pos_x = 0
        cls.init_pos_y = 0
        print('Ready to test Player class.')

    @classmethod
    def tearDownClass(cls) -> None:
        print('End of Player class test.')

    def test_init_position(self):
        print('Test player init position.')
        pos_x = self.player.zuobiaox()
        pos_y = self.player.zuobiaoy()
        self.assertEqual((pos_x, pos_y), (self.init_pos_x, self.init_pos_y))

    def test_move(self):
        print('Test player movement.')
        # test player move with positive move
        self.player.move(2, 3)
        right_x = 2 + self.init_pos_x
        right_y = 3 + self.init_pos_y
        self.assertEqual(self.player.zuobiaox(), right_x)
        self.assertEqual(self.player.zuobiaoy(), right_y)

        # test player move with negative move
        self.player.move(-5, -3)
        right_x -= 5
        right_y -= 3
        self.assertEqual(self.player.zuobiaox(), right_x)
        self.assertEqual(self.player.zuobiaoy(), right_y)

    def test_hurt(self):
        print('Test player hurt.')
        self.player.hurt()
        self.assertEqual(self.player.shanshuo_zhen, 1)


class Test_Wall(unittest.TestCase):
    def setUp(self) -> None:
        # Generate a random walls
        self.wall_pos = tuple(random.sample(range(5, 15), 2))
        self.wall = Wall(self.game, self.wall_pos[0], self.wall_pos[1])

    @classmethod
    def tearDownClass(cls):
        print('End of Wall class test.')

    @classmethod
    def setUpClass(cls):
        cls.game = Game()
        cls.game.new()
        cls.TITLESIZE = 32
        print('Ready to test Wall class.')

    def test_position(self):
        print("Test wall's position.")
        right_wall_pos = (self.wall.x, self.wall.y)
        self.assertEqual(right_wall_pos, self.wall_pos)

    def test_rect(self):
        print("Test wall's rect position.")
        right_rect_pos = (self.wall_pos[0] * self.TITLESIZE, self.wall_pos[1] * self.TITLESIZE)
        self.assertEqual(right_rect_pos, (self.wall.rect.x, self.wall.rect.y))

    def test_image(self):
        print("Test wall's image type.")
        self.assertIsInstance(self.wall.image, pg.Surface)


class Test_Box(unittest.TestCase):
    def setUp(self) -> None:
        self.x, self.y = tuple(random.sample(range(5, 15), 2))
        self.box = Box(self.game, self.game.screen, self.x, self.y)

    @classmethod
    def tearDownClass(cls):
        print('End of Box class test.')

    @classmethod
    def setUpClass(cls):
        cls.game = Game()
        cls.game.new()
        print('Ready to test Box class.')

    def test_box_position(self):
        print('Test box position.')
        right_pos = (self.x, self.y)
        self.assertEqual((self.box.x, self.box.y), right_pos)

    def test_box_image(self):
        print('Test box image.')
        self.assertEqual(self.box.image, self.game.box_img)

    def test_box_update(self):
        print('Test box update.')
        old_screen = self.box.screen
        # Test whether the object has changed
        self.box.update()
        self.assertEqual(self.box.screen, old_screen)


class Test_Bomb(unittest.TestCase):
    def setUp(self) -> None:
        self.x, self.y = tuple(random.sample(range(5, 15), 2))
        self.bomb = Bomb(
            self.game,
            self.x,
            self.y,
            self.game.screen,
            self.game.map_data,
            self.game.player_play.fanwei,
            "123"
        )

    @classmethod
    def tearDownClass(cls):
        print('End of Bomb class test.')

    @classmethod
    def setUpClass(cls):
        cls.game = Game()
        cls.game.new()
        print('Ready to test Bomb class.')

    def test_update(self):
        print('Test Bomb update')
        old_screen = self.bomb.screen
        self.bomb.update()
        self.assertEqual(self.bomb.screen, old_screen)

    def test_image(self):
        print('Test bomb image.')
        self.assertEqual(self.bomb.image, self.game.bomb_img)

    def test_position(self):
        print('Test bomb position.')
        self.assertEqual((self.bomb.x, self.bomb.y), (self.x, self.y))

    def test_bomb_fanwei(self):
        print('Test bomb fanwei.')
        self.assertEqual(self.bomb.fanwei, self.game.player_play.fanwei)

    def test_direction(self):
        print('Test bomb direction.')
        self.assertEqual(self.bomb.left, -self.game.player_play.fanwei)
        self.assertEqual(self.bomb.right, self.game.player_play.fanwei + 1)
        self.assertEqual(self.bomb.top, -self.game.player_play.fanwei)
        self.assertEqual(self.bomb.down, self.game.player_play.fanwei + 1)


class Test_Robot(unittest.TestCase):
    def setUp(self) -> None:
        self.robot = Robot(self.game, self.game.screen, self.game.map_data)

    @classmethod
    def tearDownClass(cls):
        print('End of Robot class test.')

    @classmethod
    def setUpClass(cls):
        cls.game = Game()
        cls.game.new()
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

    def test_image(self):
        print('Test robot image.')
        self.assertEqual(self.robot.image, self.game.monster_img_one)
        self.assertEqual(self.robot.image1, self.game.monster_img_two)

    def test_time(self):
        print('Test robot time.')
        self.assertEqual(self.robot.time, 100)
        self.assertEqual(self.robot.time1, 8)


class Test_Daoju(unittest.TestCase):
    def setUp(self) -> None:
        self.x, self.y = tuple(random.sample(range(5, 15), 2))
        self.daoju1 = Daoju(self.game, self.game.screen, self.x, self.y, 1)
        self.daoju2 = Daoju(self.game, self.game.screen, self.x, self.y, 2)

    @classmethod
    def tearDownClass(cls):
        print('End of Daoju class test.')

    @classmethod
    def setUpClass(cls):
        cls.game = Game()
        cls.game.new()
        print('Ready to test Daoju class.')

    def test_image(self):
        print('Test Daoju image.')
        self.assertEqual(self.daoju1.image, self.game.props_img)
        self.assertEqual(self.daoju1.image1, self.game.yaoshui_img)

        self.assertEqual(self.daoju2.image, self.game.props_img)
        self.assertEqual(self.daoju2.image1, self.game.yaoshui_img)

        self.assertEqual(self.daoju1.id, 1)
        self.assertEqual(self.daoju2.id, 2)

    def test_update(self):
        print('Test Daoju update.')
        old_screen = self.daoju1.screen
        self.daoju1.update()
        self.assertEqual(self.daoju1.screen, old_screen)

        old_screen = self.daoju2.screen
        self.daoju2.update()
        self.assertEqual(self.daoju2.screen, old_screen)


if __name__ == '__main__':
    unittest.main()