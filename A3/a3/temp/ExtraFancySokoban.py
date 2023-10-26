from a3_support import *
from model import *
from main import *


class ExtraFancySokoban:

    root = None
    path = ''

    def __init__(self, master: tk.Tk, maze_file: str) -> None:
        self.root = master
        self.path = maze_file

    def redraw(self):
        game = Game(self.path)
        game.set_root(self.root)
        game.game_init()

    def handle_keypress(self, event: tk.Event) -> None:
        # 選擇yes
        self.redraw()
