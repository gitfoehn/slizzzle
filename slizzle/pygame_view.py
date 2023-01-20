import pygame

from constants import CAPTION, ICON, MENU_RESOLUTION, Colors, SCHRIFTZUG
from pil_to_pygame_image import convert_to_pygame_surface
from slizzle.model.slizzle_tile import SlizzleTile

class View:
    def __init__(self):
        self.model = None
        self.display = None

        self.button_start = None
        self.button_difficulty = None
        self.button_image_path = None
        self.button_back_to_menu = None

        pygame.init()
        pygame.display.set_caption(CAPTION)
        icon = pygame.image.load(ICON)

        pygame.display.set_icon(icon)

    def init_menu_view(self):
        self.display = pygame.display.set_mode(MENU_RESOLUTION)

    def show_menu_view(self, difficulty_text: str, default_image):

        self.display.fill(Colors.SHADOWN_PLANET)

        self.button_image_path = Button("LOAD IMAGE", Colors.PINK_BYTE, (150, 350), 200, 40)
        self.button_start = Button("START", Colors.PINK_BYTE, (200, 450), 100, 40)
        self.button_difficulty = Button(difficulty_text, Colors.PINK_BYTE, (200, 400), 100, 40)

        self.button_start.draw(self.display)
        self.button_difficulty.draw(self.display)
        self.button_image_path.draw(self.display)

        logo = pygame.image.load(SCHRIFTZUG)
        screen_width, screen_height = pygame.display.get_surface().get_size()

        logo_x = screen_width // 2 - logo.get_width() // 2
        logo_y = 30

        self.display.blit(logo, (logo_x, logo_y))
        preview = default_image.copy()

        preview.thumbnail((200, 200))

        pic = convert_to_pygame_surface(preview)
        self.display.blit(pic, (250 - pic.get_rect().width // 2, logo_y + logo.get_rect().height + 20))

        pygame.display.flip()

    def init_game_view(self, resolution: (int, int)) -> None:
        self.display = pygame.display.set_mode(resolution)
        self.update_grid()

    def update_grid(self) -> None:
        self.display.fill(Colors.CAMBRIDGE_BLUE)

        grid = self.model.grid
        for x in range(len(grid.grid)):
            for y in range(len(grid.grid[x])):
                tile = grid.grid[x][y]
                if tile.is_visible:
                    self.draw_tile(tile, (x * tile.image.get_width(), y * tile.image.get_height()))
        pygame.display.flip()

    def draw_tile(self, tile: SlizzleTile, pos: (int, int)):
        # TODO ggf. blit image_boarder only when not all tiles are visible else blit image
        image = tile.get_image()

        self.display.blit(image, pos)

    def show_end_screen(self, window_dimensions: (int, int)) -> None:
        window_x, window_y = window_dimensions

        label_text = f"You made it in {self.model.moves} move(s)."
        label_banner = pygame.font.Font(None, 36).render(label_text, True, Colors.MIDNIGHT_DREAMS)

        banner_width = label_banner.get_rect().width + 20
        banner_height = label_banner.get_rect().height + 20

        banner_x = window_x // 2 - banner_width // 2
        banner_y = window_y // 2 - banner_height // 2

        banner = pygame.Rect(banner_x, banner_y, banner_width, banner_height)

        x_label = banner_x + banner_width // 2 - label_banner.get_rect().width // 2
        y_label = banner_y + banner_height // 2 - label_banner.get_rect().height // 2

        button_width = 200
        button_height = 40

        x_button = window_x // 2 - button_width // 2
        y_button = banner_y + banner_height + 10

        pygame.draw.rect(self.display, Colors.POOL_BLUE, banner)

        self.display.blit(label_banner, (x_label, y_label))
        button_text = f"BACK TO MENU"
        self.button_back_to_menu = Button(button_text, Colors.POOL_BLUE, (x_button, y_button), button_width, button_height)
        self.button_back_to_menu.draw(self.display)
        pygame.display.flip()


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

    def draw(self, surface: pygame.Surface) -> None:
        label_elem = pygame.font.Font(None, 36).render(self.label, True, Colors.MIDNIGHT_DREAMS)

        pygame.draw.rect(surface, Colors.PINK_BYTE, self.rect)
        surface.blit(label_elem, (self.rect.x + self.rect.width // 2 - label_elem.get_rect().width // 2,
                                  self.rect.y + self.rect.height // 2 - label_elem.get_rect().height // 2))



