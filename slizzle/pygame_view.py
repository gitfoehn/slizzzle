import pygame

from constants import CAPTION, ICON, MENU_RESOLUTION, Colors
from slizzle.model.slizzle_grid import SlizzleGrid
from slizzle.model.slizzle_tile import SlizzleTile


class View:
    def __init__(self):
        self.model = None
        self.display = None

        self.button_start = None
        self.button_difficulty = None
        self.button_image_path = None

        pygame.init()
        pygame.display.set_caption(CAPTION)
        icon = pygame.image.load(ICON)

        pygame.display.set_icon(icon)

    def show_menu_view(self, difficulty_text: str):
        self.display = pygame.display.set_mode(MENU_RESOLUTION)
        self.display.fill(Colors.CAMBRIDGE_BLUE)

        self.button_image_path = Button("LOAD IMAGE", Colors.PASTEL_YELLOW, (200, 350), 200, 40)
        self.button_start = Button("START", Colors.PASTEL_YELLOW, (200, 450), 100, 40)
        self.button_difficulty = Button(difficulty_text, Colors.PASTEL_YELLOW, (200, 400), 100, 40)

        self.button_start.draw(self.display)
        self.button_difficulty.draw(self.display)
        self.button_image_path.draw(self.display)

        pygame.display.flip()

    def init_game_view(self, resolution: (int, int)):
        self.display = pygame.display.set_mode(resolution)
        self.update_grid()

    def update_grid(self):
        self.display.fill(Colors.CAMBRIDGE_BLUE)

        grid = self.model.grid
        for x in range(len(grid.grid)):
            for y in range(len(grid.grid[x])):
                tile = grid.grid[x][y]
                if tile.is_visible:
                    self.draw_tile(tile, (x * tile.image.get_width(), y * tile.image.get_height()))
        pygame.display.flip()

    def draw_tile(self, tile: SlizzleTile, pos: (int, int)):
        image = tile.image

        self.display.blit(image, pos)

    def show_grid(self, grid: SlizzleGrid):
        pass


class Button:
    """
    Helper Class to Build Buttons.
    -
    """

    def __init__(self, label: str, color: (int, int, int), pos: (int, int), width: int, height: int):
        self.label = label
        self.color = color
        self.pos = pos
        self.x = pos[0]
        self.y = pos[1]
        self.width = width
        self.height = height
        self.rect = pygame.Rect(self.x, self.y, width, height)

    def draw(self, surface: pygame.Surface):
        label_elem = pygame.font.Font(None, 36).render(self.label, True, Colors.BLACK)

        pygame.draw.rect(surface, Colors.PASTEL_YELLOW, self.rect)
        surface.blit(label_elem, (self.rect.x + self.rect.width // 2 - label_elem.get_rect().width // 2,
                                  self.rect.y + self.rect.height // 2 - label_elem.get_rect().height // 2))
