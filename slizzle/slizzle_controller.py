import sys

import pygame
from PIL import Image

import constants
from slizzle.model.slizzle_model import SlizzleModel
from slizzle.model.slizzle_tile import SlizzleTile
from pil_to_pygame_image import convert_to_pygame_surface
from slizzle.pygame_view import View


class SlizzleController:
    def __init__(self):
        self.image = None
        self.model = None
        self.view = View()

        self.inMenu = True
        self.selected_diff = 0
        # TODO: Get puzzle_resolution rom settings
        self.puzzle_resolution = (3, 3)  # (width, height)

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

    def open_menu(self) -> None:
        while self.inMenu:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    if self.view.button_start.rect.collidepoint(event.pos):
                        print('Start button clicked')
                        self.inMenu = False
                        self.puzzle_resolution = constants.DIFFICULTIES[self.selected_diff].res

                    if self.view.button_difficulty.rect.collidepoint(event.pos):
                        print('Change difficulty')
                        self.selected_diff = (self.selected_diff + 1) % len(constants.DIFFICULTIES)

            self.view.show_menu_view(constants.DIFFICULTIES[self.selected_diff].name)

    def start_game(self) -> None:
        self.load_image('assets/logo/slizzle_logo_small.png')
        tiles = self.slice_image(self.puzzle_resolution)

        self.model = SlizzleModel(tiles, constants.DIFFICULTIES[self.selected_diff])
        self.view.model = self.model

        self.model.start_game()
        self.game_loop()

    def game_loop(self):
        while True:
            self.event_handler()
            self.view.show_game_view(self.image.size)

    def event_handler(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                pos = pygame.mouse.get_pos()
                cell = self.get_puzzle_coord_from_pos(pos)
                print(f'Left Mouse Button was clicked at location {pos} and grid cell {cell}')  # ToDo: Debug
                self.model.grid_swap(cell)

    def get_puzzle_coord_from_pos(self, pos: (int, int)) -> (int, int):
        puzzle_view_size = self.image.size
        # tile.w = view.w / puzzle_res.w
        tile_size = tuple((puzzle_view_size[0] / self.puzzle_resolution[0], puzzle_view_size[1] / self.puzzle_resolution[1]))
        # pos.x % tile.w
        x = int(pos[0] // tile_size[0])
        y = int(pos[1] // tile_size[1])

        return tuple((x, y))
