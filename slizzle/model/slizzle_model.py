from random import shuffle
from slizzle.model.slizzle_tile import SlizzleTile
from slizzle.model.slizzle_grid import SlizzleGrid


class SlizzleModel:
    def __init__(self, size: (int, int), tiles: list[SlizzleTile]):
        self.width = size[0]
        self.height = size[1]
        self.tiles = tiles
        self.grid = None

    def hide_last_tile(self) -> None:
        self.tiles[len(self.tiles)-1].is_visible = False

    def show_all_tiles(self) -> None:
        for tile in self.tiles:
            tile.is_visible = True

    def shuffle_tiles(self) -> None:
        shuffle(self.tiles)

    def start_game(self) -> None:
        self.hide_last_tile()
        self.shuffle_tiles()
        self.grid = SlizzleGrid(self.width, self.height, self.tiles)

    def grid_swap(self, clicked_cell_pos: (int, int)) -> bool:
        return self.grid.try_swap(clicked_cell_pos)

    def game_end(self) -> None:
        self.show_all_tiles()
