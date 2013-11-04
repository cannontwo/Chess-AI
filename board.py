from pieces import *

class Board:
	def __init__(self):
		self.blocked = {}
	
	def add_piece(self, piece):
		assert isinstance(piece, Piece), "The given object is not a piece"
		self.blocked[piece.location] = piece
		
	def check_tile(self, location):
		assert type(location) == tuple
		if self.blocked.has_key(location):
			return True
		else:
			return False
 
