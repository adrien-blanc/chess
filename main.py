

from board import Board
from piece import Piece

def main():
    
    print('Init board')
    main_board = Board(BOARD)
    print('en {} il y a : {} {}'.format(main_board.board[1], main_board.cases[1].name, main_board.cases[1].color))
    print('en {} il y a : {} {}'.format(main_board.board[35], main_board.cases[35].name, main_board.cases[35].color))
    print('en {} il y a : {} {}'.format(main_board.board[60], main_board.cases[60].name, main_board.cases[60].color))

if __name__ == "__main__":
    main() 