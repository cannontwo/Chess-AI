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
        return_string += str(self.points) + " "
        return_string += self.name + " "
        return_string += "(" + str(self.location[0]) + "," + str(self.location[1]) + ")"
        return return_string

    def possible_moves(self, board):
        """Returns possible moves for a specific piece and board state"""
        raise NotImplementedError("Implement a method to return possible moves")


class Pawn(Piece):
    def __init__(self, location=(0, 0), player_num = 0):
        super(Pawn, self).__init__(1, "pawn", location, player_num)

    def possible_moves(self, board):
        """Possible moves for a pawn"""
        current_x = self.location[0]
        current_y = self.location[1]

        if self.player_num is 0:
            if board.check_tile_empty((current_x, current_y + 1)) and board.check_valid_location((current_x, current_y + 1)):
                yield board.create_branch_board(branch.Branch(self, (current_x, current_y + 1)))
            elif board.check_valid_location((current_x + 1, current_y + 1)) and not board.check_tile_empty((current_x + 1, current_y + 1)):
                if board.pieces[(current_x + 1, current_y + 1)].player_num != self.player_num:
                    yield board.create_branch_board(branch.Branch(self, (current_x + 1, current_y + 1)))
            elif board.check_valid_location((current_x - 1, current_y + 1)) and not board.check_tile_empty((current_x - 1, current_y + 1)):
                if board.pieces[(current_x - 1, current_y + 1)].player_num != self.player_num:
                    yield board.create_branch_board(branch.Branch(self, (current_x - 1, current_y + 1)))
        else:
            if board.check_tile_empty((current_x, current_y - 1)) and board.check_valid_location((current_x, current_y - 1)):
                yield board.create_branch_board(branch.Branch(self, (current_x, current_y - 1)))
            elif board.check_valid_location((current_x + 1, current_y - 1)) and not board.check_tile_empty((current_x + 1, current_y - 1)):
                if board.pieces[(current_x + 1, current_y - 1)].player_num != self.player_num:
                    yield board.create_branch_board(branch.Branch(self, (current_x + 1, current_y - 1)))
            elif board.check_valid_location((current_x - 1, current_y - 1)) and not board.check_tile_empty((current_x - 1, current_y - 1)):
                if board.pieces[(current_x - 1, current_y - 1)].player_num != self.player_num:
                    yield board.create_branch_board(branch.Branch(self, (current_x - 1, current_y - 1)))


class Bishop(Piece):
    def __init__(self, location=(0, 0), player_num = 0):
        super(Bishop, self).__init__(3, "bishop", location, player_num)

    def possible_moves(self, board):
        """Possible moves for a bishop"""
        x = current_x = self.location[0]
        y = current_y = self.location[1]

        while True:

            if not board.check_valid_location((x + 1, y + 1)):
                break

            x += 1
            y += 1

            if board.check_tile_empty((x, y)):
                yield board.create_branch_board(branch.Branch(self, (x, y)))
            elif board.pieces[(x, y)].player_num is not self.player_num:
                yield board.create_branch_board(branch.Branch(self, (x, y)))
                break
            else:
                break

        x = current_x
        y = current_y

        while True:

            if not board.check_valid_location((x - 1, y + 1)):
                break

            x -= 1
            y += 1

            if board.check_tile_empty((x, y)):
                yield board.create_branch_board(branch.Branch(self, (x, y)))
            elif board.pieces[(x, y)].player_num is not self.player_num:
                yield board.create_branch_board(branch.Branch(self, (x, y)))
                break
            else:
                break

        x = current_x
        y = current_y

        while True:

            if not board.check_valid_location((x - 1, y - 1)):
                break

            x -= 1
            y -= 1

            if board.check_tile_empty((x, y)):
                yield board.create_branch_board(branch.Branch(self, (x, y)))
            elif board.pieces[(x, y)].player_num is not self.player_num:
                yield board.create_branch_board(branch.Branch(self, (x, y)))
                break
            else:
                break

        x = current_x
        y = current_y

        while True:

            if not board.check_valid_location((x + 1, y - 1)):
                break


            x += 1
            y -= 1

            if board.check_tile_empty((x, y)):
                yield board.create_branch_board(branch.Branch(self, (x, y)))
            elif board.pieces[(x, y)].player_num is not self.player_num:
                yield board.create_branch_board(branch.Branch(self, (x, y)))
                break
            else:
                break


class Knight(Piece):
    def __init__(self, location=(0, 0), player_num = 0):
        super(Knight, self).__init__(3, "knight", location, player_num)

    def possible_moves(self, board):
        """Possible moves for a knight"""

        current_x = self.location[0]
        current_y = self.location[1]

        if board.check_clear_or_capture((current_x + 3, current_y + 1), self):
            yield board.create_branch_board(branch.Branch(self, (current_x + 3, current_y + 1)))

        if board.check_clear_or_capture((current_x + 1, current_y + 3), self):
            yield board.create_branch_board(branch.Branch(self, (current_x + 1, current_y + 3)))

        if board.check_clear_or_capture((current_x - 3, current_y + 1), self):
            yield board.create_branch_board(branch.Branch(self, (current_x - 3, current_y + 1)))

        if board.check_clear_or_capture((current_x - 1, current_y + 3), self):
            yield board.create_branch_board(branch.Branch(self, (current_x - 1, current_y + 3)))

        if board.check_clear_or_capture((current_x - 3, current_y - 1), self):
            yield board.create_branch_board(branch.Branch(self, (current_x - 3, current_y - 1)))

        if board.check_clear_or_capture((current_x - 1, current_y - 3), self):
            yield board.create_branch_board(branch.Branch(self, (current_x - 1, current_y - 3)))

        if board.check_clear_or_capture((current_x + 3, current_y - 1), self):
            yield board.create_branch_board(branch.Branch(self, (current_x + 3, current_y - 1)))

        if board.check_clear_or_capture((current_x + 1, current_y - 3), self):
            yield board.create_branch_board(branch.Branch(self, (current_x + 1, current_y - 3)))


class Rook(Piece):
    def __init__(self, location=(0, 0), player_num = 0):
        super(Rook, self).__init__(5, "rook", location, player_num)

    def possible_moves(self, board):
        """Possible moves for a rook"""
        x = current_x = self.location[0]
        y = current_y = self.location[1]

        while True:

            if not board.check_valid_location((x + 1, y)):
                break

            x += 1

            if board.check_tile_empty((x, y)):
                yield board.create_branch_board(branch.Branch(self, (x, y)))
            elif board.pieces[(x, y)].player_num is not self.player_num:
                yield board.create_branch_board(branch.Branch(self, (x, y)))
                break
            else:
                break

        x = current_x
        y = current_y

        while True:

            if not board.check_valid_location((x - 1, y)):
                break

            x -= 1

            if board.check_tile_empty((x, y)):
                yield board.create_branch_board(branch.Branch(self, (x, y)))
            elif board.pieces[(x, y)].player_num is not self.player_num:
                yield board.create_branch_board(branch.Branch(self, (x, y)))
                break
            else:
                break

        x = current_x
        y = current_y

        while True:

            if not board.check_valid_location((x, y - 1)):
                break

            y -= 1

            if board.check_tile_empty((x, y)):
                yield board.create_branch_board(branch.Branch(self, (x, y)))
            elif board.pieces[(x, y)].player_num is not self.player_num:
                yield board.create_branch_board(branch.Branch(self, (x, y)))
                break
            else:
                break

        x = current_x
        y = current_y

        while True:

            if not board.check_valid_location((x, y + 1)):
                break

            y += 1

            if board.check_tile_empty((x, y)):
                yield board.create_branch_board(branch.Branch(self, (x, y)))
            elif board.pieces[(x, y)].player_num is not self.player_num:
                yield board.create_branch_board(branch.Branch(self, (x, y)))
                break
            else:
                break


class Queen(Piece):
    def __init__(self, location=(0, 0), player_num = 0):
        super(Queen, self).__init__(9, "queen", location, player_num)

    def possible_moves(self, board):
        """Possible moves for a queen"""
        x = current_x = self.location[0]
        y = current_y = self.location[1]

        while True:

            if not board.check_valid_location((x + 1, y)):
                break

            x += 1

            if board.check_tile_empty((x, y)):
                yield board.create_branch_board(branch.Branch(self, (x, y)))
            elif board.pieces[(x, y)].player_num is not self.player_num:
                yield board.create_branch_board(branch.Branch(self, (x, y)))
                break
            else:
                break

        x = current_x
        y = current_y

        while True:

            if not board.check_valid_location((x - 1, y)):
                break

            x -= 1

            if board.check_tile_empty((x, y)):
                yield board.create_branch_board(branch.Branch(self, (x, y)))
            elif board.pieces[(x, y)].player_num is not self.player_num:
                yield board.create_branch_board(branch.Branch(self, (x, y)))
                break
            else:
                break

        x = current_x
        y = current_y

        while True:

            if not board.check_valid_location((x, y - 1)):
                break

            y -= 1

            if board.check_tile_empty((x, y)):
                yield board.create_branch_board(branch.Branch(self, (x, y)))
            elif board.pieces[(x, y)].player_num is not self.player_num:
                yield board.create_branch_board(branch.Branch(self, (x, y)))
                break
            else:
                break

        x = current_x
        y = current_y

        while True:

            if not board.check_valid_location((x, y + 1)):
                break

            y += 1

            if board.check_tile_empty((x, y)):
                yield board.create_branch_board(branch.Branch(self, (x, y)))
            elif board.pieces[(x, y)].player_num is not self.player_num:
                yield board.create_branch_board(branch.Branch(self, (x, y)))
                break
            else:
                break

        x = current_x
        y = current_y

        while True:

            if not board.check_valid_location((x + 1, y + 1)):
                break

            x += 1
            y += 1

            if board.check_tile_empty((x, y)):
                yield board.create_branch_board(branch.Branch(self, (x, y)))
            elif board.pieces[(x, y)].player_num is not self.player_num:
                yield board.create_branch_board(branch.Branch(self, (x, y)))
                break
            else:
                break

        x = current_x
        y = current_y

        while True:

            if not board.check_valid_location((x - 1, y + 1)):
                break

            x -= 1
            y += 1

            if board.check_tile_empty((x, y)):
                yield board.create_branch_board(branch.Branch(self, (x, y)))
            elif board.pieces[(x, y)].player_num is not self.player_num:
                yield board.create_branch_board(branch.Branch(self, (x, y)))
                break
            else:
                break

        x = current_x
        y = current_y

        while True:

            if not board.check_valid_location((x - 1, y - 1)):
                break

            x -= 1
            y -= 1

            if board.check_tile_empty((x, y)):
                yield board.create_branch_board(branch.Branch(self, (x, y)))
            elif board.pieces[(x, y)].player_num is not self.player_num:
                yield board.create_branch_board(branch.Branch(self, (x, y)))
                break
            else:
                break

        x = current_x
        y = current_y

        while True:

            if not board.check_valid_location((x + 1, y - 1)):
                break


            x += 1
            y -= 1

            if board.check_tile_empty((x, y)):
                yield board.create_branch_board(branch.Branch(self, (x, y)))
            elif board.pieces[(x, y)].player_num is not self.player_num:
                yield board.create_branch_board(branch.Branch(self, (x, y)))
                break
            else:
                break


class King(Piece):
    def __init__(self, location=(0, 0), player_num = 0):
        super(King, self).__init__(20, "king", location, player_num)

    def possible_moves(self, board):
        """Possible moves for a King"""
        current_x = self.location[0]
        current_y = self.location[1]

        if board.check_clear_or_capture((current_x + 1, current_y + 1), self):
            yield board.create_branch_board(branch.Branch(self, (current_x + 1, current_y + 1)))

        if board.check_clear_or_capture((current_x - 1, current_y - 1), self):
            yield board.create_branch_board(branch.Branch(self, (current_x - 1, current_y - 1)))

        if board.check_clear_or_capture((current_x + 1, current_y - 1), self):
            yield board.create_branch_board(branch.Branch(self, (current_x + 1, current_y - 1)))

        if board.check_clear_or_capture((current_x - 1, current_y + 1), self):
            yield board.create_branch_board(branch.Branch(self, (current_x - 1, current_y + 1)))

        if board.check_clear_or_capture((current_x - 1, current_y), self):
            yield board.create_branch_board(branch.Branch(self, (current_x - 1, current_y)))

        if board.check_clear_or_capture((current_x + 1, current_y), self):
            yield board.create_branch_board(branch.Branch(self, (current_x + 1, current_y)))

        if board.check_clear_or_capture((current_x, current_y - 1), self):
            yield board.create_branch_board(branch.Branch(self, (current_x, current_y - 1)))

        if board.check_clear_or_capture((current_x, current_y + 1), self):
            yield board.create_branch_board(branch.Branch(self, (current_x, current_y + 1)))