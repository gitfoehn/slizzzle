from PIL import Image, ImageOps
import pygame
from pygame import Surface

import constants


def convert_to_pygame_surface(image: Image) -> Surface:
    """
    Helper function for converting a Pillow Image to a Pygame Image
    """
    mode = image.mode
    size = image.size
    data = image.tobytes()

    pygame_image = pygame.image.fromstring(data, size, mode)
    return pygame_image


def add_border_to_tile(img) -> Image:
    """
    Helper function for adding a border to an image_tile
    """
    tile_w, tile_h = img.size
    return ImageOps.expand(img, border=constants.BORDER_SIZE, fill=constants.GRID_COLOR).resize((tile_w, tile_h))
