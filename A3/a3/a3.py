import tkinter as tk
from tkinter import messagebox, filedialog
from typing import Callable
from model import SokobanModel, Tile, Entity
from a2_support import *
from a3_support import *

class FancyGameView(AbstractGrid):
	"""show the game map"""

	def __init__(self, master: tk.Tk, dimensions: tuple[int, int],
	             size: tuple[int, int], **kwargs) -> None:
		super().__init__(master, dimensions, size)
		self._cache = {}  # save images

	def initial_redraw(self, board_state: list[list[Union[str, None]]]) -> \
			None:
		""" Draw the initial state using text annotations. """
		self.clear()
		for i, row in enumerate(board_state):
			for j, marker in enumerate(row):
				text = marker if marker is not None else ''
				bbox = self.get_bbox((i, j))
				self.create_rectangle(*bbox)
				self.annotate_position((i, j), text)

	def get_image_name(self, marker):
		if marker.get_type() == WALL:
			return 'images/W.png'
		elif marker.get_type() == FLOOR:
			return 'images/Floor.png'
		elif marker.get_type() == GOAL:
			return 'images/G.png'
		elif marker.get_type() == CRATE:
			return 'images/C.png'
		elif marker.get_type() == FILLED_GOAL:
			return 'images/X.png'
		elif marker.get_type() == PLAYER:
			return 'images/P.png'
		elif marker.get_type() == FANCY_POTION:
			return 'images/F.png'
		elif marker.get_type() == MOVE_POTION:
			return 'images/M.png'
		elif marker.get_type() == STRENGTH_POTION:
			return 'images/S.png'

	def display(self, maze: Grid, entities: Entities, player_position: Position):
		"""use images to represent game elements"""
		self.clear()

		for i, row in enumerate(maze):
			for j, marker in enumerate(row):
				bbox = self.get_bbox((i, j))
				self.create_rectangle(*bbox)

				# Check if there's an entity at the current position
				entity = entities.get((i, j), None)
				print(entities.get)
				if entity:
					image_name = self.get_image_name(entity)
				elif (i, j) == player_position:
					image_name = self.get_image_name(PLAYER)
				elif marker is not None:
					image_name = self.get_image_name(marker)
				else:
					image_name = None

				# Display the maze (including tile, wall, goal)
				if image_name:
					size = self.get_cell_size()
					image = get_image(image_name, size, self._cache)
					midpoint = self.get_midpoint((i, j))
					self.create_image(midpoint, image=image)

class FancyStatsView(AbstractGrid):
	def __init__(self, master: tk.Tk) -> None:
		pass

	def draw_stats(selfself, moves_remaining: int, strength: int, money: int) \
			-> None:
		pass

class Shop(tk.Frame):
	def __init__(self, master: tk.Frame) -> None:
		pass

	def create_buyable_item(self, item: str, amount: int, callback: Callable[[],
	None]) -> None:
		pass

class FancySokobanView:
	def __init__(self, master: tk.Tk, dismensions: tuple[int, int],
	             size: tuple[int,
	             int]) -> None:
		pass

	def display_game(selfself, maze: Grid, entities: Entities, player_position:
	Position) -> None:
		pass

	def display_stats(selfself, moves: int, strength: int, money: int) -> None:
		pass

	def create_shop_items(self, shop_items: dict[str, int],
	                      button_callback: Callable[[str], None]) -> None:
		pass

class ExtraFancySokoban:
	def __init__(self, master: tk.Tk, maze_file: str) -> None:
		pass

	def redraw(self):
		pass

	def handle_keypress(selfself, event: tk.Event) -> None:
		pass

def play_game(root: tk.Tk, maze_file: str) -> None:
	fancygameview = FancyGameView(root, (7, 8), (MAZE_SIZE, MAZE_SIZE))
	sokobanModel = SokobanModel(maze_file)
	fancygameview.display(sokobanModel.get_maze(), sokobanModel.get_entities(),
	                      sokobanModel.get_player_position())
	fancygameview.pack()
	root.mainloop()

def main() -> None:
	root = tk.Tk()
	root.geometry("450x450")
	play_game(root,
	          "/Users/anya.c/Desktop/CEES7030/A3/a3/maze_files/maze1.txt")

if __name__ == "__main__":
	main()
