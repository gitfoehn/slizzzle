from slizzle.model.slizzle_model import Difficulty


class Colors:
    """
    Source of some Colors: https://colorpalettes.io/cyberpunk-synthwave-color-palette/
    """
    CAMBRIDGE_BLUE = (195, 218, 195)  # Background Color
    PASTEL_YELLOW = (250, 250, 153)  # Button Colors
    PHOENIX_BLUE = (189, 226, 238)
    BLACK = (0, 0, 0)
    POOL_BLUE = (0, 188, 225)
    PINK_BYTE = (233, 60, 172)
    SAPPHIRE_SPLENDOUR = (30, 34, 170)
    SHADOWN_PLANET = (32, 21, 71)
    MIDNIGHT_DREAMS = (5, 28, 44)


# Window Properties
CAPTION = "Slizzle"
WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720
RESOLUTION = (WINDOW_WIDTH, WINDOW_HEIGHT)
LOGO = 'assets/logo/slizzle_logo_small.png'
ICON = 'assets/logo/slizzle_icon.png'
SCHRIFTZUG = 'assets/logo/schriftzug.png'
DEFAULT_PICTURE = 'assets/loewe.jpg'

# Game Window Properties
GAME_VIEW_RATIO = 0.7
GAME_VIEW_RESOLUTION = [i * GAME_VIEW_RATIO for i in RESOLUTION]

# Game Properties
TILE_AMOUNT_HORIZONTAL = 3
TILE_AMOUNT_VERTICAL = 3

MENU_RESOLUTION = (500, 500)

# Other
DIFFICULTIES = (Difficulty("EASY", 3, 3, 15),
                Difficulty("MEDIUM", 4, 4, 40),
                Difficulty("HARD", 5, 5, 100),
                Difficulty("INSANE", 8, 8, 400))

SCALE_FACTOR = 0.95
MAX_WIDTH = WINDOW_WIDTH
MAX_HEIGHT = WINDOW_HEIGHT

BOARDER_SIZE = 3

# Colors
MENU_BACKGROUND_COLOR = Colors.SHADOWN_PLANET
BACKGROUND_COLOR = Colors.CAMBRIDGE_BLUE
BUTTON_COLOR = Colors.PINK_BYTE
SECONDARY_BUTTON_COLOR = Colors.POOL_BLUE
FONT_COLOR = Colors.MIDNIGHT_DREAMS
