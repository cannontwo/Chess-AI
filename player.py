from board import Board
from pieces import *


class Player:
    def __init__(self, player_num, board):
        """player_num is either 1 or 0, representing black or white"""
        self.pieces = []

        self.init_board(board)

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

        temp = Queen()
        temp.location = (4 - player_num, player_num * 7)
        self.pieces.append(temp)

        for piece in self.pieces:
            board.add_piece(piece)

    def init_board(self, board):
        """Initializes local board variable"""
        assert isinstance(board, Board), "Parameter must be of type 'Board'"
        self.board = board

    def get_board_string(self):
        return_string = ""

        for piece in self.pieces:
            return_string = return_string + "," + piece.string_rep()

        return_string = return_string[1:]
        return return_string