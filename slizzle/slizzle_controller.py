import sys
from tkinter import filedialog as fd

import pygame
from PIL import Image

from constants import MAX_WIDTH, MAX_HEIGHT, MIN_WIDTH, MIN_HEIGHT, DEFAULT_PICTURE, DIFFICULTIES
from helper import convert_to_pygame_surface, add_border_to_tile
from slizzle.model.slizzle_model import SlizzleModel
from slizzle.model.slizzle_tile import SlizzleTile
from slizzle.pygame_view import View


class SlizzleController:
	"""
	SlizzleController is the Controller of the Slizzle Application according to the MVC Pattern

	The Controller handles the Events that occur during Runtime
	It also handles the flow of the Application
	"""

	def __init__(self):
		"""
		Creates a new Controller with a default Image and a base View
		"""
		self.image = Image.open(DEFAULT_PICTURE)
		self.model = None
		self.view = View()

		self.inMenu = True
		self.running = False
		self.selected_diff = 0
		self.puzzle_resolution = DIFFICULTIES[self.selected_diff].res

	def start(self) -> None:
		"""
		Starts the Controller and checks in which state the application is in and executes the specific code for this
		state. States being like inMenu or inGame or endGame
		"""
		while True:
			if self.inMenu and not self.running:		# inMenu
				self.open_menu()
			elif not self.inMenu and self.running:		# inGame
				self.start_game()
			elif not self.inMenu and not self.running:	# endGame
				self.end_game()

	def open_menu(self) -> None:
		"""
		This function handles the menu screen when the Application is in the state 'inMenu'.
		It calls the view to show the menu screen and contains event listeners for button presses
		"""
		self.view.init_menu_view()
		while self.inMenu:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					sys.exit()
				if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
					if self.view.button_start.rect.collidepoint(event.pos):
						print('Start button clicked')
						if self.image is None:
							self.load_image(DEFAULT_PICTURE)
						self.inMenu = False
						self.running = True
					if self.view.button_difficulty.rect.collidepoint(event.pos):
						print('Change difficulty')
						self.selected_diff = (self.selected_diff + 1) % len(DIFFICULTIES)
					if self.view.button_image_path.rect.collidepoint(event.pos):
						self.select_image()
			self.view.show_menu_view(DIFFICULTIES[self.selected_diff].name, self.image)

	def start_game(self) -> None:
		"""
		This function handles the initialization of the game when the state of the Application changes to 'inGame'.
		It creates the SlizzleModel which handles the game logic and tells the view to initialize the game screen.
		Starts the game loop after the initialization.
		"""
		self.puzzle_resolution = DIFFICULTIES[self.selected_diff].res
		self.model = SlizzleModel(None, DIFFICULTIES[self.selected_diff])
		tiles = self.slice_image(self.puzzle_resolution)
		self.model.tiles = tiles
		self.view.model = self.model

		self.model.start_game()
		self.view.init_game_view(self.image.size)
		self.game_loop()

	def end_game(self) -> None:
		"""
		This function handles the end screen when the Application is in the state 'endGame'.
		It calls the view to show the end screen and contains event listeners for button presses
		"""
		while not self.inMenu and not self.running:
			self.view.show_end_screen(self.image.size)
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					sys.exit()
				if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
					if self.view.button_to_menu.rect.collidepoint(event.pos):
						self.running = False
						self.inMenu = True

	def game_loop(self):
		"""
		The gameloop calls the event handler and tells the view to update
		Keeps track of the model.is_running state to set the state of the controller to 'endGame'
		"""
		while self.model.is_running:
			self.event_handler()
			self.view.update_grid()
		self.running = False

	def event_handler(self):
		"""
		Handles the events that happen during the game e.g. like clicking on a puzzle tile
		"""
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

	def select_image(self) -> None:
		image_path = fd.askopenfilename(
			initialdir="/",
			title="Choose picture",
			filetypes=[('Image files', ('*.jpg', '*.png'))])
		if image_path:
			self.load_image(image_path)
			print(f'Added image Path {image_path}')

	def load_image(self, image_url: str) -> None:
		self.image = Image.open(image_url)

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
