import board


class Agent:
    def __init__(self, player1, player2, start_board):
        """Create main AI agent"""

        self.player_white = player1
        self.player_black = player2
        self.current_board = start_board

        self.possible_boards = []

    def take_turn(self, turn_board):
        """Main loop of the AI"""

        #At some point
        self.possible_boards.sort(key=board.Board.compare_board, reverse=True)


