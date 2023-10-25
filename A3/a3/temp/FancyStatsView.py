from a3_support import *


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

    def draw_stats(self, moves_remaining:int, strength: int, money: int) -> None:
        self.moves_remaining = str(moves_remaining)
        self.strength = str(strength)
        self.money = str(money)

    def display(self, moves_remaining:int, strength: int, money: int):
        self.draw_stats(moves_remaining, strength, money)
        width = MAZE_SIZE + SHOP_WIDTH
        self.create_rectangle(0, MAZE_SIZE + BANNER_HEIGHT, width, MAZE_SIZE + BANNER_HEIGHT + STATS_HEIGHT, fill='white')
        self.create_text(0, STATS_HEIGHT / 4, text='Player Stats')
        self.create_text(width - 40, STATS_HEIGHT / 2, text='moves_remaining')
        self.create_text(width, STATS_HEIGHT / 2, text='strength')
        self.create_text(width + 40, STATS_HEIGHT / 2, text='money')
        self.create_text(width - 40, STATS_HEIGHT * 3 / 4, text=self.moves_remaining)
        self.create_text(width , STATS_HEIGHT * 3 / 4, text=self.strength)
        self.create_text(width + 40, STATS_HEIGHT * 3 / 4, text=self.money)
        self.pack()
