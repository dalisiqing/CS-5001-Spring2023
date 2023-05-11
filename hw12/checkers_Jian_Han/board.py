from pieces import Piece
from constants import BLACK, ROWS, RED, COLS, BROWN, CELL_SIZE

class Board():

    def __init__(self, BOARD_SIZE):
        self.board = []
        self.size = BOARD_SIZE
        self.selected_piece = None
        self.red_left = self.black_left = 12
        self.red_kings = self.black_kings = 0
        self.create_board()

    def create_board(self):
        for row in range(self.size):
            self.board.append([])
            for col in range(self.size):
                if col % 2 == ((row + 1) % 2):
                    if row < 3:
                        self.board[row].append(Piece(row, col, CELL_SIZE, RED))
                    elif row > 4:
                        self.board[row].append(Piece(row, col, CELL_SIZE, BLACK))
                    else:
                        self.board[row].append(0)
                else:
                    self.board[row].append(0)

    def draw_cells(self):
        for row in range(self.size):
            for col in range(self.size):
                if col % 2 == ((row + 1) % 2):
                    noStroke()
                    fill(*BROWN)
                    square(row * CELL_SIZE, col * CELL_SIZE, CELL_SIZE)

    def display(self, mouse_x, mouse_y):
        self.draw_cells()
        for row in range(self.size):
            for col in range(self.size):
                piece = self.board[row][col]
                if piece != 0:
                    piece.display(mouse_x, mouse_y)

    def get_all_pieces(self, color):
        pieces = []
        for row in self.board:
            for piece in row:
                if piece != 0 and piece.color == color:
                    pieces.append(piece)
        return pieces

    def move(self, piece, row, col):
        self.board[piece.row][piece.col], self.board[row][col] = self.board[row][col], self.board[piece.row][piece.col]
        piece.move(row, col)

        if row == ROWS - 1 or row == 0:
            piece.be_king()
            if piece.color == BLACK:
                self.black_kings += 1
            else:
                self.red_kings += 1

    def get_piece(self, row, col):
        return self.board[row][col]

    def get_valid_moves(self, piece):
        moves = {}
        left = piece.col - 1
        right = piece.col + 1
        row = piece.row

        if piece.color == BLACK or piece.king:
            moves.update(self._traverse_left(row -1, max(row-3, -1), -1, piece.color, left))
            moves.update(self._traverse_right(row -1, max(row-3, -1), -1, piece.color, right))
        if piece.color == RED or piece.king:
            moves.update(self._traverse_left(row +1, min(row+3, ROWS), 1, piece.color, left))
            moves.update(self._traverse_right(row +1, min(row+3, ROWS), 1, piece.color, right))
    
        return moves

    def _traverse_left(self, start, stop, step, color, left, skipped=[]):
        moves = {}
        last = []
        for r in range(start, stop, step):
            if left < 0:
                break
            
            current = self.board[r][left]
            if current == 0:
            # we found an empty square
                if skipped and not last:
                # if we've skipped over something we found a blank square and we don't have anything that we can skip again, we can't move there
                    break
                elif skipped:
                    # if we skipped and we did find another thing that we can skip over, then add another skipped to the last skip
                    moves[(r, left)] = last + skipped
                else:
                # if we didn't skip anything so we're on the first one as soon as we find an empty square this is valid moves equals empty last.
                    moves[(r, left)] = last
                
                if last:
                # we had something that can be skipped over now
                    if step == -1:
                        row = max(r-3, 0)
                    else:
                        row = min(r+3, ROWS)
                    moves.update(self._traverse_left(r+step, row, step, color, left-1,skipped=last))
                    moves.update(self._traverse_right(r+step, row, step, color, left+1,skipped=last))
                break
            elif current.color == color:
                break
            else:
            # if current != 0 and it was the other color, I could potentially skip over this current piece assuming that it's an empty square next
                last = [current]
            
            # left is where to start for column
            left -= 1
        
        return moves

    def _traverse_right(self, start, stop, step, color, right, skipped=[]):
        moves = {}
        last = []
        for r in range(start, stop, step):
            if right >= COLS:
                break
            
            current = self.board[r][right]
            if current == 0:
                if skipped and not last:
                    break
                elif skipped:
                    moves[(r,right)] = last + skipped
                else:
                    moves[(r, right)] = last
                
                if last:
                    if step == -1:
                        row = max(r-3, 0)
                    else:
                        row = min(r+3, ROWS)
                    moves.update(self._traverse_left(r+step, row, step, color, right-1,skipped=last))
                    moves.update(self._traverse_right(r+step, row, step, color, right+1,skipped=last))
                break
            elif current.color == color:
                break
            else:
                last = [current]

            right += 1
        
        return moves

    def remove(self, pieces):
        for piece in pieces:
            self.board[piece.row][piece.col] = 0
            if piece != 0:
                if piece.color == RED:
                    self.red_left -= 1
                else:
                    self.black_left -= 1

    def winner(self, turn):
        if self.red_left <= 0:
            return BLACK
        elif self.black_left <= 0:
            return RED

        # red_pieces = self.get_all_pieces(RED)
        # black_pieces = self.get_all_pieces(BLACK)

        # if turn == RED:
        #     for piece in red_pieces:
        #         if self.get_valid_moves(piece):
        #             return None
        #     return BLACK

        # else:
        #     for piece in black_pieces:
        #         if self.get_valid_moves(piece):
        #             return None
        #     return RED
