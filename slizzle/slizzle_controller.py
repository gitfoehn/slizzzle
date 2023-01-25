import sys
from tkinter import filedialog as fd

import pygame
from PIL import Image

from constants import MAX_WIDTH, MAX_HEIGHT, MIN_WIDTH, MIN_HEIGHT, DEFAULT_PICTURE, DIFFICULTIES
from helper import convert_to_pygame_surface, add_border_to_tile
from slizzle.model.slizzle_model import SlizzleModel
from slizzle.model.slizzle_tile import SlizzleTile
from slizzle.pygame_view import View


def add_boarder_to_tile(img):
	tile_w, tile_h = img.size
	return ImageOps.expand(img, border=constants.BOARDER_SIZE, fill=GRID_COLOR).resize((tile_w, tile_h))


class SlizzleController:
	def __init__(self):
		self.image = Image.open(DEFAULT_PICTURE)
		self.model = None
		self.view = View()

		self.inMenu = True
		self.running = False
		self.selected_diff = 0
		self.puzzle_resolution = DIFFICULTIES[self.selected_diff].res

	def start(self) -> None:
		while True:
			if self.inMenu and not self.running:
				self.open_menu()
			elif not self.inMenu and self.running:
				self.start_game()
			elif not self.inMenu and not self.running:
				self.end_game()

	def load_image(self, image_url: str) -> None:
		self.image = Image.open(image_url)

	def resize_to_minmax(self) -> None:
		width, height = self.image.size

		if width / MAX_WIDTH > height / MAX_HEIGHT:
			# crop to max_width
			if width > MAX_WIDTH:
				factor = width / MAX_WIDTH
			else:
				factor = width / MIN_WIDTH
		else:
			# crop to max_height
			if height > MAX_HEIGHT:
				factor = height / MAX_HEIGHT
			else:
				factor = height / MIN_HEIGHT

		print(f"width: {width} height: {height}")
		width, height = int(width / factor), int(height / factor)
		print(f"width: {width} height: {height}")
		self.image = self.image.resize((width, height), Image.ANTIALIAS)

	def crop_image(self) -> None:
		width, height = self.image.size
		print(f"width: {width} height: {height}")

		if width > MAX_WIDTH or height > MAX_HEIGHT or width < MIN_WIDTH or height < MIN_HEIGHT:
			self.resize_to_minmax()
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

				# Creates bordered Version
				pil_img_bord = add_border_to_tile(pil_img)
				bord_img = convert_to_pygame_surface(pil_img_bord)

				img = convert_to_pygame_surface(pil_img)
				tile = SlizzleTile(self.model, img, bord_img, (w, h))
				tiles.append(tile)

		return tiles
