from slizzle.model.slizzle_grid import SlizzleGrid
from slizzle.model.slizzle_tile import SlizzleTile


class SlizzleModel:
	"""
	SlizzleModel is the model of the Slizzle application according to the MVC pattern.

	The Model handles all the game logic for a sliding puzzle.
	"""

	def __init__(self, tiles: list[SlizzleTile] | None, difficulty):
		"""
		Creates a new Model.
		"""
		self.width = difficulty.tile_amount_horizontal
		self.height = difficulty.tile_amount_vertical
		self.tiles = tiles
		self.grid = None
		self.moves = 0
		self.shuffles = difficulty.shuffle_amount
		self.is_running = False

	def hide_last_tile(self) -> None:
		"""
		Hides the Last Tile in the List of Tiles (Which is the lower right corner).
		"""
		self.tiles[len(self.tiles) - 1].is_visible = False

	def show_all_tiles(self) -> None:
		"""
		Sets all Tiles to Visible.
		Used when puzzle is solved.
		"""
		for tile in self.tiles:
			tile.is_visible = True

	def start_game(self) -> None:
		"""
		Initializes the game.
		"""
		self.is_running = True
		self.hide_last_tile()
		self.grid = SlizzleGrid(self.width, self.height, self.tiles)
		self.grid.shuffle(self.shuffles)

	def grid_swap(self, clicked_cell_pos: (int, int)) -> None:
		"""
		Tries to swap the clicked tile with the neighbouring empty tile.
		"""
		if self.grid.try_swap(clicked_cell_pos):
			self.moves += 1
			if self.grid.check_tiles():
				self.game_end()

	def game_end(self) -> None:
		"""
		Sets the game to an end state.
		"""
		self.show_all_tiles()
		self.is_running = False
		print(f'Du geile Sau hast es in {self.moves} Zügen geschafft')


class Difficulty:
	"""
	Helper class for difficulties of the game.
	Sets the amount of tiles the puzzle will have and how many times it will be shuffled
	e.g. hard = 5 x 5 tiles shuffled for 100 times
	"""

	def __init__(self, name: str, horizontal: int, vertical: int, shuffles: int):
		self.name = name
		self.res = (horizontal, vertical)
		self.tile_amount_horizontal = horizontal
		self.tile_amount_vertical = vertical
		self.shuffle_amount = shuffles
