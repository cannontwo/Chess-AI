from copy import deepcopy
import branch
import pieces


class Board:

    def __init__(self):
        self.pieces = {}
        self.current_turn = 0

    def add_piece(self, piece):
        assert isinstance(piece, pieces.Piece), "The given object is not a piece"
        self.pieces[piece.location] = piece

    def check_tile_empty(self, location):
        assert type(location) == tuple
        if location in self.pieces:
            return False
        else:
            return True

    def evaluate(self, player_num):
        point_sum = 0

        for piece in self.pieces.values():
            if piece.player_num == player_num:
                point_sum += piece.points
            else:
                point_sum -= piece.points

        return point_sum

    def apply_branch(self, current_branch):
        """Applies a branch object to the board"""

        assert isinstance(current_branch, branch.Branch)

        if current_branch.piece in self.pieces.values():
            current_location = current_branch.piece.location
            current_branch.piece.location = current_branch.move_location
            self.pieces[current_branch.move_location] = current_branch.piece
            del(self.pieces[current_location])

    def create_branch_board(self, pos_branch):
        """Returns a new board with the branch applied to it"""

        assert isinstance(pos_branch, branch.Branch)

        return_board = deepcopy(self)

        cur_piece = return_board.pieces[pos_branch.piece.location]
        new_branch = branch.Branch(cur_piece, pos_branch.move_location)

        return_board.apply_branch(new_branch)

        return return_board