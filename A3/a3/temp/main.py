import tkinter as tk
from a3_support import *
from model import *
from FancyGameView import *
from FancyStatsView import *
from Shop import *
from Banner import *

class Game():

    width = None
    height = None
    root = None
    banner_frame = None
    maze_frame = None
    shop_frame = None
    stat_frame = None
    sokoban_model = None

    def __init__(self, maze_file_path: str):
        self.sokoban_model = SokobanModel(maze_file_path)

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

    def get_potion(self, type: str) -> Potion:
        if type == STRENGTH_POTION:
            return StrengthPotion()
        elif type == MOVE_POTION:
            return MovePotion()
        elif type == FANCY_POTION:
            return FancyPotion()

    def play_game(self):
        player = self.sokoban_model.player
        game_view = FancyGameView(self.maze_frame, self.sokoban_model.get_dimensions(), (MAZE_SIZE, MAZE_SIZE))
        game_view.display(self.sokoban_model.get_maze(), self.sokoban_model.get_entities(), self.sokoban_model.get_player_position())
        stat_view = FancyStatsView(self.stat_frame)
        stat_view.draw_stats(player.get_moves_remaining(), player.get_strength(), player.get_money())
        stat_view.display()
        banner_view = Banner(self.banner_frame, (1,1), (MAZE_SIZE + SHOP_WIDTH, BANNER_HEIGHT))
        banner_view.display((0,0))
        shop_view = Shop(self.shop_frame)
        for item in self.sokoban_model.get_shop_items():
            potion_effect = self.get_potion(item).effect()
            player_function = player.apply_effect(potion_effect)
            shop_view.create_buyable_item(item, self.sokoban_model.get_shop_items()[item], player_function)
        shop_view.display()
        self.root.mainloop()

Game('../maze_files/coin_maze.txt').play_game()