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
        self._title_font = ('Arial', 14, 'bold')
        self.annotate_position((0, 1), "Player Stats", font=self._title_font)
        self.annotate_position((1, 0), "Moves remaining:")
        self.annotate_position((1, 1), "Strength:")
        self.annotate_position((1, 2), "Money:")
        self.moves_remaining = tk.IntVar()
        self.strength = tk.IntVar()
        self.money = tk.IntVar()

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
        self.create_text(self.get_midpoint((2, 2)), text=str(self.money.get()), tags='money')
        self.pack()