from typing import Callable

from a3_support import *
from model import *


class Shop(tk.Frame):
    items = {}

    def __init__(self, master: tk.Frame) -> None:
        super().__init__(master)

    def create_buyable_item(self, item: str, amount: int, callback: Callable[[], None]) -> None:
        self.items[item + '_' + str(amount)] = callback

    def create_shop_items(self, items: dict[str, int], player: Player):
        for item in items.keys():
            item_name = ''
            potion = None
            if item == MOVE_POTION:
                item_name = 'Move Potion'
                potion = MovePotion()
            elif item == STRENGTH_POTION:
                item_name = 'Strengh Potion'
                potion = StrengthPotion()
            elif item == FANCY_POTION:
                item_name = 'Fancy Potion'
                potion = FancyPotion()

            amount = items[item]
            self.create_buyable_item(item_name, amount, lambda: player.apply_effect(potion.effect()))

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
