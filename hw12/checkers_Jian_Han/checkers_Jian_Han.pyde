CELL_SIZE = 100
BOARD_SIZE = 8
BURLY_WOOD = (205, 155, 155)


def setup():
    global gc
    from board import Board
    from game_controller import GameController
    size(CELL_SIZE * BOARD_SIZE,
         CELL_SIZE * BOARD_SIZE)

    board = Board(BOARD_SIZE)
    gc = GameController()
    
    answer = input('enter your name')
    
    gc.save_score(answer)
    
def draw():
    background(*BURLY_WOOD)
    gc.update(mouseX, mouseY)

def mousePressed():
    gc.press(mouseX, mouseY)

def mouseDragged():
    gc.drag(mouseX, mouseY)

def mouseReleased():
    gc.release()

def input(self, message=''):
    from javax.swing import JOptionPane
    return JOptionPane.showInputDialog(frame, message)
