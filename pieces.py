#!/bin/python

class Piece:
	def __init__(self, points = 0, name = "", location = (0,0)):
		self.points = points
		self.name = name
		self.location = location
		
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
		
