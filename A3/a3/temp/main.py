import tkinter as tk
from a3_support import *

class Game():

    width = None
    height = None
    root = None
    banner_frame = None
    maze_frame = None
    shop_frame = None
    stat_frame = None

    def __init__(self):
        self.width = str(MAZE_SIZE + SHOP_WIDTH)
        self.height = str(MAZE_SIZE + BANNER_HEIGHT + STATS_HEIGHT)

        self.root = tk.Tk()
        self.root.title('GAME')
        self.root.geometry(f'{self.width}x{self.height}')
        self.banner_frame = tk.Frame(self.root, background='red', width=self.width, height=BANNER_HEIGHT)
        self.banner_frame.place(x=0, y=0)
        self.maze_frame = tk.Frame(self.root, background='yellow', width=MAZE_SIZE, height=MAZE_SIZE)
        self.maze_frame.place(x=0, y=BANNER_HEIGHT)
        self.shop_frame = tk.Frame(self.root, background='green', width=SHOP_WIDTH, height=MAZE_SIZE)
        self.shop_frame.place(x=MAZE_SIZE, y=BANNER_HEIGHT)
        self.stat_frame = tk.Frame(self.root, background='blue', width=self.width, height=STATS_HEIGHT)
        self.stat_frame.place(x=0, y=MAZE_SIZE + BANNER_HEIGHT)

    def play_game(self):
        self.root.mainloop()

Game().play_game()