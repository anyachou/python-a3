import tkinter as tk
from tkinter import messagebox, filedialog
from typing import Callable, Union
from PIL import Image, ImageTk

def get_image(
    image_name: str,
    size: tuple[int, int],
    cache: dict[str, ImageTk.PhotoImage] = None
) -> ImageTk.PhotoImage:
    """ Returns the cached image for image_id if one exists, otherwise creates a
        new one, caches and returns it.

    Parameters:
        image_name: The path to the image to load.
        size: The size to resize the image to, as (width, height).
        cache: The cache to use. If None, no caching is performed.

    Returns:
        The image for the given image_name, resized appropriately.
    """
    if cache is None or image_name not in cache:
        image = ImageTk.PhotoImage(image=Image.open(image_name).resize(size))
        if cache is not None:
            cache[image_name] = image
    elif image_name in cache:
        return cache[image_name]
    return image


class AbstractGrid(tk.Canvas):
    """ A type of tkinter Canvas that provides support for using the canvas as a
        grid (i.e. a collection of rows and columns). """

    def __init__(
        self,
        master: Union[tk.Tk, tk.Frame],
        dimensions: tuple[int, int],
        size: tuple[int, int],
        **kwargs
    ) -> None:
        """ Constructor for AbstractGrid.

        Parameters:
            master: The master frame for this Canvas.
            dimensions: (#rows, #columns)
            size: (width in pixels, height in pixels)
        """
        super().__init__(
            master,
            width=size[0] + 1,
            height=size[1] + 1,
            highlightthickness=0,
            **kwargs
        )
        self._size = size
        self.set_dimensions(dimensions)

class FancyGameView(AbstractGrid):
    """ Display the game map, including tiles and entities.  """

    def __init__(self, master: tk.Tk, dimensions: tuple[int, int],
	             size: tuple[int, int], **kwargs) -> None:
        super().__init__(master, dimensions, size)
        self._cache = {}

    def display_image(self, image_path: str, position: tuple[int, int]):
        """ Display an image on the canvas at the specified position. """
        image = get_image(image_path, (50, 50), self._cache)  # Assuming you want to resize the image to 50x50 pixels
        self.create_image(0,0, image=image, anchor=tk.nw)


def main() -> None:
    root = tk.Tk()
    test_frame = tk.Canvas(root, background="red")
    # view = FancyGameView(root, (10, 10), (500, 500))
    test_frame.pack(side=tk.TOP)
    # view.pack()
    # view.display_image("images/C.png", (10, 10))  # Replace with your image path
    root.mainloop()

if __name__ == "__main__":
    main()
