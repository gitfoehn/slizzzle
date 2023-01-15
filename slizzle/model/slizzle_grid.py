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
        empty_cell = None
        # up
        if cell_pos[1] > 0 and not self.grid[cell_pos[0]][cell_pos[1]-1].is_visible:
            empty_cell = tuple((cell_pos[0], cell_pos[1]-1))
        # right
        elif cell_pos[0] < self.width - 1 and not self.grid[cell_pos[0]+1][cell_pos[1]].is_visible:
            empty_cell = tuple((cell_pos[0]+1, cell_pos[1]))
        # down
        elif cell_pos[1] < self.height - 1 and not self.grid[cell_pos[0]][cell_pos[1]+1].is_visible:
            empty_cell = tuple((cell_pos[0], cell_pos[1]+1))
        # left
        elif cell_pos[0] > 0 and not self.grid[cell_pos[0]-1][cell_pos[1]].is_visible:
            empty_cell = tuple((cell_pos[0]-1, cell_pos[1]))

        else:
            return False

        self.swap(cell_pos, empty_cell)

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
