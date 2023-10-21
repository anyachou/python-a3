import tkinter as tk
from tkinter import messagebox, filedialog
from typing import Callable
from model import SokobanModel, Tile, Entity
from a2_support import *
from a3_support import *

# Write your classes and functions here
class FancyGameView(AbstractGrid):
    """ Display the game map, including tiles and entities.  """

    def __init__(self, 
                 master: tk.Frame,
                 dimensions: tuple[int, int], 
                 size: tuple[int, int], 
                 **kwargs) -> None:
        """ Constructor for AbstractGrid.

        Parameters:
            master: The master frame for this Canvas.
            dimensions: Dimensions of this grid as (#rows, #columns)
            size: (width in pixels, height in pixels)
        """
        super().__init__(master, dimensions, size)
        self._cache = {}    # store images

        return None
    
    
    def _get_image_name(self, marker):
        """ Returns image filename based on marker.

        Parameters:
            marker (str): Marker representing a tile or entity.

        Returns:
            str: Image filename associated with the marker.
        """
        if marker.get_type() == FLOOR:
            return "images/Floor.png"
        elif marker.get_type() == WALL:
            return "images/W.png"
        elif marker.get_type() == GOAL:
            return "images/G.png"
        elif marker.get_type() == FILLED_GOAL:
            return "images/F.png"
        elif marker.get_type() == CRATE:
            return "images/C.png"
        elif marker.get_type() == PLAYER:
            return "images/P.png"
        elif marker.get_type() == STRENGTH_POTION:
            return "images/S.png"
        elif marker.get_type() == MOVE_POTION:
            return "images/M.png"
        elif marker.get_type() == FANCY_POTION:
            return "images/F.png"


    def _display_image(self, marker: str, position: Position):
        """ Create image on the frame.
        
        Parameters:
            marker (str): Image path.
            position (tuple(int, int)): The location of the image.
        """
        size = self.get_cell_size()
        tile_image = get_image(marker, size, self._cache)
        self.create_image(self.get_midpoint(position), image=tile_image)
        

    def display(self, 
                maze: Grid, 
                entities: Entities, 
                player_position: Position):
        """ Turn the text-based maze and position of entities into image.

        Parameters:
            maze (Grid): A list of the maze.
            entities (Entities): A dictionary of potions and crates' positions.
            player_position (Position): A tuple of player's position.
        """
        # display tile (floor, wall & goal)
        for i, row in enumerate(maze):
            for j, marker in enumerate(row):
                if marker is not None:
                    self._display_image(self._get_image_name(marker), (i, j))

        # display entity
        for position, entity in entities.items():
            self._display_image(self._get_image_name(entity), (position))
        
        # display player
        self._display_image("images/P.png", player_position)


class FancyStatsView(AbstractGrid):
    """ Display player stats. """

    def __init__(self, master: tk.Tk) -> None:
        """ Constructor for AbstractGrid.

        Parameters:
            master: The master frame for this Canvas.
        """
        super().__init__(master, (3, 3), (MAZE_SIZE + SHOP_WIDTH, STATS_HEIGHT))
        self._cache = {}
    
    def draw_stats(self, 
                   moves_remaining: int,
                   strength: int, 
                   money: int) -> None:
        """ Display user stats, including remaining moves, strength and money.

        Parameters:
            moves_remaining (int): Remaining moves, 
                                   get by Player.get_moves_remaining.
            strength (int): Strength to move the crate,
                            get by Player.get_strength.
            money (int): Money will be used in shop, get by Player.get_money.
        """
        self.create_text(*self.get_midpoint((0, 1)), text="Play Stats", font=TITLE_FONT)
        self.create_text(*self.get_midpoint((1, 0)), text="Moves remaining:")
        self.create_text(*self.get_midpoint((1, 1)), text="Strength:")
        self.create_text(*self.get_midpoint((1, 2)), text="Money:")
        self.create_text(*self.get_midpoint((2, 0)), text=moves_remaining)
        self.create_text(*self.get_midpoint((2, 1)), text=strength)
        self.create_text(*self.get_midpoint((2, 2)), text=money)


class Shop(tk.Frame):
    """ Display item information and buttons for all buyable items. """

    def __init__(self, master: tk.Frame) -> None: 
        super().__init__(master)    

        self._master = master 

        shop_title = tk.Label(
            self._master,
            text="Shop",
            font=TITLE_FONT
        )
        shop_title.pack()

    def create_buyable_item(self, 
                            item: str, 
                            amount: int, 
                            callback: Callable[[], None]) -> None:
        """ Display items of the shop, including label and button.
        
        Parameters:
            item (str): 
            amount (int):
            callback (Callable[]):
        """

        print("iejwijeifwjef")
        # create frame in shop frame
        item_frame = tk.Frame(self._master)

        item_title = tk.Label(
            item_frame,
            text=item + ": " + amount
        )
        item_title.pack(side=tk.RIGHT)

        item_button = tk.Button(
            item_frame,
            text="Buy"
        )
        item_button.pack(side=tk.LEFT)
        
        item_frame.pack()


class FancySokobanView:
    """ Wrap all frame - banner, maze, shop and player stats - together, and 
        provides a wrap for the item small widget in shop.
    """

    def __init__(self, 
                 master: tk.Tk, 
                 dimensions: tuple[int, int], 
                 size: tuple[int, int]) -> None:
        """ Basic window setting, including window title, banner, and
            set frame for maze, shop, player stats.
        
        Parameters:
            master (tk.Tk): The window of the game.
            dimension (tuple[int, int]): (#rows, #columns)
            size (tuple[int, int]): (width in pixels, height in pixels)
        """
        self._master = master
        self._dimensions = dimensions
        self._size = size

        self._cache = {}

        # create window title
        self._master.geometry(f"{self._size[0]}x{self._size[1]}")
        self._master.title("Extra Fancy Sokoban")

        # create banner image
        banner = tk.Canvas(self._master,
                           width=MAZE_SIZE + SHOP_WIDTH,
                           height=BANNER_HEIGHT)        
        self.banner_image = get_image("images/banner.png",
                                      (MAZE_SIZE + SHOP_WIDTH, BANNER_HEIGHT),
                                      self._cache)
        banner.create_image(0, 0, anchor="nw", image=self.banner_image)
        banner.pack(side=tk.TOP)

        #set maze and shop frame
        self._maze_shop_frame = tk.Frame(self._master)
        self._maze_shop_frame.pack(side=tk.TOP)

        # set player stats frame
        self._stats_frame = tk.Frame(self._master)
        self._stats_frame.pack(side=tk.TOP)

    def display_game(self, 
                     maze: Grid, 
                     entities: Entities, 
                     player_position: Position) -> None:
        """ Clear and redraws the game view.

        Parameters:
            maze (Grid): A list of tiles (goal and wall).
            entities (Entities): A dictionary of 
                                 potion and crates' position and entity type.
            player_position (Position): A tuple of player's position.
        """
        # set frame for maze
        game = FancyGameView(self._master, (7, 8), (MAZE_SIZE, MAZE_SIZE))
        game.display(maze, entities, player_position)
        game.pack(side=tk.LEFT)

    def display_stats(self, moves: int, strength: int, money: int) -> None:
        """ Clear and redraws the stats view.

        Parameters:
            moves (int): Player's remaining moves.
            strength (int): Player's strength.
            money (int): Player's money to use in shop.
        """
        player_stats = FancyStatsView(self._master)
        player_stats.draw_stats(moves, strength, money)
        player_stats.pack(side=tk.BOTTOM)


        


class ExtraFancySokoban:
    """ Main flow of the game. """
    """ reherherhreh"""
    def __init__(self, root: tk.Tk, maze_file: str) -> None:
        """ Create shop items

        Parameters:
            root (tk.Tk): Window of the game.
            maze_file (str): Path of the maze file.
        """
        self._root = root
        self._maze_file = maze_file

        self._sokobanModel = SokobanModel(self._maze_file)

    def redraw(self) -> None:
        fancySokobanView = FancySokobanView(self._root,
                                            (1, 1),
                                            (MAZE_SIZE + SHOP_WIDTH, BANNER_HEIGHT + MAZE_SIZE + STATS_HEIGHT))
        fancySokobanView.display_stats(self._sokobanModel.get_player_moves_remaining(),
                                       self._sokobanModel.get_player_strength(),
                                       self._sokobanModel.get_player_money())
        fancySokobanView.display_game(self._sokobanModel.get_maze(), 
                                      self._sokobanModel.get_entities(), 
                                      self._sokobanModel.get_player_position())



    def handle_keypress(self, event: tk.Event) -> None:
        pass


def play_game(root: tk.Tk, maze_file: str) -> None:
    """ Construct the controller instance.
    
    Parameters:
        root (tk.Tk): main window of the game.
        maze_file (str): path of the maze file.
    """
    extraFancySokoban = ExtraFancySokoban(root, maze_file)
    extraFancySokoban.redraw()
    root.mainloop()


def main() -> None:
    """ The main function. """
    root = tk.Tk()
    play_game(root, "maze_files/maze2.txt")


if __name__ == "__main__":
    main()
