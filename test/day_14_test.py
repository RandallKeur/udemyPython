"""Test for Day 14 of Coding Challenges"""
import os
import sys
import unittest
from io import StringIO
from unittest import mock

from src.day_14 import higher_lower
from src.constants.ascii_art import HIGHER_LOWER


class Day14Test(unittest.TestCase):
    """Test for Day 14 of Coding"""

    def test_higher_lower_art(self):
        """Test the Higher or Lower image"""
        # setup
        out = StringIO()
        os.environ['TERM'] = 'xterm-256color'

        with mock.patch('sys.stdin', new=StringIO('A\nA\nA\nA\nA\nA\nA\nA\nA\nA\nA\nA\nA\nA\nA\nA\n'
                                                  'A\nA\nA\nA\nA\nA')):
            # given
            art = HIGHER_LOWER.strip()
            sys.stdout = out

            # when
            higher_lower()
            actual = out.getvalue().strip()

            # then
            self.assertTrue(art in actual)