#!/bin/python

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


class Pawn(Piece):
    def __init__(self):
        Piece.__init__(self, 1, "pawn")


class Bishop(Piece):
    def __init__(self):
        Piece.__init__(self, 3, "bishop")


class Knight(Piece):
    def __init__(self):
        Piece.__init__(self, 3, "knight")


class Rook(Piece):
    def __init__(self):
        Piece.__init__(self, 5, "rook")


class Queen(Piece):
    def __init__(self):
        Piece.__init__(self, 9, "queen")


class King(Piece):
    def __init__(self):
        Piece.__init__(self, 20, "king")
