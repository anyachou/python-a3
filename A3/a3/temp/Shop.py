from typing import Callable

from a3_support import *
from model import *


class Shop(tk.Frame):
    items = {}

    def __init__(self, master: tk.Frame) -> None:
        super().__init__(master)

    # callback = SokobanModel().get_shop_items()
    def create_buyable_item(self, item: str, amount: int, callback: Callable[[], None]) -> None:
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

        label = tk.Label(self, text='Shop', anchor='n', font=('Arial', 20, 'bold'))
        label.grid(row=0, column=0)
        init_row = 1
        for item in self.items:
            text = tk.Label(self, text=item + ': $' + str(self.items[item]), font=('Arial', 16))
            text.grid(row=init_row, column=0)
            button = tk.Button(self, text='Buy')
            button.grid(row=init_row, column=1)
            init_row += 1
        self.pack()
