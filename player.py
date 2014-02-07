import board
from pieces import *


class Player:
    def __init__(self, player_num, player_board):
        """player_num is either 1 or 0, representing black or white"""

        self.pieces = []

        assert isinstance(player_board, board.Board), "Parameter must be of type 'Board'"
        self.current_board = player_board

        assert player_num == 0 or player_num == 1, "Player number invalid"

        for i in range(0, 10):
            temp = Pawn()
            temp.location = (i, (player_num * 5) + 1)
            self.pieces.append(temp)

        temp = Rook()
        temp.location = (0, player_num * 7)
        self.pieces.append(temp)

        temp = Rook()
        temp.location = (7, player_num * 7)
        self.pieces.append(temp)

        temp = Knight()
        temp.location = (1, player_num * 7)
        self.pieces.append(temp)

        temp = Knight()
        temp.location = (6, player_num * 7)
        self.pieces.append(temp)

        temp = Bishop()
        temp.location = (2, player_num * 7)
        self.pieces.append(temp)

        temp = Bishop()
        temp.location = (5, player_num * 7)
        self.pieces.append(temp)

        temp = King()
        temp.location = (3 + player_num, player_num * 7)
        self.pieces.append(temp)

        """Each player's king. Editing king should be done through 'pieces' array if possible"""
        self.king = temp

        temp = Queen()
        temp.location = (4 - player_num, player_num * 7)
        self.pieces.append(temp)

        for piece in self.pieces:
            player_board.add_piece(piece)