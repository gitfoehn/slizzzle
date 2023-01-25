from slizzle.model.slizzle_model import Difficulty

# Colors
"""
Source of some Colors: https://colorpalettes.io/cyberpunk-synthwave-color-palette/
"""
CAMBRIDGE_BLUE = (195, 218, 195)
BLACK = (0, 0, 0)
POOL_BLUE = (0, 188, 225)
PINK_BYTE = (233, 60, 172)
SHADOWN_PLANET = (32, 21, 71)
MIDNIGHT_DREAMS = (5, 28, 44)

# assets
LOGO = 'assets/logo/slizzzle_logo_small.png'
ICON = 'assets/logo/slizzzle_icon.png'
GAME_NAME = "assets/logo/schriftzug.png"
DEFAULT_PICTURE = "assets/loewe.jpg"

# window properties
CAPTION = "Slizzzle"
MENU_RESOLUTION = (500, 500)

# game properties
DIFFICULTIES = (Difficulty("EASY", 3, 3, 10),
                Difficulty("MEDIUM", 4, 4, 40),
                Difficulty("HARD", 5, 5, 100),
                Difficulty("INSANE", 8, 8, 400))

# resize properties
SCALE_FACTOR = 0.95
MAX_WIDTH = 1280
MAX_HEIGHT = 720

# grid properties
BOARDER_SIZE = 3

# theme
MENU_BACKGROUND_COLOR = SHADOWN_PLANET
GAME_BACKGROUND_COLOR = BLACK
BUTTON_COLOR = PINK_BYTE
SECONDARY_BUTTON_COLOR = POOL_BLUE
FONT_COLOR = MIDNIGHT_DREAMS
GRID_COLOR = BLACK

