from copy import deepcopy
import branch
import pieces


class Board:

    def __init__(self):
        self.pieces = {}
        self.current_turn = 0

    def add_piece(self, piece):
        assert isinstance(piece, pieces.Piece), "The given object is not a piece"
        self.pieces[piece] = piece.location

    def check_tile_empty(self, location):
        assert type(location) == tuple
        if location in self.pieces.values():
            return False
        else:
            return True

    def evaluate(self, player_num):
        point_sum = 0

        for piece in self.pieces:
            if piece.player_num == player_num:
                point_sum += piece.points
            else:
                point_sum -= piece.points

        return point_sum

    def apply_branch(self, current_branch):
        """Applies a branch object to the board"""

        assert isinstance(current_branch, branch.Branch)

        if current_branch.piece in self.pieces:
            current_branch.piece.location = current_branch.move_location
            self.pieces[current_branch.piece] = current_branch.move_location

    def create_branch_board(self, pos_branch):
        """Returns a new board with the branch applied to it"""

        assert isinstance(pos_branch, branch.Branch)

        return_board = deepcopy(self)
        return_board.apply_branch(pos_branch)

        return return_board