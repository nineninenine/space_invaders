

class Settings():
	"""class to store settings in space invaders"""

	def __init__(self):
		"""init settins in space invaders"""
		#screen settings
		self.screen_width = 1200
		self.screen_height = 800
		self.bg_color = (230, 230, 230)

		#ship settings
		self.ship_speed_factor = 1.5