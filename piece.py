

VIDE='.'
SimplifiedNamePiece=(VIDE,'r','d','t','c','f','p')
NamePiece=(VIDE,'ROI','DAME','TOUR','CAVALIER','FOU','PION')

class Piece(object):

    valuePiece=(0,0,9,5,3,3,1)

    tab120 = (
        -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
        -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
        -1,  0,  1,  2,  3,  4,  5,  6,  7, -1,
        -1,  8,  9, 10, 11, 12, 13, 14, 15, -1,
        -1, 16, 17, 18, 19, 20, 21, 22, 23, -1,
        -1, 24, 25, 26, 27, 28, 29, 30, 31, -1,
        -1, 32, 33, 34, 35, 36, 37, 38, 39, -1,
        -1, 40, 41, 42, 43, 44, 45, 46, 47, -1,
        -1, 48, 49, 50, 51, 52, 53, 54, 55, -1,
        -1, 56, 57, 58, 59, 60, 61, 62, 63, -1,
        -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
        -1, -1, -1, -1, -1, -1, -1, -1, -1, -1
        )

    tab64 = (
        21, 22, 23, 24, 25, 26, 27, 28,
        31, 32, 33, 34, 35, 36, 37, 38,
        41, 42, 43, 44, 45, 46, 47, 48,
        51, 52, 53, 54, 55, 56, 57, 58,
        61, 62, 63, 64, 65, 66, 67, 68,
        71, 72, 73, 74, 75, 76, 77, 78,
        81, 82, 83, 84, 85, 86, 87, 88,
        91, 92, 93, 94, 95, 96, 97, 98
        )

    deplacements_tour=(-10,10,-1,1)
    deplacements_fou=(-11,-9,11,9)
    deplacements_cavalier=(-12,-21,-19,-8,12,21,19,8)

    def __init__(self, name=VIDE, color=''):
        self.name = name
        self.value = self.valuePiece[NamePiece.index(name)]
        self.color = color
    
    def getSimplifiedPiece(board, case):
        name = SimplifiedNamePiece[NamePiece.index(board.cases[case].name)]
        color = board.cases[case].color
        if color == "blanc":
            name = name.upper()
        return name


    def isEmpty(self):        
        return (self.nom==self.VIDE)

