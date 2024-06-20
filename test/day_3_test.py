""" Test for Day 3 of Coding Challenges"""
import sys
import unittest
from io import StringIO
from unittest import mock

from src.constants.ascii_art import ISLAND, ALLIGATOR, BOAT, FIRE, CARNIVOROUS_PLANTS, TREASURE
from src.day_3 import treasure_island


class Day3Test(unittest.TestCase):
    """ Test cases for Day 3 of Coding"""

    def setUp(self):
        self.out = StringIO()
        
    def test_left_swim(self):
        """Test the Alligator image"""

        with mock.patch('sys.stdin', new=StringIO('left\nswim')):
            # given
            island = ISLAND.strip()
            alligator = ALLIGATOR.strip()
            sys.stdout = self.out

            # when
            treasure_island()
            actual = self.out.getvalue().strip()

            # then
            self.assertTrue(island in actual)
            self.assertTrue(alligator in actual)

    def test_left_wait(self):
        """Test the Boat image"""

        with mock.patch('sys.stdin', new=StringIO('left\nwait\nblue')):
            # given
            island = ISLAND.strip()
            boat = BOAT.strip()
            sys.stdout = self.out

            # when
            treasure_island()
            actual = self.out.getvalue().strip()

            # then
            self.assertTrue(island in actual)
            self.assertTrue(boat in actual)

    def test_right_red(self):
        """Test the Fire image"""

        with mock.patch('sys.stdin', new=StringIO('right\nred')):
            # given
            island = ISLAND.strip()
            fire = FIRE.strip()
            sys.stdout = self.out

            # when
            treasure_island()
            actual = self.out.getvalue().strip()

            # then
            self.assertTrue(island in actual)
            self.assertTrue(fire in actual)

    def test_right_green(self):
        """Test the Plant image"""

        with mock.patch('sys.stdin', new=StringIO('right\ngreen')):
            # given
            island = ISLAND.strip()
            plants = CARNIVOROUS_PLANTS.strip()
            sys.stdout = self.out

            # when
            treasure_island()
            actual = self.out.getvalue().strip()

            # then
            self.assertTrue(island in actual)
            self.assertTrue(plants in actual)

    def test_right_blue(self):
        """Test the Treasure image"""

        with mock.patch('sys.stdin', new=StringIO('right\nblue')):
            # given
            island = ISLAND.strip()
            treasure = TREASURE.strip()
            sys.stdout = self.out

            # when
            treasure_island()
            actual = self.out.getvalue().strip()

            # then
            self.assertTrue(island in actual)
            self.assertTrue(treasure in actual)


if __name__ == '__main__':
    unittest.main()
