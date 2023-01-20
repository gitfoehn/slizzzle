from slizzle.model.slizzle_model import Difficulty

# Window Properties
CAPTION = "Slizzle"
WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720
RESOLUTION = (WINDOW_WIDTH, WINDOW_HEIGHT)
LOGO = 'assets/logo/slizzle_logo_small.png'
ICON = 'assets/logo/slizzle_icon.png'

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

BOARDER_SIZE = 5


# Colors
class Colors:
    CAMBRIDGE_BLUE = (195, 218, 195)  # Background Color
    PASTEL_YELLOW = (250, 250, 153)  # Button Colors
    BLACK = (0, 0, 0)
