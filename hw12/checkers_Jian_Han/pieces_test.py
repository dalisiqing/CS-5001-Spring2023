import unittest
from pieces import Piece

class TestPiece(unittest.TestCase):
    def test_init(self):
        p = Piece(0, 0, 50, (255, 0, 0))
        self.assertEqual(p.row, 0)
        self.assertEqual(p.col, 0)
        self.assertEqual(p.color, (255, 0, 0))
        self.assertFalse(p.king)
        self.assertEqual(p.x, 50)
        self.assertEqual(p.y, 50)
        self.assertEqual(p.big_size, 42.5)
        self.assertEqual(p.small_size, 32.5)
        self.assertFalse(p.drag)
        self.assertFalse(p.press)
        self.assertEqual(p.STROKE_WEIGHT1, 2)
        self.assertEqual(p.STROKE_WEIGHT2, 2)

    def test_be_king(self):
        p = Piece(0, 0, 50, (255, 0, 0))
        p.be_king()
        self.assertTrue(p.king)

    def test_calc_pos(self):
        p = Piece(0, 0, 50, (255, 0, 0))
        p.calc_pos()
        self.assertEqual(p.x, 50)
        self.assertEqual(p.y, 50)

    def test_move(self):
        p = Piece(0, 0, 50, (255, 0, 0))
        p.move(1, 1)
        self.assertEqual(p.row, 1)
        self.assertEqual(p.col, 1)
        self.assertEqual(p.x, 150)
        self.assertEqual(p.y, 150)

if __name__ == '__main__':
    unittest.main()
