import pieces
import board


class Branch:
    def __init__(self, piece, to_location):
        assert isinstance(piece, pieces.Piece), "Passed parameter of non-Piece type"

        self.piece = piece
        self.from_location = piece.location
        self.to_location = to_location