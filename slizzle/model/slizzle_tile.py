class SlizzleTile:

	def __init__(self,image_border, image, position: (int, int)):
		self.image_border = image_border
		self.image = image
		self.position = position
		self.is_visible = True

	def toggle_visibility(self) -> None:
		self.is_visible = not self.is_visible
