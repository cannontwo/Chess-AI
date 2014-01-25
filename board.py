from pieces import *
from player import Player


class Board:
    def __init__(self):
        self.pieces = {}

    def add_piece(self, piece):
        assert isinstance(piece, Piece), "The given object is not a piece"
        self.pieces[piece.location] = piece

    def check_tile(self, location):
        assert type(location) == tuple
        if self.pieces.has_key(location):
            return True
        else:
            return False

    def evaluate(self, player):
        assert isinstance(player, Player), "Non-Player object passed in error"
        point_sum = 0

        for piece in self.pieces:
            if piece.owner == player:
                point_sum += piece.points
            else:
                point_sum -= piece.points

        return point_sum