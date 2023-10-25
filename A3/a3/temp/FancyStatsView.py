from a3_support import *


class FancyStatsView(AbstractGrid):
    """Display the game of stats"""
    moves_remaining = ''
    strength = ''
    money = ''

    def __init__(self, master: tk.Tk | tk.Frame) -> None:
        """Initializes the FancyStatsView."""
        super().__init__(master, (3, 3),
                         (MAZE_SIZE + SHOP_WIDTH, STATS_HEIGHT))
        self._cache = {}
        self._title_font = ('Arial', 14, 'bold')
        self.annotate_position((0, 1), "Player Stats", font=self._title_font)
        self.annotate_position((1, 0), "Moves remaining:")
        self.annotate_position((1, 1), "Strength:")
        self.annotate_position((1, 2), "Money:")

    def draw_stats(self, moves_remaining:int, strength: int, money: int) -> None:
        self.moves_remaining = str(moves_remaining)
        self.strength = str(strength)
        self.money = str(money)

    def display(self):
        self.annotate_position((2, 0), self.moves_remaining)
        self.annotate_position((2, 1), self.strength)
        self.annotate_position((2, 2), self.money)
        self.pack()