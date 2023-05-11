from board import Board
from constants import BLACK, ROWS, RED, COLS, BROWN, CELL_SIZE, BOARD_SIZE
import random

class GameController():
    """
    The Game Controller
    """
    def __init__(self):
        self.reset()
    
    def reset(self):
        self.selected = None
        self.board = Board(BOARD_SIZE)
        self.turn = BLACK
        self.valid_moves = {}

        self.is_moving = False
        self.current_piece = None
        self.winner = None

    def update(self, mouse_x, mouse_y):
        """
        Carry out board update and
        check if game is over
        """
        self.board.display(mouse_x, mouse_y)

    
    def win(self, turn):
        if self.board.winner(turn):
            self.winner = self.board.winner(turn)
            if self.winner == BLACK:
                print("You win!")
            else:
                print("Computer win!")

    def press(self, mouse_x, mouse_y):
        for r in self.board.board:
            for c in r:
                if c != 0 and c.close(mouse_x, mouse_y):
                    self.current_piece = c
                    self.is_moving = True

    def drag(self, mouse_x, mouse_y):
        if self.is_moving:
            self.current_piece.x = mouse_x
            self.current_piece.y = mouse_y

    def release(self):
        if self.is_moving:
            for row in range(BOARD_SIZE):
                for col in range(BOARD_SIZE):
                    if self.close(self.current_piece.x, self.current_piece.y, row, col) and col % 2 == ((row + 1) % 2) and self.move(self.current_piece, row, col):
                        self.is_moving = False
                        self.ai_move()
                        self.win(self.turn)
                        return

        self.current_piece.row = self.current_piece.pre_row
        self.current_piece.col = self.current_piece.pre_col
        self.current_piece.calc_pos()
        self.win(self.turn)
        self.is_moving = False

    def move(self, piece, row, col):
        self.valid_moves = self.board.get_valid_moves(piece)
        if piece != 0 and piece.color == self.turn and (row, col) in self.valid_moves:
            self.board.move(piece, row, col)
            skipped = self.valid_moves[(row, col)]
            if skipped:
                self.board.remove(skipped)
            self.change_turn()
            return True
        return False

    def change_turn(self):
        self.valid_moves = {}
        if self.turn == RED:
            self.turn = BLACK
            print("Your turn!")
        else:
            self.turn = RED
            print("Computer turn!")

    def close(self, x, y, row, col):
        if col*CELL_SIZE <= x <= (col+1)*CELL_SIZE and row*CELL_SIZE <= y <= (row+1)*CELL_SIZE:
            return True
        else:
            return False

    def ai_move(self):
        all_pieces = self.board.get_all_pieces(RED)
        if all_pieces:
            while self.turn == RED:
                random_piece = random.choice(all_pieces)
                if self.board.get_valid_moves(random_piece):
                    for row in range(BOARD_SIZE):
                        for col in range(BOARD_SIZE):
                            if col % 2 == ((row + 1) % 2) and self.move(random_piece, row, col):
                                return
                else:
                    all_pieces.remove(random_piece)

    def save_score(self, name, score=0):
        # read existing scores from file
        try:
            with open("scores.txt", "r") as f:
                scores = f.readlines()
        except FileNotFoundError:
            scores = []

        # parse existing scores into a dictionary
        score_dict = {}
        for line in scores:
            name, score_str = line.strip().split()
            score_dict[name] = int(score_str)

        # update score for current player
        if name in score_dict:
            score_dict[name] += score
        else:
            score_dict[name] = score

        # sort scores by descending order
        score_list = sorted(score_dict.items(), key=lambda x: x[1], reverse=True)

        # write scores back to file
        with open("scores.txt", "w") as f:
            for name, score in score_list:
                f.write(name + ' ' + str(score) + '\n')


