import random

from slizzle.model.slizzle_tile import SlizzleTile


class SlizzleGrid:
    def __init__(self, width: int, height: int, tiles: list[SlizzleTile]):
        self.width = width
        self.height = height
        self.grid = self.tiles_to_grid(tiles)

    def tiles_to_grid(self, tiles_list: list[SlizzleTile]) -> list[list[SlizzleTile]]:
        """ Returns a [[SlizzleTile],...]

        Used to add Tiles to the X by X Grid.
        """
        grid = []

        for w in range(self.width):
            grid.append([])
            for h in range(self.height):
                grid[w].append(tiles_list[w * self.height + h])

        return grid

    def try_swap(self, cell_pos: (int, int)) -> bool:
        """ Checks if clicked cell is neighbour with empty cell (tile)

        Checks in every direction if a neighbouring cell is invisible.
        If a neighbouring cell is invisible the clicked cell and invisible cell are swapped using swap() Method.
        Else returnn false.
        """
        x_cord = cell_pos[0]
        y_cord = cell_pos[1]

        # up
        if y_cord > 0 and not self.grid[x_cord][y_cord - 1].is_visible:
            empty_cell = tuple((x_cord, y_cord - 1))
        # right
        elif x_cord < self.width - 1 and not self.grid[x_cord + 1][y_cord].is_visible:
            empty_cell = tuple((x_cord + 1, y_cord))
        # down
        elif y_cord < self.height - 1 and not self.grid[x_cord][y_cord + 1].is_visible:
            empty_cell = tuple((x_cord, y_cord + 1))
        # left
        elif x_cord > 0 and not self.grid[x_cord - 1][y_cord].is_visible:
            empty_cell = tuple((x_cord - 1, y_cord))

        else:
            return False

        self.swap(cell_pos, empty_cell)
        return True

    def swap(self, cell_pos: (int, int), empty_pos: (int, int)) -> None:
        """ Swaps Clicked Cell with Empty cell. """
        clicked_tile = self.grid[cell_pos[0]][cell_pos[1]]
        empty_tile = self.grid[empty_pos[0]][empty_pos[1]]

        self.grid[cell_pos[0]][cell_pos[1]] = empty_tile
        self.grid[empty_pos[0]][empty_pos[1]] = clicked_tile

    def check_tiles(self) -> bool:
        """ Checks if all tiles are in the right order. """
        for h in range(self.height):
            for w in range(self.width):
                if (w, h) != self.grid[w][h].position:
                    return False
        return True

    def shuffle(self, swap_count: int) -> None:
        """ Shuffles tiles. """
        directions = 4
        # get empty coordinates
        empty_tile = self.find_empty_tile()
        # while count
        while swap_count > 0:
            x_cord, y_cord = empty_tile
            rand_direction = random.randrange(directions)
            rand_tile = None

            # up
            if rand_direction == 0 and y_cord > 0:
                rand_tile = (x_cord, y_cord - 1)
            # right
            elif rand_direction == 1 and x_cord < self.width - 1:
                rand_tile = (x_cord + 1, y_cord)
            # down
            elif rand_direction == 2 and y_cord < self.height - 1:
                rand_tile = (x_cord, y_cord + 1)
            # left
            elif rand_direction == 3 and x_cord > 0:
                rand_tile = (x_cord - 1, y_cord)

            if rand_tile is not None:
                self.swap(rand_tile, empty_tile)
                empty_tile = rand_tile
                swap_count -= 1

    def find_empty_tile(self) -> (int, int):
        for h in range(self.height):
            for w in range(self.width):
                if not self.grid[h][w].is_visible:
                    return tuple((h, w))
