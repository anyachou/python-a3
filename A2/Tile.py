from A2.a2.a2 import *


class Tile(ABC):
    @abstractmethod
    def is_blocking(self) -> bool:
        return False

    @abstractmethod
    def get_type(self) -> str:
        return 'Abstract Tile'

    def __str__(self) -> str:
        return self.get_type()

    def __repr__(self) -> str:
        return self.get_type()


class Floor(Tile):
    is_block = False

    def is_blocking(self) -> bool:
        return self.is_block

    def get_type(self) -> str:
        return FLOOR


class Wall(Tile):
    is_block = True

    def is_blocking(self) -> bool:
        return self.is_block

    def get_type(self) -> str:
        return WALL

class Goal(Tile):
    is_block = False
    status = GOAL

    def is_blocking(self) -> bool:
        return self.is_block

    def get_type(self) -> str:
        return GOAL

    def is_filled(self) -> bool:
        return self.status == FILLED_GOAL

    def fill(self) -> None:
        if not self.is_filled():
            self.status = FILLED_GOAL

    def unfill(self) -> None:
        if self.is_filled():
            self.status = GOAL
