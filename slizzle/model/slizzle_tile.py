class SlizzleTile:
	def __init__(self, model, image, image_border, position: (int, int)):
		self.model = model
		self.image = image
		self.image_border = image_border
		self.position = position
		self.is_visible = True

	def toggle_visibility(self) -> None:
		self.is_visible = not self.is_visible

	def get_image(self):
		if not self.model.is_running:
			return self.image
		return self.image_border
