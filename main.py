from board import Board
from engine import Engine

def main():
    
    print('Init Board')
    board = Board()
    board.displaySimplifiedBoard()

    print('Start Engine')
    engine = Engine(board)
    engine.start()


if __name__ == "__main__":
    main() 