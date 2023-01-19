import sys
from tkinter import filedialog as fd

import pygame
from PIL import Image

import constants
from constants import SCALE_FACTOR, MAX_WIDTH, MAX_HEIGHT
from pil_to_pygame_image import convert_to_pygame_surface
from slizzle.model.slizzle_model import SlizzleModel
from slizzle.model.slizzle_tile import SlizzleTile
from slizzle.pygame_view import View


class SlizzleController:
    def __init__(self):
        self.image = None
        self.model = None
        self.view = View()

        self.inMenu = True
        self.selected_diff = 0
        # TODO: Get puzzle_resolution rom settings
        self.puzzle_resolution = constants.DIFFICULTIES[self.selected_diff].res

    def load_image(self, image_url: str) -> None:
        self.image = Image.open(image_url)

    def check_resize(self) -> None:
        width, height = self.image.size
        while width > MAX_WIDTH or height > MAX_HEIGHT:
            width, height = width * SCALE_FACTOR, height * SCALE_FACTOR
        self.image = self.image.resize((int(width), int(height)), Image.ANTIALIAS)

    def crop_image(self) -> None:
        width, height = self.image.size
        print(f"width: {width} height: {height}")

        if width > MAX_WIDTH or height > MAX_HEIGHT:
            self.check_resize()
            width, height = self.image.size

        width -= (width % self.puzzle_resolution[0])
        height -= (height % self.puzzle_resolution[1])
        print(f"width: {width} height: {height}")
        self.image = self.image.crop((0, 0, width, height))

    def slice_image(self, tile_amount: (int, int)) -> list:
        self.crop_image()
        img_width, img_height = self.image.size

        # Calculate Tile dimensions
        tile_width = img_width / tile_amount[0]
        tile_height = img_height / tile_amount[1]
        tiles = []

        for w in range(tile_amount[0]):
            for h in range(tile_amount[1]):
                pil_img = self.image.crop(
                    (w * tile_width, h * tile_height, (w + 1) * tile_width, (h + 1) * tile_height))
                img = convert_to_pygame_surface(pil_img)
                tile = SlizzleTile(img, (w, h))
                tiles.append(tile)

        return tiles

    def load_image_path(self) -> None:
        impage_path = fd.askopenfilename(
            initialdir="/",
            title="Choose picture",
            filetypes=[('Image files', ('*.jpg', '*.png'))])
        if impage_path:
            self.image = impage_path
            self.load_image(self.image)
            print(f'Added image Path {self.image}')

    def open_menu(self) -> None:
        self.view.init_menu_view()
        while self.inMenu:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    if self.view.button_start.rect.collidepoint(event.pos):
                        print('Start button clicked')
                        if self.image is None:
                            self.load_image(constants.LOGO)
                        self.inMenu = False
                    if self.view.button_difficulty.rect.collidepoint(event.pos):
                        print('Change difficulty')
                        self.selected_diff = (self.selected_diff + 1) % len(constants.DIFFICULTIES)
                    if self.view.button_image_path.rect.collidepoint(event.pos):
                        self.load_image_path()

            self.view.show_menu_view(constants.DIFFICULTIES[self.selected_diff].name)

    def start_game(self) -> None:
        self.puzzle_resolution = constants.DIFFICULTIES[self.selected_diff].res
        tiles = self.slice_image(self.puzzle_resolution)
        self.model = SlizzleModel(tiles, constants.DIFFICULTIES[self.selected_diff])
        self.view.model = self.model

        self.model.start_game()
        self.view.init_game_view(self.image.size)
        self.game_loop()

    def game_loop(self):
        while True:
            self.event_handler()
            self.view.update_grid()

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
        tile_size = tuple(
            (puzzle_view_size[0] / self.puzzle_resolution[0], puzzle_view_size[1] / self.puzzle_resolution[1]))
        # pos.x % tile.w
        x = int(pos[0] // tile_size[0])
        y = int(pos[1] // tile_size[1])

        return tuple((x, y))
