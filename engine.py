from tabnanny import check
from board import Board
from piece import Piece

class Engine(object):
    def __init__(self, board):
        self.init(board)
    
    def init(self, board):
        self.board = board
        self.cases = board.cases
        self.end = False

    def start(self):
        print("La partie commence, au tour des {} de jouer.".format(self.board.side2move))
        while self.end == False:
            coup = input("Quel coup voulez-vous jouer ? > ")
            if self.checkCoup(coup):
                self.executeCoup(coup)

    def checkCoup(self, coup):
        if len(coup) == 4 :
            fisrtPiece = coup[:2]
            secondPlace = coup[2:]
        
        

        return True
    
    def executeCoup(self, coup):
        if len(coup) == 4 :
            fisrtPiece = coup[:2]
            secondPlace = coup[2:]

        self.board.cases[self.board.board.index(secondPlace)] = Piece(self.board.cases[self.board.board.index(fisrtPiece)].name, self.board.cases[self.board.board.index(fisrtPiece)].color)
        self.board.cases[self.board.board.index(fisrtPiece)].name = "."

        self.board.changePlayer()
        self.board.displaySimplifiedBoard()