from __builtin__ import str


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


class Bishop(Piece):
    def __init__(self, location=(0, 0), player_num = 0):
        super(Bishop, self).__init__(3, "bishop", location, player_num)

    def possible_moves(self, board):
        """Possible moves for a bishop"""


class Knight(Piece):
    def __init__(self, location=(0, 0), player_num = 0):
        super(Knight, self).__init__(3, "knight", location, player_num)

    def possible_moves(self, board):
        """Possible moves for a knight"""


class Rook(Piece):
    def __init__(self, location=(0, 0), player_num = 0):
        super(Rook, self).__init__(5, "rook", location, player_num)

    def possible_moves(self, board):
        """Possible moves for a rook"""


class Queen(Piece):
    def __init__(self, location=(0, 0), player_num = 0):
        super(Queen, self).__init__(9, "queen", location, player_num)

    def possible_moves(self, board):
        """Possible moves for a queen"""


class King(Piece):
    def __init__(self, location=(0, 0), player_num = 0):
        super(King, self).__init__(20, "king", location, player_num)

    def possible_moves(self, board):
        """Possible moves for a King"""