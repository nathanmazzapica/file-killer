import math
from enemy import Enemy

import pygame
import os

pygame.init()
screen = pygame.display.set_mode((1280,720))
clock = pygame.time.Clock()
running = True
dt = 0

game_center = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

player = Enemy("player", 15, game_center.x, game_center.y, 20)

angle = 0
offset = 0

enemies = []
for file in os.listdir("files"):
	testEnemy = Enemy(file, 15, 300 + offset, 300 + offset * 3, 20)
	testEnemy.draw(screen)
	offset += 30
	enemies.append(testEnemy)

while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

	background = pygame.Surface(screen.get_size())
	background = background.convert()
	background.fill((170,238,187))
	screen.blit(background, (0,0))

	for enemy in enemies:
		enemy.draw(screen)

		if enemy.check_collision(player):
			enemy.die()


	for e in enemies:
		if not e.should_draw:
			enemies.remove(e)

	player.draw(screen)
	keys = pygame.key.get_pressed()


  # TODO: normalize this
	if keys[pygame.K_w]:
		player.position.y -= 300 * dt
	if keys[pygame.K_s]:
		player.position.y += 300 * dt
	if keys[pygame.K_a]:
		player.position.x -= 300 * dt
	if keys[pygame.K_d]:
		player.position.x += 300 * dt

	pygame.display.flip()

	dt = clock.tick(60) / 1000
	angle += 5 * dt


pygame.quit()
