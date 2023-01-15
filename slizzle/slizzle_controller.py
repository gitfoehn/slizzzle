import sys

import pygame
from PIL import Image

from slizzle.model.slizzle_model import SlizzleModel
from slizzle.model.slizzle_tile import SlizzleTile
from pil_to_pygame_image import convert_to_pygame_surface
from slizzle.pygame_view import View


class SlizzleController:
    def __init__(self):
        self.image = None
        self.model = None
        self.view = None

        self.puzzle_resolution = (4, 3)  # (width, height)

    def load_image(self, image_url: str) -> None:
        self.image = Image.open(image_url)
        self.crop_image()

    def crop_image(self) -> None:
        width, height = self.image.size
        width -= (width % self.puzzle_resolution[0])
        height -= (height % self.puzzle_resolution[1])
        self.image = self.image.crop((0, 0, width, height))

    def slice_image(self, tile_amount: (int, int)) -> list:
        img_width, img_height = self.image.size

        # Calculate Tile dimensions
        tile_width = img_width / tile_amount[0]
        tile_height = img_height / tile_amount[1]
        tiles = []

        for w in range(tile_amount[0]):
            for h in range(tile_amount[1]):
                # TODO Crop to optimal size
                pil_img = self.image.crop((w * tile_width, h * tile_height, (w + 1) * tile_width, (h + 1) * tile_height))
                img = convert_to_pygame_surface(pil_img)
                tile = SlizzleTile(img, (w, h))
                tiles.append(tile)

        return tiles

    def start_game(self) -> None:
        self.load_image('assets/bregenzerwald.jpg')
        tiles = self.slice_image(self.puzzle_resolution)

        self.model = SlizzleModel(self.puzzle_resolution, tiles)
        self.view = View(self.model, self.image.size)

        self.model.start_game()
        self.game_loop()

    def game_loop(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    pos = pygame.mouse.get_pos()
                    cell = self.get_puzzle_coord_from_pos(pos)
                    print(f'Left Mouse Button was clicked at location {pos} and grid cell {cell}')
                    # For all Recs check if mouse pos during click is colliding with Rec
                    # try to move tile
                    self.model.grid_swap(cell)

            self.view.show_game_view()

    def get_puzzle_coord_from_pos(self, pos: (int, int)) -> (int, int):
        puzzle_view_size = self.image.size
        # tile.w = view.w / puzzle_res.w
        tile_size = tuple((puzzle_view_size[0] / self.puzzle_resolution[0], puzzle_view_size[1] / self.puzzle_resolution[1]))
        # pos.x % tile.w
        x = int(pos[0] // tile_size[0])
        y = int(pos[1] // tile_size[1])

        return tuple((x, y))

