import math
from constants import BLACK, ROWS, RED, COLS, BROWN, CELL_SIZE

class Piece():
    def __init__(self, row, col, PIECE_SIZE, color):
        self.row, self.pre_row = row, row
        self.col, self.pre_col = col, col
        self.color = color
        self.king = False
        self.x = 0
        self.y = 0
        self.calc_pos()

        BIG_FACTOR = 0.85
        SMALL_FACTOR = 0.65
        self.big_size = PIECE_SIZE*BIG_FACTOR
        self.small_size = PIECE_SIZE*SMALL_FACTOR
        
        self.drag = False
        self.press = False
        
        self.STROKE_WEIGHT1 = 2
        self.STROKE_WEIGHT2 = 2
    
    def be_king(self):
        self.king = True
        if self.color == BLACK:
            print("Player achieves king rank")
        else:
            print("Computer achieves king rank")

    def calc_pos(self):
        self.x = self.col*CELL_SIZE + CELL_SIZE//2
        self.y = self.row*CELL_SIZE + CELL_SIZE//2

    def display(self, mouse_x, mouse_y):
        """
        Display pieces
        """
        STROKE_COLOR = 255

        self.STROKE_WEIGHT1 = 2

        if self.close(mouse_x, mouse_y):
            self.STROKE_WEIGHT1 = 5

        stroke(STROKE_COLOR)

        fill(*self.color)
        strokeWeight(self.STROKE_WEIGHT1)
        ellipse(self.x, self.y, self.big_size, self.big_size)
        strokeWeight(self.STROKE_WEIGHT2)
        ellipse(self.x, self.y, self.small_size, self.small_size)

        if self.king:
            img = loadImage("crown.png")
            image(img, self.x - self.small_size//2//math.sqrt(2), self.y - self.small_size//2//math.sqrt(2), self.small_size//math.sqrt(2), self.small_size//math.sqrt(2))

    def close(self, x, y):
        BLACK = (0, 0, 0)
        if (
            (dist(x, y, self.x, self.y) <= self.big_size//2)
                and (self.color == BLACK)):
            return True

    def move(self, row, col):
        self.row, self.pre_row = row, row
        self.col, self.pre_col = col, col
        self.calc_pos()
