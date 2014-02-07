import pieces
import board


class Branch:
    def __init__(self, piece, move_location):
        assert isinstance(piece, pieces.Piece), "Passed parameter of non-Piece type"

        self.piece = piece
        self.move_location = move_location