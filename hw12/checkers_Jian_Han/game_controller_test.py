import unittest
from game_controller import GameController

class TestGameController(unittest.TestCase):
    def test_reset(self):
        gc = GameController()
        gc.selected = 'test'
        gc.reset()
        self.assertIsNone(gc.selected)
        self.assertIsNotNone(gc.board)
        self.assertDictEqual(gc.valid_moves, {})
        self.assertFalse(gc.is_moving)
        self.assertIsNone(gc.current_piece)

    def test_winner(self):
        gc = GameController()
        self.assertIsNone(gc.winner())

    def test_close(self):
        gc = GameController()
        self.assertFalse(gc.close(50, 50, 1, 1))

if __name__ == '__main__':
    unittest.main()
