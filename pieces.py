#!/bin/python
from __builtin__ import str


class Piece:
    def __init__(self, points=0, name="", location=(0, 0)):
        self.points = points
        self.name = name
        self.location = location

    def string_rep(self):
        return_string = " "
        return_string += "P:" + str(self.points) + " "
        return_string += self.name + " "
        return_string += "(" + str(self.location[0]) + "," + str(self.location[1]) + ")"
        return return_string

    def possible_moves(self, board):
        """Returns possible moves for a specific piece and board state"""
        raise NotImplementedError("Implement an error to return possible moves")


class Pawn(Piece):
    def __init__(self):
        Piece(self, 1, "pawn")

    def possible_moves(self, board):
        """Possible moves for a pawn"""


class Bishop(Piece):
    def __init__(self):
        Piece(self, 3, "bishop")

    def possible_moves(self, board):
        """Possible moves for a bishop"""


class Knight(Piece):
    def __init__(self):
        Piece(self, 3, "knight")

    def possible_moves(self, board):
        """Possible moves for a knight"""


class Rook(Piece):
    def __init__(self):
        Piece(self, 5, "rook")

    def possible_moves(self, board):
        """Possible moves for a rook"""


class Queen(Piece):
    def __init__(self):
        Piece(self, 9, "queen")

    def possible_moves(self, board):
        """Possible moves for a queen"""


class King(Piece):
    def __init__(self):
        Piece(self, 20, "king")

    def possible_moves(self, board):
        """Possible moves for a King"""