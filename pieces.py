from __builtin__ import str
import branch


class Piece(object):
    def __init__(self, points=0, name="", location=(0, 0), player_num = 0):
        self.points = points
        self.name = name
        self.location = location
        self.player_num = player_num

    def __repr__(self):
        """Returns string representation of the given piece"""
        return_string = " "
        return_string += "P:" + str(self.points) + " "
        return_string += self.name + " "
        return_string += "(" + str(self.location[0]) + "," + str(self.location[1]) + ")"
        return return_string

    def possible_moves(self, board):
        """Returns possible moves for a specific piece and board state"""
        raise NotImplementedError("Implement an error to return possible moves")



#TODO Massive implementation of possible move generation for different pieces


class Pawn(Piece):
    def __init__(self, location=(0, 0), player_num = 0):
        super(Pawn, self).__init__(1, "pawn", location, player_num)

    def possible_moves(self, board):
        """Possible moves for a pawn"""
        pos_moves = []
        current_x = self.location[0]
        current_y = self.location[1]

        if self.player_num is 0:
            if board.check_tile_empty((current_x, current_y + 1)) and board.check_valid_location((current_x, current_y + 1)):
                pos_moves.append(board.create_branch_board(branch.Branch(self, (current_x, current_y + 1))))
            elif board.check_valid_location((current_x + 1, current_y + 1)) and not board.check_tile_empty((current_x + 1, current_y + 1)):
                if board.pieces[(current_x + 1, current_y + 1)].player_num != self.player_num:
                    pos_moves.append(board.create_branch_board(branch.Branch(self, (current_x + 1, current_y + 1))))
            elif board.check_valid_location((current_x - 1, current_y + 1)) and not board.check_tile_empty((current_x - 1, current_y + 1)):
                if board.pieces[(current_x - 1, current_y + 1)].player_num != self.player_num:
                    pos_moves.append(board.create_branch_board(branch.Branch(self, (current_x - 1, current_y + 1))))

        return pos_moves



class Bishop(Piece):
    def __init__(self, location=(0, 0), player_num = 0):
        super(Bishop, self).__init__(3, "bishop", location, player_num)

    def possible_moves(self, board):
        """Possible moves for a bishop"""
        pos_moves = []

        return pos_moves


class Knight(Piece):
    def __init__(self, location=(0, 0), player_num = 0):
        super(Knight, self).__init__(3, "knight", location, player_num)

    def possible_moves(self, board):
        """Possible moves for a knight"""
        pos_moves = []

        return pos_moves


class Rook(Piece):
    def __init__(self, location=(0, 0), player_num = 0):
        super(Rook, self).__init__(5, "rook", location, player_num)

    def possible_moves(self, board):
        """Possible moves for a rook"""
        pos_moves = []

        return pos_moves


class Queen(Piece):
    def __init__(self, location=(0, 0), player_num = 0):
        super(Queen, self).__init__(9, "queen", location, player_num)

    def possible_moves(self, board):
        """Possible moves for a queen"""
        pos_moves = []

        return pos_moves


class King(Piece):
    def __init__(self, location=(0, 0), player_num = 0):
        super(King, self).__init__(20, "king", location, player_num)

    def possible_moves(self, board):
        """Possible moves for a King"""
        pos_moves = []

        return pos_moves