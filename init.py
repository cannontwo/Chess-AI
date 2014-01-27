from board import Board
from player import Player

board = Board()
self_player = Player(0, board)
enemy_player = Player(1, board)

print "Player 1's pieces: %s"%(self_player.pieces)