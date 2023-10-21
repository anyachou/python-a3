from abc import ABC, abstractmethod
from a2_support import * 

# Write your classes here
class Tile():
    """ Basic definition of initializing Tiles  """
    def is_blocking(self)->bool:
        return False
    def get_type(self)->str:
        return 'Abstract Tile'
    def __str__(self)->str:
        return self.get_type()
    def __repr__(self)->str:
        return self.__str__()
class Floor(Tile):
    """check floor status if it is blocking"""
    def is_blocking(self)->bool:
        return False
    def get_type(self)->str:
        return FLOOR
    def __str__(self)->str:
        return self.get_type()
    def __repr__(self)->str:
        return FLOOR
class Wall(Tile):
    """check wall status if it is blocking"""
    def is_blocking(self)->bool:
        return True
    def get_type(self)->str:
        return WALL
    def __str__(self)->str:
        return self.get_type()
    def __repr__(self)->str:
        return WALL
class Goal(Tile):
    """check the goal' status, is filled or unfill"""
    _goal=GOAL
    def is_blocking(self)->bool:
        return False
    def get_type(self)->str:
        return GOAL
    def __str__(self)->str:
        return FILLED_GOAL if self.is_filled() else GOAL
    def __repr__(self)->str:
        return FILLED_GOAL if self.is_filled() else GOAL
    def is_filled(self)->bool:
        return self._goal == FILLED_GOAL
    def fill(self)->None:
        if not self.is_filled():
            self._goal=FILLED_GOAL
    def unfill(self) -> None:
        if self.is_filled():
            self._goal=GOAL
class Entity():
    def get_type(self)->str:
        return "Abstract Entity"
    def is_movable(self)->bool:
        pass
    def __str__(self)->str:
        return "Abstract Entity"
    def __repr__(self)->str:
        return "Abstract Entity"
class Crate(Entity):
    strength = 0
    def __init__(self, strength: int) -> None:
        self.strength = strength
    def get_strength(self) -> int:
        return self.strength
    def get_type(self)->str:
        return CRATE
    def is_movable(self)->bool:
        return True
    def __str__(self)->str:
        return str(self.strength)
    def __repr__(self)->str:
        return str(self.strength)
class Potion(Entity):
    def effect(self) -> dict[str, int]:
        return {};
    def get_type(self)->str:
        return "Potion"
    def is_movable(self)->bool:
        return False
    def __str__(self)->str:
        return "Potion"
    def __repr__(self)->str:
        return "Potion"
class StrengthPotion(Potion):
    def effect(self) -> dict[str, int]:
        return {'strength': 2}
    def get_type(self)->str:
        return STRENGTH_POTION
    def is_movable(self)->bool:
        return False
    def __str__(self)->str:
        return STRENGTH_POTION
    def __repr__(self)->str:
        return STRENGTH_POTION
class MovePotion:
    def effect(self) -> dict[str, int]:
        return {'moves': 5}
    def get_type(self)->str:
        return MOVE_POTION
    def is_movable(self)->bool:
        return False
    def __str__(self)->str:
        return MOVE_POTION
    def __repr__(self)->str:
        return MOVE_POTION
class FancyPotion:
    def effect(self) -> dict[str, int]:
        return {'strength': 2, 'moves':2}
    def get_type(self)->str:
        return FANCY_POTION
    def is_movable(self)->bool:
        return False
    def __str__(self)->str:
        return FANCY_POTION
    def __repr__(self)->str:
        return FANCY_POTION
class Player(Entity):
    strength = 0
    move = 0
    def get_type(self)->str:
        return PLAYER
    def is_movable(self)->bool:
        return self.move != 0
    def __str__(self)->str:
        return PLAYER
    def __repr__(self)->str:
        return PLAYER
    def __init__(self, start_strength: int, moves_remaining: int) ->None:
        self.strength = start_strength
        self.move = moves_remaining
    def get_strength(self)-> int:
        return self.strength 
    def add_strength(self, amount:int)-> None:
        self.strength += amount 
    def get_moves_remaining(self) -> int:
        return self.move
    def add_moves_remaining(self, amount: int) -> None:
        self.move += amount
    def apply_effect(self, potion_effect: dict[str, int]) -> None:
        if not potion_effect.get("strength") is None:
            self.strength += potion_effect.get("strength")
        if not potion_effect.get("moves") is None:
            self.move += potion_effect.get("moves")
        
def main():
    # uncomment the lines below once you've written your Sokoban class
    # game = Sokoban('maze_files/maze1.txt')
    # game.play_game()
    tile = Tile
    floor = Floor
    wall = Wall
    goal = Goal
    entity = Entity
    crate = Crate
    potion = Potion
    strenghpotion =StrengthPotion
    movepotion = MovePotion
    fancypotion = FancyPotion
    player = Player

if __name__ == '__main__':
    main()
