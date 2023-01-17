from slizzle.model.slizzle_tile import SlizzleTile
from slizzle.model.slizzle_grid import SlizzleGrid


class SlizzleModel:
    """
    Slizzle Model
    """
    def __init__(self, tiles: list[SlizzleTile], difficulty):
        self.width = difficulty.tile_amount_horizontal
        self.height = difficulty.tile_amount_vertical
        self.tiles = tiles
        self.grid = None
        self.moves = 0
        self.shuffles = difficulty.shuffle_amount

    def hide_last_tile(self) -> None:
        """
        Hides the Last Tile in the List of Tiles.
        Sets its Visible for the last Tile to False.
        """
        self.tiles[len(self.tiles)-1].is_visible = False

    def show_all_tiles(self) -> None:
        """
        Sets all Tiles to Visible.
        Used when game is Won. (comlpleted)
        """
        for tile in self.tiles:
            tile.is_visible = True

    def start_game(self) -> None:
        self.hide_last_tile()
        self.grid = SlizzleGrid(self.width, self.height, self.tiles)
        self.grid.shuffle(self.shuffles)

    def grid_swap(self, clicked_cell_pos: (int, int)) -> None:
        if self.grid.try_swap(clicked_cell_pos):
            self.increment_moves()
            if self.grid.check_tiles():
                self.game_end()

    def game_end(self) -> None:
        self.show_all_tiles()
        print(f'Du geile Sau hast es in {self.moves} Zügen geschafft')

    def increment_moves(self):
        self.moves += 1

    def reset_moves(self):
        self.moves = 0


class Difficulty:
    """
    Helper Class to set Difficulty of a Game.
    - example Hard = 5 X 5 Tiles Shuffled for 100 times
    """
    def __init__(self, name: str, horizontal: int, vertical: int, shuffles: int):
        self.name = name
        self.res = (horizontal, vertical)
        self.tile_amount_horizontal = horizontal
        self.tile_amount_vertical = vertical
        self.shuffle_amount = shuffles
