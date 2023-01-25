import pygame

from constants import CAPTION, ICON, MENU_RESOLUTION, GAME_NAME, MENU_BACKGROUND_COLOR, GAME_BACKGROUND_COLOR,\
    BUTTON_COLOR, WIN_BANNER_COLOR, FONT_COLOR
from helper import convert_to_pygame_surface
from slizzle.model.slizzle_tile import SlizzleTile


class View:
    """
    SlizzleView is the view of the Slizzle application according to the MVC pattern.

    The View handles the rendering of the application to the screen.
    """
    def __init__(self):
        """
        Creates a new View without a model. This has to be set before calling the game view.
        """
        self.model = None
        self.display = None

        self.button_start = None
        self.button_difficulty = None
        self.button_image_path = None
        self.button_to_menu = None

        pygame.init()
        pygame.display.set_caption(CAPTION)
        icon = pygame.image.load(ICON)

        pygame.display.set_icon(icon)

    def init_menu_view(self):
        """
        Initializes the menu window
        """
        self.display = pygame.display.set_mode(MENU_RESOLUTION)

    def show_menu_view(self, difficulty_text: str, default_image):
        """
        Render the menu view to the menu window
        """
        self.display.fill(MENU_BACKGROUND_COLOR)

        # Add buttons
        self.button_image_path = Button("LOAD IMAGE", BUTTON_COLOR, (150, 350), 200, 40)
        self.button_start = Button("START", BUTTON_COLOR, (200, 450), 100, 40)
        self.button_difficulty = Button(difficulty_text, BUTTON_COLOR, (200, 400), 100, 40)

        # Draw buttons
        self.button_start.draw(self.display)
        self.button_difficulty.draw(self.display)
        self.button_image_path.draw(self.display)

        # Place logo
        logo = pygame.image.load(GAME_NAME)
        screen_width, screen_height = pygame.display.get_surface().get_size()
        logo_x = screen_width // 2 - logo.get_width() // 2
        logo_y = 30
        self.display.blit(logo, (logo_x, logo_y))

        # Show preview of selected image
        preview = default_image.copy()
        preview.thumbnail((200, 200))
        pic = convert_to_pygame_surface(preview)
        self.display.blit(pic, (250 - pic.get_rect().width // 2, logo_y + logo.get_rect().height + 20))

        # Update the screen
        pygame.display.flip()

    def init_game_view(self, resolution: (int, int)) -> None:
        """
        Initialize the game window
        """
        self.display = pygame.display.set_mode(resolution)
        self.update_grid()

    def update_grid(self) -> None:
        """
        Redraw the grid of the puzzle.
        """
        self.display.fill(GAME_BACKGROUND_COLOR)

        grid = self.model.grid
        for x in range(len(grid.grid)):
            for y in range(len(grid.grid[x])):
                tile = grid.grid[x][y]
                if tile.is_visible:
                    self.draw_tile(tile, (x * tile.image.get_width(), y * tile.image.get_height()))
        pygame.display.flip()

    def draw_tile(self, tile: SlizzleTile, pos: (int, int)):
        """
        Draws a single tile to the puzzle grid
        """
        image = tile.get_image()

        self.display.blit(image, pos)

    def show_end_screen(self, window_dimensions: (int, int)) -> None:
        """
        Display the end screen on top of the game view
        """
        window_x, window_y = window_dimensions

        # Draw banner
        label_text = f"You made it in {self.model.moves} move(s)."
        label_banner = pygame.font.Font(None, 36).render(label_text, True, FONT_COLOR)

        banner_width = label_banner.get_rect().width + 20
        banner_height = label_banner.get_rect().height + 20

        banner_x = window_x // 2 - banner_width // 2
        banner_y = window_y // 2 - banner_height // 2

        banner = pygame.Rect(banner_x, banner_y, banner_width, banner_height)
        pygame.draw.rect(self.display, WIN_BANNER_COLOR, banner)

        # Draw win text
        x_label = banner_x + banner_width // 2 - label_banner.get_rect().width // 2
        y_label = banner_y + banner_height // 2 - label_banner.get_rect().height // 2

        self.display.blit(label_banner, (x_label, y_label))

        # Draw back to menu button
        button_width = 200
        button_height = 40

        x_button = window_x // 2 - button_width // 2
        y_button = banner_y + banner_height + 10

        button_text = f"BACK TO MENU"
        self.button_to_menu = Button(button_text, WIN_BANNER_COLOR, (x_button, y_button), button_width, button_height)
        self.button_to_menu.draw(self.display)

        # Update the screen
        pygame.display.flip()


class Button:
    """
    Helper class to build buttons.
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
        """
        Draws the button to the surface.
        """
        label_elem = pygame.font.Font(None, 36).render(self.label, True, FONT_COLOR)

        pygame.draw.rect(surface, BUTTON_COLOR, self.rect)
        surface.blit(label_elem, (self.rect.x + self.rect.width // 2 - label_elem.get_rect().width // 2,
                                  self.rect.y + self.rect.height // 2 - label_elem.get_rect().height // 2))
