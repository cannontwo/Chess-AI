from copy import deepcopy
import branch
import pieces


class Board:

    @staticmethod
    def compare_board(cmp_board):
        if isinstance(cmp_board, Board):
            return cmp_board.evaluate()
        else:
            return 0

    def __init__(self):
        self.pieces = {}
        self.current_turn = 0

    def add_piece(self, piece):
        """Adds piece to board at the piece's location if the board does not already have a piece at that location.
            Should only be called at board creation and when a pawn reaches the opposite edge of the board."""
        assert isinstance(piece, pieces.Piece), "The given object is not a piece"

        if self.check_tile_empty(piece.location):
            self.pieces[piece.location] = piece

    def check_tile_empty(self, location):
        assert type(location) == tuple
        if location in self.pieces:
            return False
        else:
            return True

    def evaluate(self, player_num=0):
        """Returns point sum of piece values on the board for a specified player"""
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

    def get_possible_moves(self, player_num):
        moves = []
        for piece in self.pieces:
            for move in piece.possible_moves():
                moves.append(move)

        return moves


class FakeBoard(Board):

    def __init__(self, num):
        super.__init__()
        self.value = num

    def evaluate(self, player_num=0):
        return self.value