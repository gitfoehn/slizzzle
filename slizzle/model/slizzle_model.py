from random import shuffle
from slizzle.model.slizzle_tile import SlizzleTile
from slizzle.model.slizzle_grid import SlizzleGrid


class SlizzleModel:
    def __init__(self, width: int, height: int, tiles: list[SlizzleTile]):
        self.width = width
        self.height = height
        self.tiles = tiles
        self.grid = SlizzleGrid(width, height, tiles)

    def hide_last_tile(self) -> None:
        self.tiles[len(self.tiles)].is_visible = False

    def show_all_tiles(self) -> None:
        for tile in self.tiles:
            tile.is_visible = True

    def shuffle_tiles(self) -> None:
        shuffle(self.tiles)

    def start_game(self) -> None:
        self.hide_last_tile()
        self.shuffle_tiles()

    def game_end(self) -> None:
        self.show_all_tiles()
