class SlizzleTile:
	def __init__(self, image, image_border, position: (int, int)):
		self.image = image
		self.image_border = image_border
		self.position = position
		self.is_visible = True

	def toggle_visibility(self) -> None:
		self.is_visible = not self.is_visible
