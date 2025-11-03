import unittest

from hanoi import (
    moves,
)


class HanoiTest(unittest.TestCase):
    def test_two_poles(self):
        self.assertEqual(moves(2, 1), 1)

    def test_three_poles(self):
        self.assertEqual(moves(3, 7), 127)

    def test_four_poles(self):
        self.assertEqual(moves(4, 7), 25)

    def test_five_poles(self):
        self.assertEqual(moves(5, 7), 19)

    def test_six_poles(self):
        self.assertEqual(moves(6, 7), 17)

    def test_zero_discs(self):
        self.assertEqual(moves(9, 0), 0)
