from a3_support import *
from model import *

class FancyGameView(AbstractGrid):

    image_paths = None
    size = None

    # 初始化
    def __init__(self, master: tk.Tk | tk.Frame, dimensions: tuple[int, int], size: tuple[int, int], **kwargs) -> None:
        super().__init__(master, dimensions, size)
        self._cache = {}
        self.image_paths = {
            COIN: '../images/$.png',
            WALL: '../images/W.png',
            FLOOR: '../images/Floor.png',
            GOAL: '../images/G.png',
            CRATE: '../images/C.png',
            FILLED_GOAL: '../images/X.png',
            PLAYER: '../images/P.png',
            FANCY_POTION: '../images/F.png',
            MOVE_POTION: '../images/M.png',
            STRENGTH_POTION: '../images/S.png'
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

