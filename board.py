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
        self.previous_branch = 0

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

    def check_valid_location(self, location):
        assert type(location) == tuple
        if location[0] > 7 or location[1] > 7 or location[0] < 0 or location[1] < 0:
            return False
        else:
            return True

    def check_clear_or_capture(self, location, mov_piece):
        if self.check_valid_location(location):
            if self.check_tile_empty(location):
                return True
            elif self.pieces[location].player_num != mov_piece.player_num:
                return True
            else:
                return False
        else:
            return False

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

        if isinstance(self.pieces[current_branch.from_location], current_branch.piece.__class__):
            move_piece = self.pieces[current_branch.from_location]
            move_piece.location = current_branch.to_location
            self.pieces[current_branch.to_location] = move_piece
            del(self.pieces[current_branch.from_location])
            self.previous_branch = current_branch

    def create_branch_board(self, pos_branch):
        """Returns a new board with the branch applied to it"""

        assert isinstance(pos_branch, branch.Branch)

        return_board = deepcopy(self)

        cur_piece = return_board.pieces[pos_branch.piece.location]
        new_branch = branch.Branch(cur_piece, pos_branch.to_location)

        return_board.apply_branch(new_branch)

        return return_board

    def get_possible_moves(self, player_num):
        moves = []
        for piece in self.pieces.values():
            if piece.player_num == player_num:
                for move in piece.possible_moves(self):
                    moves.append(move)

        return moves


class FakeBoard(Board):

    def __init__(self, num):
        self.value = num

    def evaluate(self, player_num=0):
        return self.value