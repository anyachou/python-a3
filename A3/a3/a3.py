import tkinter as tk
from tkinter import messagebox, filedialog
from typing import Callable
from model import SokobanModel, Tile, Entity, COIN, Player, StrengthPotion, \
    MovePotion, FancyPotion, Potion
from a2_support import *
from a3_support import *

class FancyGameView(AbstractGrid):

    image_paths = None
    size = None


    def __init__(self, master: tk.Tk | tk.Frame, dimensions: tuple[int, int],
                 size: tuple[int, int], **kwargs) -> None:
        """initialize"""
        super().__init__(master, dimensions, size)
        self._cache = {}
        self.image_paths = {
            COIN: 'images/$.png',
            WALL: 'images/W.png',
            FLOOR: 'images/Floor.png',
            GOAL: 'images/G.png',
            CRATE: 'images/C.png',
            FILLED_GOAL: 'images/X.png',
            PLAYER: 'images/P.png',
            FANCY_POTION: 'images/F.png',
            MOVE_POTION: 'images/M.png',
            STRENGTH_POTION: 'images/S.png',
            'B': 'images/banner.png'
        }
        self.size = self.get_cell_size()

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
        return self.image_paths[marker.get_type()]

    def display(self, maze: Grid, entities: Entities, player_position: Position):
        """use images to represent game elements"""
        for i, row in enumerate(maze):  # Assuming maze is similar to board_state in structure
            for j, marker in enumerate(row):
                bbox = self.get_bbox((i, j))
                self.create_rectangle(*bbox)
                # display floor, wall, goal
                if marker is not None:
                    position = (i, j)
                    self.display_image(marker, position)
                    if player_position == position:
                        # display the player position
                        self.display_image(Player(0,0), position)
                    elif position in entities.keys():
                        # display entities, including potions
                        self.display_image(entities[(i, j)], position)

    def display_image(self, marker, position):
        image_path = self.get_image_name(marker)
        image = get_image(image_path, self.size, self._cache)
        midpoint = self.get_midpoint(position)
        self.create_image(midpoint, image=image)
        self.pack()

class FancyStatsView(AbstractGrid):
    """Display the game of stats"""
    moves_remaining = None
    strength = None
    money = None

    def __init__(self, master: tk.Tk | tk.Frame) -> None:
        """Initializes the FancyStatsView."""
        super().__init__(master, (3, 3),
                         (MAZE_SIZE + SHOP_WIDTH, STATS_HEIGHT))
        self._cache = {}
        self._title_font = ('Arial', 18, 'bold')
        self.annotate_position((0, 1), "Player Stats", font=self._title_font)
        self.annotate_position((1, 0), "Moves remaining:")
        self.annotate_position((1, 1), "Strength:")
        self.annotate_position((1, 2), "Money:")
        self.moves_remaining = tk.IntVar()
        self.moves_remaining.set(0)
        self.strength = tk.IntVar()
        self.strength.set(0)
        self.money = tk.IntVar()
        self.money.set(0)

    def draw_stats(self, moves_remaining:int, strength: int, money: int) -> None:
        self.moves_remaining.set(moves_remaining)
        self.strength.set(strength)
        self.money.set(money)

    def display(self):
        self.delete('move')
        self.delete('strength')
        self.delete('money')
        self.create_text(self.get_midpoint((2, 0)), text=str(self.moves_remaining.get()), tags='move')
        self.create_text(self.get_midpoint((2, 1)), text=str(self.strength.get()), tags='strength')
        self.create_text(self.get_midpoint((2, 2)), text='$'+str(
            self.money.get()), tags='money')
        self.pack()

class Shop(tk.Frame):
    items = {}

    def __init__(self, master: tk.Frame) -> None:
        super().__init__(master)

    # callback = SokobanModel().get_shop_items()
    def create_buyable_item(self, item: str, amount: int,
                            callback: Callable[[], None]) -> None:
        item_name = ''
        if item == MOVE_POTION:
            item_name = 'Move Potion'
        elif item == STRENGTH_POTION:
            item_name = 'Strengh Potion'
        elif item == FANCY_POTION:
            item_name = 'Fancy Potion'
        self.items[item_name] = amount

    def display(self):
        for widget in self.winfo_children():
            widget.destroy()

        label = tk.Label(self, text='Shop', anchor='n',
                         font=('Arial', 20, 'bold'))
        label.grid(row=0, column=0)
        init_row = 1
        for item in self.items:
            text = tk.Label(self, text=item + ': $'
                                 + str(self.items[item]), font=('Arial', 16))
            text.grid(row=init_row, column=0)
            button = tk.Button(self, text='Buy')
            button.grid(row=init_row, column=1)
            init_row += 1
        self.pack()

class Banner(AbstractGrid):

    image_path = ''
    size = ()


    def __init__(self, master: tk.Tk | tk.Frame, dimensions: tuple[int, int],
                 size: tuple[int, int], **kwargs) -> None:
        super().__init__(master, dimensions, size)
        self.image_path = 'images/banner.png'
        self._cache = {}
        self.size = size

    def display(self, position: tuple[int, int]):
        image = get_image(self.image_path, self.size, self._cache)
        midpoint = self.get_midpoint(position)
        self.create_image(midpoint, image=image)
        self.pack()


class Game():

    width = None
    height = None
    root = None
    banner_frame = None
    maze_frame = None
    shop_frame = None
    stat_frame = None
    sokoban_model = None
    game_view = None
    stat_view = None
    banner_view = None
    shop_view = None
    player = None

    def __init__(self, maze_file_path: str):
        self.sokoban_model = SokobanModel(maze_file_path)

        self.width = str(MAZE_SIZE + SHOP_WIDTH)
        self.height = str(MAZE_SIZE + BANNER_HEIGHT + STATS_HEIGHT)

        self.root = tk.Tk()
        self.root.title('Extra Fancy Sokoban')
        self.root.geometry(f'{self.width}x{self.height}')
        self.banner_frame = tk.Frame(self.root,
                                     width=self.width, height=BANNER_HEIGHT)
        self.banner_frame.place(x=0, y=0)
        self.maze_frame = tk.Frame(self.root,
                                   width=MAZE_SIZE, height=MAZE_SIZE)
        self.maze_frame.place(x=0, y=BANNER_HEIGHT)
        self.shop_frame = tk.Frame(self.root,
                                   width=SHOP_WIDTH, height=MAZE_SIZE)
        self.shop_frame.place(x=MAZE_SIZE, y=BANNER_HEIGHT)
        self.stat_frame = tk.Frame(self.root,
                                   width=self.width, height=STATS_HEIGHT)
        self.stat_frame.place(x=0, y=MAZE_SIZE + BANNER_HEIGHT)
        self.player = self.sokoban_model._player


def get_potion(type: str) -> Potion:
    if type == STRENGTH_POTION:
        return StrengthPotion()
    elif type == MOVE_POTION:
        return MovePotion()
    elif type == FANCY_POTION:
        return FancyPotion()





def play_game(root: tk.Tk, maze_file: str) -> None:
    sokoban_model = SokobanModel(maze_file)
    width = str(MAZE_SIZE + SHOP_WIDTH)
    height = str(MAZE_SIZE + BANNER_HEIGHT + STATS_HEIGHT)

    root.title('Extra Fancy Sokoban')
    root.geometry(f'{width}x{height}')
    banner_frame = tk.Frame(root, background='red', width=width,
                                 height=BANNER_HEIGHT)
    banner_frame.place(x=0, y=0)
    maze_frame = tk.Frame(root, background='yellow', width=MAZE_SIZE,
                               height=MAZE_SIZE)
    maze_frame.place(x=0, y=BANNER_HEIGHT)
    shop_frame = tk.Frame(root, background='green', width=SHOP_WIDTH,
                               height=MAZE_SIZE)
    shop_frame.place(x=MAZE_SIZE, y=BANNER_HEIGHT)
    stat_frame = tk.Frame(root, background='blue', width=width,
                               height=STATS_HEIGHT)
    stat_frame.place(x=0, y=MAZE_SIZE + BANNER_HEIGHT)
    player = sokoban_model._player


    game_view = FancyGameView(maze_frame,
                                   sokoban_model.get_dimensions(),
                                   (MAZE_SIZE, MAZE_SIZE))
    game_view.display(sokoban_model.get_maze(),
                           sokoban_model.get_entities(),
                           sokoban_model.get_player_position())
    stat_view = FancyStatsView(stat_frame)
    stat_view.draw_stats(player.get_moves_remaining(),
                              player.get_strength(),
                              player.get_money())
    stat_view.display()
    banner_view = Banner(banner_frame, (1, 1),
                              (MAZE_SIZE + SHOP_WIDTH, BANNER_HEIGHT))
    banner_view.display((0, 0))
    shop_view = Shop(shop_frame)
    for item in sokoban_model.get_shop_items():
        potion_effect = get_potion(item).effect()
        player_function = player.apply_effect(potion_effect)
        shop_view.create_buyable_item(item,
                                           sokoban_model.get_shop_items()[
                                               item], player_function)
    shop_view.display()

def main() -> None:
    root = tk.Tk()
    play_game(root, 'maze_files/coin_maze.txt')
    root.mainloop()


if __name__ == "__main__":
	main()





