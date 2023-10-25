from a3_support import *

class Banner(AbstractGrid):

    image_path = ''
    size = ()


    def __init__(self, master: tk.Tk | tk.Frame, dimensions: tuple[int, int], size: tuple[int, int], **kwargs) -> None:
        super().__init__(master, dimensions, size)
        self.image_path = '../images/banner.png'
        self._cache = {}
        self.size = size

    def display(self, position: tuple[int, int]):
        image = get_image(self.image_path, self.size, self._cache)
        midpoint = self.get_midpoint(position)
        self.create_image(midpoint, image=image)
        self.pack()
