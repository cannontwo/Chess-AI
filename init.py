from board import Board
from player import Player
from agent import Agent

game_board = Board()
self_player = Player(0, game_board)
enemy_player = Player(1, game_board)

game_agent = Agent(self_player, enemy_player, game_board)
game_agent.begin(self_player)
