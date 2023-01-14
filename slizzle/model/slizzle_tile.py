class SlizzleTile:
    def __init__(self, image, position: (int, int), is_visible: bool):
        self.image = image
        self.position = position
        self.is_visible = is_visible

    def toggle_visibility(self) -> None:
        self.is_visible = not self.is_visible
