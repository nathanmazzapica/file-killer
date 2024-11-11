import pygame

class CircleShape(pygame.sprite.Sprite):
	def __init__(self, x, y, radius):

		super().__init__()

		self.position = pygame.Vector2(x, y)
		self.velocity = pygame.Vector2(0, 0)
		self.radius = radius


	def draw(self, screen):
		pass


	def update(self, dt):
		pass


	def check_collision(self, other):
		dist = self.position.distance_to(other.position)

		if dist <= self.radius + other.radius:
			return True
		else:
			return False
