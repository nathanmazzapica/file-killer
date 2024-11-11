from circleshape import *
import pygame
from os import remove as remove_file_dangerous

class Enemy(CircleShape):

	def __init__(self, name, hp, x, y, radius):
		self.name = name
		self.hp = hp

		self.should_draw = True

		super().__init__(x, y, radius)

	def draw(self, screen):
		if not self.should_draw:
			return

		pygame.draw.circle(screen, (255,255,255), self.position, self.radius, 2)

		font = pygame.font.Font(None, 32)
		text = font.render(self.name, True, (10, 10, 10))
		textpos = text.get_rect(centerx=self.position.x, y=self.position.y - (self.radius + 40))

		screen.blit(text, textpos)

	def take_damage(self, dmg):
		self.hp -= dmg

		if self.hp <= 0:
			self.die()

	def die(self, safeMode=False):
		self.kill()
		self.should_draw = False

		if not safeMode:
			try:
				remove_file_dangerous(f"files/{self.name}")
			except:
				print("already dead")
