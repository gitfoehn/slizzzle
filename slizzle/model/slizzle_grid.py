from slizzle.model.slizzle_tile import SlizzleTile


class SlizzleGrid:
    def __init__(self, width: int, height: int, tiles: list[SlizzleTile]):
        self.width = width
        self.height = height
        self.grid = self.tiles_to_grid(tiles)

    def tiles_to_grid(self, tiles_list: list[SlizzleTile]) -> list[list[SlizzleTile]]:
        grid = []

        for h in range(self.height):
            grid.append([])
            for w in range(self.width):
                grid[h].append(tiles_list[h * self.width + w])

        return grid

    def check_tiles(self) -> bool:
        for h in range(self.height):
            for w in range(self.width):
                if (w, h) != self.grid[w][h].position:
                    return False
        return True
