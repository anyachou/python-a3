from SokobanModel import *
from a2.a2_support import SokobanView


class Sokoban:
	model = None
	sokobanView = SokobanView()

	def __init__(self, maze_file: str) -> None:
		self.model = SokobanModel(maze_file)

	def display(self) -> None:
		self.sokobanView.display_game(
			self.model.get_maze(),
			self.model.get_entities(),
			self.model.get_player_position()
		)
		self.sokobanView.display_stats(
			self.model.get_player_moves_remaining(),
			self.model.get_player_strength()
		)

	def play_game(self) -> None:

		while not (self.model.has_won() or self.model.get_player_moves_remaining() == 0):
			self.display()
			user_move = input('Enter move: ')
			if user_move == 'q':
				return

			if self.model.attempt_move(user_move):
				print('\n')
			else:
				print('Invalid move\n')

		if self.model.has_won():
			print('You won!')
		else:
			print('You lost!')
