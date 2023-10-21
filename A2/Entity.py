from A2.a2.a2 import *


class Entity(ABC):
    @abstractmethod
    def get_type(self) -> str:
        return "Abstract Entity"

    @abstractmethod
    def is_movable(self) -> bool:
        pass

    def __str__(self) -> str:
        return self.get_type()

    def __repr__(self) -> str:
        return self.get_type()


class Crate(Entity):
    strength = 0

    def __init__(self, strength: int) -> None:
        self.strength = strength

    def get_strength(self) -> int:
        return self.strength

    def get_type(self) -> str:
        return CRATE

    def is_movable(self) -> bool:
        return True


class Potion(Entity, ABC):
    @abstractmethod
    def effect(self) -> dict[str, int]:
        return {}

    @abstractmethod
    def get_type(self) -> str:
        return "Potion"

    def is_movable(self) -> bool:
        return False


class StrengthPotion(Potion):
    def effect(self) -> dict[str, int]:
        return {'strength': 2}

    def get_type(self) -> str:
        return STRENGTH_POTION


class MovePotion(Potion):
    def effect(self) -> dict[str, int]:
        return {'moves': 5}

    def get_type(self) -> str:
        return MOVE_POTION


class FancyPotion(Potion):
    def effect(self) -> dict[str, int]:
        return {'strength': 2, 'moves': 2}

    def get_type(self) -> str:
        return FANCY_POTION


class Player(Entity):
    strength = 0
    move = 0

    def __init__(self, start_strength: int, moves_remaining: int) -> None:
        self.strength = start_strength
        self.move = moves_remaining

    def get_type(self) -> str:
        return PLAYER

    def is_movable(self) -> bool:
        return self.move != 0

    def get_strength(self) -> int:
        return self.strength

    def add_strength(self, amount: int) -> None:
        self.strength += amount

    def get_moves_remaining(self) -> int:
        return self.move

    def add_moves_remaining(self, amount: int) -> None:
        self.move += amount

    def apply_effect(self, potion_effect: dict[str, int]) -> None:
        potion_move = potion_effect.get("moves")
        potion_strength = potion_effect.get("strength")
        if not potion_strength is None:
            self.strength += potion_strength
        if not potion_move is None:
            self.move += potion_move
