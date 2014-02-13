import board
import player


class Agent:
    def __init__(self, player1, player2, start_board):
        """Create main AI agent"""

        assert isinstance(player1, player.Player)
        assert isinstance(player2, player.Player)
        assert isinstance(start_board, board.Board)

        self.me_player = player1
        self.enemy_player = player2

    def take_turn(self, eval_board, depth, a, b, player_num):
        """Main loop of the AI"""
        assert isinstance(eval_board, board.Board)

        if depth == 0 or len(eval_board.get_possible_moves(player_num)) == 0:
            return eval_board

        #The number passed to evaluate() should never change, so that scores are consistent for similar board states
        if player_num == 0:
            for move in eval_board.get_possible_moves(player_num).sort(key=board.Board.compare_board, reverse=True):
                a = max(a, self.take_turn(move, depth - 1, a, b, 1), key=board.Board.compare_board)
                if b.evaluate() <= a.evaluate():
                    break
            return a
        else:
            for move in eval_board.get_possible_moves(player_num).sort(key=board.Board.compare_board, reverse=True):
                b = min(b, self.take_turn(move, depth - 1, a, b, 0), key=board.Board.compare_board)
                if b.evaluate() <= a.evaluate():
                    break
            return b

    def run(self, current_board):

        best_board = self.take_turn(current_board,
                                    4,
                                    board.FakeBoard(-9999999),
                                    board.FakeBoard(9999999),
                                    self.me_player.player_num)

        return self.generate_real_move(current_board, best_board)

    def generate_real_move(self, first_board, new_board):
        assert isinstance(first_board, board.Board)
        assert isinstance(new_board, board.Board)

        #TODO: Add something chess framework-specific to return a real move to the framework