from PIL import Image
import pygame
from pygame import Surface


def convert_to_pygame_surface(image: Image) -> Surface:
    mode = image.mode
    size = image.size
    data = image.tobytes()

    pygame_image = pygame.image.fromstring(data, size, mode)
    return pygame_image
