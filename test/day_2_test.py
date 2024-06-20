""" Test for Day 2 of Coding Challenges"""
import sys
import unittest
from io import StringIO
from unittest import mock

from src.day_2 import calculate_tip


class Day2Test(unittest.TestCase):
    """ Test for Day 2 of Coding"""

    def setUp(self):
        self.out = StringIO()

    def test_tip_calculator(self):
        """ Test for Tip Calculator"""
        total_bill = 1000
        people = 10
        tip_percent = 20
        expected = '120'
        with mock.patch('sys.stdin', StringIO(f'{total_bill}\n{people}\n{tip_percent}')):
            # given
            sys.stdout = self.out

            # when
            calculate_tip()
            actual = self.out.getvalue().strip()

            # then
            self.assertTrue(expected in actual)


if __name__ == '__main__':
    unittest.main()
