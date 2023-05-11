import unittest
from pieces import Piece
from constants import BLACK, ROWS, RED, COLS, BROWN, CELL_SIZE
from board import Board

class TestBoard(unittest.TestCase):

    def test_create_board(self):
        board = Board(8)
        self.assertEqual(len(board.board), 8)
        self.assertEqual(len(board.board[0]), 8)

    def test_move(self):
        board = Board(8)
        piece = board.get_piece(2, 1)
        board.move(piece, 3, 0)
        self.assertIsInstance(board.get_piece(3, 0), Piece)

    def test_get_piece(self):
        board = Board(8)
        piece = board.get_piece(2, 1)
        self.assertIsInstance(piece, Piece)

    def test_get_valid_moves(self):
        board = Board(8)
        piece = board.get_piece(2, 1)
        moves = board.get_valid_moves(piece)
        self.assertIn((3, 0), moves.keys())

if __name__ == '__main__':
    unittest.main()
