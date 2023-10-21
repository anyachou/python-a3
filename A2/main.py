from Entity import *
from Tile import *
from A2.a2.a2 import *


def convert_maze(game: list[list[str]]) -> tuple[Grid, Entities, Position]:
    maze = []
    boxes = {}
    player_position = ()

    for i in range(len(game)):
        raw = []
        for j in range(len(game[i])):
            symbol = game[i][j]
            if WALL == symbol:
                raw.append(Wall())
            elif GOAL == symbol:
                raw.append(Goal())
            elif symbol.isdigit():
                raw.append(Crate(int(symbol)))
                boxes[(i, j)] = int(symbol)
            else:
                raw.append(Floor())
                if PLAYER == symbol:
                    player_position = (i, j)
        maze.append(raw)
    return maze, boxes, player_position


class SokobanModel:
    maze = Grid()
    entities = Entities()
    player_position = Position()
    player_strength = 0
    player_move_remaining = 0

    def __init__(self, maze_file: str) -> None:
        raw_maze, player_stats = read_file(maze_file)
        self.maze, self.entities, self.player_position = convert_maze(raw_maze)
        self.player_strength = player_stats[0]
        self.player_move_remaining = player_stats[1]

    def get_maze(self) -> Grid:
        return self.maze

    def get_entities(self) -> Entities:
        return self.entities

    def get_player_position(self) -> tuple[int, int]:
        return self.player_position

    def get_player_moves_remaining(self) -> int:
        return self.player_move_remaining

    def get_player_strength(self) -> int:
        return self.player_strength

    def attempt_move(self, direction: str) -> bool:
        position_change_x, position_change_y = DIRECTION_DELTAS.get(direction)
        next_tile = self.maze[self.player_position[0] + position_change_x][self.player_position[1] + position_change_y]
        return isinstance(next_tile, Tile) and not next_tile.is_blocking()

    def has_won(self) -> bool:
        for array in self.maze:
            if any(GOAL == item for item in array):
                return False
        return True
