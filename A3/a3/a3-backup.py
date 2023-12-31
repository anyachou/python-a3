import tkinter as tk
from tkinter import messagebox, filedialog
from typing import Callable
from model import SokobanModel, Tile, Entity, COIN
from a2_support import *
from a3_support import *

class FancyGameView(AbstractGrid):
	"""show the game map"""
	def __init__(self, master: tk.Tk | tk.Tk, dimensions: tuple[int, int],
	             size: tuple[int, int], **kwargs) -> None:
		super().__init__(master, dimensions, size)
		self._cache = {}  # save images
	def initial_redraw(self, board_state: list[list[Union[str, None]]]) -> None:
		""" Draw the initial state using text annotations. """
		self.clear()
		for i, row in enumerate(board_state):
			for j, marker in enumerate(row):
				text = marker if marker is not None else''
				bbox = self.get_bbox((i, j))
				self.create_rectangle(*bbox)
				self.annotate_position((i, j), text)

	def get_image_name(self, marker):
		"""check the elements in the map"""
		if marker.get_type() == COIN:
			return 'images/$.png'
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

	def display(self, maze: Grid, entities: Entities, player_position:
	Position):
		"""use images to represent game elements"""
		self.clear()
		for i, row in enumerate(
				maze):  # Assuming maze is similar to board_state in structure
			for j, marker in enumerate(row):
				bbox = self.get_bbox((i, j))
				self.create_rectangle(*bbox)
				# display floor, wall, goal
				if marker is not None:
					position = (i, j)
					size = self.get_cell_size()
					image_name = self.get_image_name(marker)
					image = get_image(image_name, size, self._cache)
					midpoint = self.get_midpoint(position)
					self.create_image(midpoint, image=image)
					# display entities, including potions
					if position in entities.keys():
						entity_symbol = entities[(i, j)]
						entity_name = self.get_image_name(entity_symbol)
						entity = get_image(entity_name, size, self._cache)
						self.create_image(self.get_midpoint(position), image=entity)
					# display the player position
					if player_position == position:
						player = get_image('images/P.png', size, self._cache)
						self.create_image(self.get_midpoint(position), image=player)
class FancyStatsView(AbstractGrid):
	"""Display the game of stats"""
	def __init__(self, master: tk.Tk | tk.Frame) -> None:
		"""Initializes the FancyStatsView."""
		super().__init__(master, (3, 3),
		                 (MAZE_SIZE + SHOP_WIDTH, STATS_HEIGHT))
		self._cache = {}
		self._title_font = ('Arial', 14, 'bold')

		# Add 'Player Stats' in the first row
		self.annotate_position((0, 1), "Player Stats",
		                                      font=self._title_font)

		# Adding titles for stats in the second row
		self.annotate_position((1, 0), "Moves remaining:")
		self.annotate_position((1, 1), "Strength:")
		self.annotate_position((1, 2), "Money:")

		# Initialize values for stats in the third row (these will be updated later)
		self._moves_label = self.annotate_position((2, 0), "")
		self._strength_label = self.annotate_position((2, 1), "")
		self._money_label = self.annotate_position((2, 2), "")

	def draw_stats(self, moves_remaining: int, strength: int, money: int) -> None:
		# Updating stats values
		self.itemconfig(self._moves_label, text=str(moves_remaining))
		self.itemconfig(self._strength_label, text=str(strength))
		self.itemconfig(self._money_label, text=str(money))

class Shop(tk.Frame):
	def __init__(self, master: tk.Frame)-> None:
		pass
	def create_buyable_item(self, item:str, amount:int, callback: Callable[[],
	None])->None:
		pass

class FancySokobanView:
	def __init__(self, master:tk.Tk,dismensions:tuple[int,int],size:tuple[int,
	int]) -> None:
		pass
	def display_game(self, maze: Grid, entities: Entities, player_position:
	Position) -> None:
		pass

	def display_stats(self, moves:int, strength: int, money: int)-> None:
		pass
	def create_shop_items(self, shop_items: dict[str,int],
	                      button_callback:Callable[[str],None])->None:
		pass

class ExtraFancySokoban:
	def __init__(self, master:tk.Tk, maze_file: str)-> None:
		pass
	def redraw(self):
		pass
	def handle_keypress(self,event:tk.Event) -> None:
		pass

def play_game(root: tk.Tk, maze_file: str) -> None:
	fancygameview = FancyGameView(root, (7,8),
	                              (MAZE_SIZE, MAZE_SIZE))
	sokobanModel = SokobanModel(maze_file)
	fancygameview.display(sokobanModel.get_maze(),sokobanModel.get_entities(),
	                      sokobanModel.get_player_position())
	fancygameview.pack()
	fancystatsview = FancyStatsView(root)
	fancystatsview.draw_stats(5, 10, 100)
	fancystatsview.pack()
	root.mainloop()

def main() -> None:
	root = tk.Tk()
	root.geometry("450x450")
	play_game(root,
	          "maze_files/coin_maze.txt")


if __name__ == "__main__":
	main()
