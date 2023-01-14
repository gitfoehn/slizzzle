from PIL import Image

from slizzle.model.slizzle_model import SlizzleModel
from slizzle.model.slizzle_tile import SlizzleTile
from pil_to_pygame_image import convert_to_pygame_surface
from slizzle.pygame_view import View


class SlizzleController:
    def __init__(self):
        self.image = None
        self.model = None
        self.view = None

    def load_image(self, image_url: str) -> None:
        self.image = Image.open(image_url)

    def slice_image(self, tile_amount_horizontal: int, tile_amount_vertical: int) -> list:
        img_width, img_height = self.image.size

        # Calculate Tile dimensions
        tile_width = img_width / tile_amount_horizontal
        tile_height = img_height / tile_amount_vertical
        tiles = []

        for w in range(tile_amount_horizontal):
            for h in range(tile_amount_vertical):
                # TODO Crop to optimal size
                pil_img = self.image.crop((w * tile_width, h * tile_height, (w + 1) * tile_width, (h + 1) * tile_height))
                img = convert_to_pygame_surface(pil_img)
                tile = SlizzleTile(img, (w, h), True)
                tiles.append(tile)

        return tiles

    def start_game(self) -> None:
        self.load_image('assets/bregenzerwald.jpg')
        tiles = self.slice_image(3, 3)

        self.model = SlizzleModel(3, 3, tiles)
        self.view = View(self.model)

        self.view.show_game_view()
