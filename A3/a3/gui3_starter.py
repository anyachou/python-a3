import tkinter as tk
from PIL import ImageTk, Image
from gui3_support import *

# Create your TicTacToeView class here

class TicTacToe:
    def __init__(self, master):
        self._master = master
        master.title('Tic Tac Toe')

        self._model = TicTacToeModel()
        self._view = TicTacToeView(master)
        self._view.pack()

        # Draw the initial state to the view

        # Add your bindings here

    def attempt_move(self, event: tk.Event) -> None:
        pass


if __name__ == '__main__':
    root = tk.Tk()
    app = TicTacToe(root)
    root.mainloop()
