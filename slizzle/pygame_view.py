import sys
import pygame
from pygame.surface import Surface

from slizzle.model.slizzle_model import SlizzleModel
from slizzle.model.slizzle_tile import SlizzleTile
from slizzle.model.slizzle_grid import SlizzleGrid
from constants import RESOLUTION, CAPTION, CAMBRIDGE_BLUE, ICON


class View:
    def __init__(self, model: SlizzleModel):
        self.model = model
        self.game_view = pygame.display.set_mode(RESOLUTION)

        pygame.init()
        pygame.display.set_caption(CAPTION)
        icon = pygame.image.load(ICON)

        pygame.display.set_icon(icon)

    def show_game_view(self):
        self.game_view.fill(CAMBRIDGE_BLUE)

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            self.update_grid()

    def update_grid(self):
        grid = self.model.grid
        for x in range(len(grid.grid)):
            for y in range(len(grid.grid[x])):
                tile = grid.grid[x][y]
                self.draw_tile(tile, (x*tile.image.get_width() + x*3, y*tile.image.get_height() + y*3))
        pygame.display.flip()

    def draw_tile(self, tile: SlizzleTile, pos: (int, int)):
        image = tile.image
        tile = pygame.Rect(image.get_rect())

        self.game_view.blit(image, pos)

    def show_grid(self, grid: SlizzleGrid):
        pass
