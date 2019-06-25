import unittest
from unittest import TestCase
import chess as cb
from chess import get_chess_board
import argparse


class TestChessBoard(TestCase):

    def test_get_chess_board_3_3(self):
        self.assertEqual(cb.get_chess_board(3, 3), ['* * ', ' ', '* * '])

    def test_get_chess_board_2_2(self):
        self.assertEqual(cb.get_chess_board(2, 2), ['* ', ' '])


if __name__ == '__main__':
    unittest.main()
