from a2_support import *

# Write your classes here
class Tile():
	""" Locating tile in this map elements """

	def is_blocking(self) -> bool:
		"""check tile is blocking return false"""
		return False

	def get_type(self) -> str:
		"""return tile's type"""
		return 'Abstract Tile'

	def __str__(self) -> str:
		return self.get_type()

	def __repr__(self) -> str:
		return self.__str__()

class Floor(Tile):
	""" check the status of floor"""

	def is_blocking(self) -> bool:
		"""check floor is blocking then return false"""
		return False

	def get_type(self) -> str:
		"""returns floor's type"""
		return FLOOR

	def __str__(self) -> str:
		return self.get_type()

	def __repr__(self) -> str:
		return FLOOR

class Wall(Tile):
	""" check the status of wall"""

	def is_blocking(self) -> bool:
		"""check wall is blocking return true"""
		return True

	def get_type(self) -> str:
		"""return wall's type"""
		return WALL

	def __str__(self) -> str:
		return self.get_type()

	def __repr__(self) -> str:
		return WALL

class Goal(Tile):
	"""check the status of goal"""
	_goal = GOAL

	def is_blocking(self) -> bool:
		"""check if goal is blocking returns false"""
		return False

	def get_type(self) -> str:
		"""returns goal's type"""
		return GOAL

	def __str__(self) -> str:
		return FILLED_GOAL if self.is_filled() else GOAL

	def __repr__(self) -> str:
		return FILLED_GOAL if self.is_filled() else GOAL

	def is_filled(self) -> bool:
		"""check the goal whether it is filled then get 'X' """
		return self._goal == FILLED_GOAL

	def fill(self) -> None:
		""" if the tile is not filled then get 'X'
		"""
		if not self.is_filled():
			self._goal = FILLED_GOAL

	def unfill(self) -> None:
		""" if tile is unfilled then get 'G'
		"""
		if self.is_filled():
			self._goal = GOAL

class Entity():
	""" check the map is entity or not"""

	def get_type(self) -> str:
		"""return the string"""
		return "Abstract Entity"

	def is_movable(self) -> bool:
		"""check the objectives is movable or not"""
		pass

	def __str__(self) -> str:
		return "Abstract Entity"

	def __repr__(self) -> str:
		return "Abstract Entity"

class Crate(Entity):
	"""check the crate status"""
	strength = 0

	def __init__(self, strength: int) -> None:
		self.strength = strength

	def get_strength(self) -> int:
		"""get the strength returns strength"""
		return self.strength

	def get_type(self) -> str:
		"""returns crate's type"""
		return CRATE

	def is_movable(self) -> bool:
		"""check crate is movable then returns true"""
		return True

	def __str__(self) -> str:
		return str(self.strength)

	def __repr__(self) -> str:
		return str(self.strength)

class Potion(Entity):
	"""Check the potion status"""

	def effect(self) -> dict[str, int]:
		"""get the effect of potion then return a dictionary """
		return {};

	def get_type(self) -> str:
		return "Potion"

	def is_movable(self) -> bool:
		return False

	def __str__(self) -> str:
		return "Potion"

	def __repr__(self) -> str:
		return "Potion"

class StrengthPotion(Potion):
	"""Check the strength potion status"""

	def effect(self) -> dict[str, int]:
		return {'strength': 2}

	def get_type(self) -> str:
		return STRENGTH_POTION

	def is_movable(self) -> bool:
		return False

	def __str__(self) -> str:
		return STRENGTH_POTION

	def __repr__(self) -> str:
		return STRENGTH_POTION

class MovePotion(Potion):
	"""Check the move potion status"""

	def effect(self) -> dict[str, int]:
		return {'moves': 5}

	def get_type(self) -> str:
		return MOVE_POTION

	def is_movable(self) -> bool:
		return False

	def __str__(self) -> str:
		return MOVE_POTION

	def __repr__(self) -> str:
		return MOVE_POTION

class FancyPotion(Potion):
	"""Check the fancy potion status"""

	def effect(self) -> dict[str, int]:
		return {'strength': 2, 'moves': 2}

	def get_type(self) -> str:
		"""returns fancy potion's type"""
		return FANCY_POTION

	def is_movable(self) -> bool:
		"""check fancy potion is movable"""
		return False

	def __str__(self) -> str:
		return FANCY_POTION

	def __repr__(self) -> str:
		return FANCY_POTION

class Player(Entity):
	"""Check the player status"""
	strength = 0
	move = 0

	def get_type(self) -> str:
		return PLAYER

	def is_movable(self) -> bool:
		# check player is movable
		return self.move != 0

	def __str__(self) -> str:
		return PLAYER

	def __repr__(self) -> str:
		return PLAYER

	def __init__(self, start_strength: int, moves_remaining: int) -> None:
		"""construct the player and get the strength initially and remaining moves"""
		self.strength = start_strength
		self.move = moves_remaining

	def get_strength(self) -> int:
		"""get the initial strength"""
		return self.strength

	def add_strength(self, amount: int) -> None:
		"""get the added strength"""
		self.strength += amount

	def get_moves_remaining(self) -> int:
		"""get remaining moves"""
		return self.move

	def add_moves_remaining(self, amount: int) -> None:
		"""check how many moves adds"""
		self.move += amount

	def apply_effect(self, potion_effect: dict[str, int]) -> None:
		"""check the potion effect including strength and moves getting"""
		if not potion_effect.get("strength") is None:
			self.strength += potion_effect.get("strength")
		if not potion_effect.get("moves") is None:
			self.move += potion_effect.get("moves")

def convert_maze(game: list[list[str]]) -> tuple[Grid, Entities, Position]:
	"""check the map and the location of all elements
			Returns a tuple :maze, boxes and the position of player"""
	maze = []
	boxes = {}
	player_position = ()
	for i in range(len(game)): # check all elements
		raw = []
		for j in range(len(game[i])):
			symbol = game[i][j]
			if WALL == symbol:
				raw.append(Wall())
			elif GOAL == symbol:
				raw.append(Goal())
			elif symbol.isdigit():  # if is the digit, is a crate
				raw.append(Floor())  # it is seen as the floor
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
    """the model of this game """
    maze = Grid()
    entities = Entities()
    player_position = Position()
    player = Player(0, 0)
    snapshot_maze = None
    snapshot_entities = None
    snapshot_player_position = None
    snapshot_player = None

    def __init__(self, maze_file: str) -> None:
        """construct this object"""
        raw_maze, player_stats = read_file(maze_file)
        self.maze, self.entities, self.player_position = convert_maze(raw_maze)
        # get the player's strength and remaining moves
        self.player = Player(player_stats[0], player_stats[1])

    def get_maze(self) -> Grid:
	    """Get the maze."""
	    return self.maze

    def get_entities(self) -> Entities:
	    """Get the entities."""
	    return self.entities

    def get_player_position(self) -> tuple[int, int]:
	    """Get the player's position as a tuple."""
	    return self.player_position

    def get_player_moves_remaining(self) -> int:
	    """Get the player's remaining moves."""
	    return self.player.get_moves_remaining()

    def get_player_strength(self) -> int:
	    """Get the player's strength."""
	    return self.player.get_strength()

    def attempt_move(self, direction: str) -> bool:
        """Return False if player move is invalid, or update player
        position and remaining moves  then returns True."""
        direction_data = DIRECTION_DELTAS.get(direction, (0, 0))
        if direction_data == (0, 0):  # if invalid moves returns false
            return False
        """ Clone currently game stats into snapshot object for undo feature"""
        self.snapshot_maze = self.maze
        self.snapshot_entities = dict(self.entities)
        self.snapshot_player_position = self.player_position
        self.snapshot_player = Player(self.player.get_strength(),
                                      self.player.get_moves_remaining())

        """check invalid moves conditions: player meets wall or strength is not 
        enough or crate is not movable or crate meets crate or potion"""

        position_change_x, position_change_y = direction_data  # change position
        next_x = self.player_position[0] + position_change_x
        next_y = self.player_position[1] + position_change_y

        obj = self.entities.get((next_x, next_y))
        move_validation = MoveValidation()
        if isinstance(obj, Potion):
            move_validation = MoveValidationToPotion()
        elif isinstance(obj, Crate):
            move_validation = MoveValidationToCrate()
        else:
            move_validation = MoveValidationToTile()
            obj = self.maze[next_x][next_y]

        is_movable = valid_move(move_validation, obj, self.maze, self.entities, self.player,
                                (next_x, next_y), (position_change_x, position_change_y))

        if is_movable:
	        # is movable then update new position and remaining moves
            self.player_position = (next_x, next_y)
            self.player.add_moves_remaining(-1)

        return is_movable

    def has_won(self) -> bool:
        """check won condition returns true"""
        for array in self.maze:
            if any(isinstance(item, Goal) and not item.is_filled() for item in array):
                return False
        return True

    def undo(self) -> None:
        """Revert game stats from snapshot object"""
        self.maze = self.snapshot_maze
        self.entities = dict(self.snapshot_entities)
        self.player_position = self.snapshot_player_position
        self.player = Player(self.snapshot_player.get_strength(),
                             self.snapshot_player.get_moves_remaining())

class MoveValidation:
    """Check valid move, returns False."""

    def valid_move(self, obj, maze, entities, player, position,
                   position_move) -> bool:
	    """Check if the player's move is valid, returns False."""
	    return False

class MoveValidationToPotion(MoveValidation):
    """Check player move to potion, returns True."""
    def valid_move(self, obj: Potion, maze: Grid, entities: Entities, player: Player, position: tuple[int, int],
                   position_move: tuple[int, int]) -> bool:
        """Check player's move invalidation, apply potion effect,
         and update its position."""
        player.apply_effect(obj.effect())
        entities.pop(position)
        return True


class MoveValidationToCrate(MoveValidation):
    """Check if the player moves to a crate.
    Returns: True if the move is valid and executed successfully
    """
    def valid_move(self, obj: Crate, maze: Grid, entities: Entities, player: Player, position: tuple[int, int],
                   position_move: tuple[int, int]) -> bool:
        """Calculate the new position after the move."""
        change_x = position[0] + position_move[0]
        change_y = position[1] + position_move[1]

        # Check if the target position is empty.
        if entities.get((change_x, change_y)) is None:
            # Get the tile at the target position.
            tile = maze[change_x][change_y]

            # Ensure that the tile is an instance of Tile.
            assert isinstance(tile, Tile)

            # Check if the player is strong enough to move the crate.
            is_player_strong = player.get_strength() >= obj.get_strength()

            # Check if the tile is not blocking and the player is strong enough.
            if not tile.is_blocking() and is_player_strong:
                # Remove the crate from its current position.
                entities.pop(position)

                # If the target tile is a Goal and not filled, fill it.
                if isinstance(tile, Goal) and not tile.is_filled():
                    tile.fill()
                else:
                    # Place the crate at the new position.
                    entities[(change_x, change_y)] = obj

                return True

        return False



class MoveValidationToTile(MoveValidation):
    """Check if the player can move to a tile without blocking.
    Returns:
    True if the move is valid, the target tile is not blocking.
    """
    def valid_move(self, obj: Tile, maze: Grid, entities: Entities, player: Player, position: tuple[int, int],
                   position_move: tuple[int, int]) -> bool:
        # Get the tile at the player's current position.
        tile = maze[position[0]][position[1]]

        # Check if the tile is an instance of Tile and not blocking.
        return isinstance(tile, Tile) and not tile.is_blocking()

def valid_move(move_validation: MoveValidation, obj, maze, entities, player, position, position_move) -> bool:
    """Validate a move using the provided MoveValidation instance.
    Returns:
    True if the move is valid, as determined by the MoveValidation instance.
    """
    return move_validation.valid_move(obj, maze, entities, player, position, position_move)


class Sokoban:
	""" the user interface of this game """
	model = None
	sokobanView = SokobanView()

	def __init__(self, maze_file: str) -> None:
		"""construct an instance of the SokobanModel class"""
		self.model = SokobanModel(maze_file)

	def display(self) -> None:
		"""call the methods in SokobanView class"""
		self.sokobanView.display_game(
			self.model.get_maze(),
			self.model.get_entities(),
			self.model.get_player_position()
		)
		self.sokobanView.display_stats(
			self.model.get_player_moves_remaining(),
			self.model.get_player_strength()
		)

	def play_game(self) -> None:
		"""run the main game"""
		while not (
				self.model.has_won() or self.model.get_player_moves_remaining() == 0):
			self.display()
			user_move = input('Enter move: ')
			if user_move == 'q':
				return
			elif user_move == 'u':
				self.model.undo()
				continue

			if not self.model.attempt_move(user_move):
				print('Invalid move\n')

		if self.model.has_won():
			self.display()
			print('You won!')
		else:
			print('You lost!')

def main():
	Sokoban('maze_files/maze2.txt').play_game()

if __name__ == '__main__':
	main()
