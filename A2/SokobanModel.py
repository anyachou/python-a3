from Tile import *


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
                raw.append(Floor())
                boxes[(i, j)] = Crate(int(symbol))
            else:
                raw.append(Floor())
                if PLAYER == symbol:
                    player_position = (i, j)
                elif STRENGTH_POTION == symbol:
                    boxes[(i, j)] = StrengthPotion()
                elif MOVE_POTION == symbol:
                    boxes[(i, j)] = MovePotion()
                elif FANCY_POTION == symbol:
                    boxes[(i, j)] = FancyPotion()
        maze.append(raw)
    return maze, boxes, player_position


class SokobanModel:
    maze = Grid()
    entities = Entities()
    player_position = Position()
    player = Player(0, 0)
    raw_maze = []

    def __init__(self, maze_file: str) -> None:
        raw_maze, player_stats = read_file(maze_file)
        self.raw_maze = raw_maze
        self.maze, self.entities, self.player_position = convert_maze(raw_maze)
        self.player = Player(player_stats[0], player_stats[1])

    def get_maze(self) -> Grid:
        return self.maze

    def get_entities(self) -> Entities:
        return self.entities

    def get_player_position(self) -> tuple[int, int]:
        return self.player_position

    def get_player_moves_remaining(self) -> int:
        return self.player.get_moves_remaining()

    def get_player_strength(self) -> int:
        return self.player.get_strength()

    def attempt_move(self, direction: str) -> bool:
        direction_data = DIRECTION_DELTAS.get(direction, (0, 0))
        if direction_data == (0, 0):
            return False
        position_change_x, position_change_y = direction_data
        next_x = self.player_position[0] + position_change_x
        next_y = self.player_position[1] + position_change_y
        movable = False
        entity = self.entities.get((next_x, next_y))
        if isinstance(entity, Potion):
            self.player.apply_effect(entity.effect())
            self.entities.pop((next_x, next_y))
            movable = True
        elif isinstance(entity, Crate):
            if self.entities.get((next_x + position_change_x, next_y + position_change_y)) is None:
                tile = self.maze[next_x + position_change_x][next_y + position_change_y]
                assert isinstance(tile, Tile)
                if not tile.is_blocking() and self.player.get_strength() >= entity.get_strength():
                    self.player.add_moves_remaining(-1)
                    self.player_position = (next_x, next_y)
                    self.entities.pop((next_x, next_y))
                    self.entities[(next_x + position_change_x, next_y + position_change_y)] = entity
                    movable = True
                    if isinstance(tile, Goal) and not tile.is_filled():
                        tile.fill()
        else:
            tile = self.maze[next_x][next_y]
            if isinstance(tile, Tile) and not tile.is_blocking():
                self.player.add_moves_remaining(-1)
                self.player_position = (next_x, next_y)
                movable = True

        return movable

    def has_won(self) -> bool:
        for array in self.maze:
            if any(isinstance(item, Goal) and not item.is_filled() for item in array):
                return False
        return True
