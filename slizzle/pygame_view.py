import sys
import pygame
from pygame.surface import Surface

from slizzle.model.slizzle_model import SlizzleModel
from slizzle.model.slizzle_tile import SlizzleTile
from slizzle.model.slizzle_grid import SlizzleGrid
from constants import RESOLUTION, GAME_VIEW_RESOLUTION, CAPTION, CAMBRIDGE_BLUE, ICON


class View:
    def __init__(self, model: SlizzleModel, resolution: (int, int)):
        self.model = model
        self.display = pygame.display.set_mode(resolution)

        pygame.init()
        pygame.display.set_caption(CAPTION)
        icon = pygame.image.load(ICON)

        pygame.display.set_icon(icon)

    def show_game_view(self):
        self.display.fill(CAMBRIDGE_BLUE)
        self.update_grid()

    def update_grid(self):
        grid = self.model.grid
        for x in range(len(grid.grid)):
            for y in range(len(grid.grid[x])):
                tile = grid.grid[x][y]
                if tile.is_visible:
                    self.draw_tile(tile, (x*tile.image.get_width(), y*tile.image.get_height()))
        pygame.display.flip()

    def draw_tile(self, tile: SlizzleTile, pos: (int, int)):
        image = tile.image
        tile = pygame.Rect(image.get_rect())

        self.display.blit(image, pos)

    def show_grid(self, grid: SlizzleGrid):
        pass
