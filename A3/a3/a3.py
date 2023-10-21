import tkinter as tk
from tkinter import messagebox, filedialog
from typing import Callable
from model import SokobanModel, Tile, Entity
from a2_support import *
from a3_support import *

class FancyGameView(AbstractGrid):
	""" Display the game map, including tiles and entities.  """

	def __init__(self, master: tk.Tk, dimensions: tuple[int, int],
	             size: tuple[int, int], **kwargs) -> None:
		super().__init__(master, dimensions, size)
		self._cache = {}

	def display(self, maze: Grid, entities: Entities, player, position:
	Position ):


		"""Create a window with title"""
	# count width and height of the window
	# window_width = MAZE_SIZE + SHOP_WIDTH
	# window_height = MAZE_SIZE + BANNER_HEIGHT + STATS_HEIGHT
	# root = tk.Tk()
	# root.geometry(
	# 	f"{window_width}x{window_height}")  # set width & height of window
	# root.title("Extra Fancy Sokoban")
	# root.mainloop()

def play_game(root: tk.Tk, maze_file: str) -> None:
	test_frame = tk.Frame(root, width="200", height="200", background="red")
	test_frame.pack(side=tk.TOP)



def main() -> None:
	root = tk.Tk()
	play_game(root, "/Users/anya.c/Desktop/CEES7030/A3/a3/maze_files/maze1.txt")
	root.mainloop()
if __name__ == "__main__":
	main()
