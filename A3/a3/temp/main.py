import tkinter as tk
from a3_support import *

class Game():

    width = None
    height = None

    def __init__(self):
        self.width = str(MAZE_SIZE + SHOP_WIDTH)
        self.height = str(MAZE_SIZE + BANNER_HEIGHT + STATS_HEIGHT)

    def console(self):
        root = tk.Tk()
        root.geometry(f'{self.width}x{self.height}')
        return root

    def play_game(self):
        pass