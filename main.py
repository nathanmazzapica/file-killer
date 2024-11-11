from config import SAFE_MODE
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
radius = 200
angle = 0
files = os.listdir("files")
for i in range(len(files)):
	angle += (2 * math.pi) / len(files)

	pos_x = game_center.x + radius * math.cos(angle)
	pos_y = game_center.y + radius * math.sin(angle)

	testEnemy = Enemy(files[i], 15, pos_x, pos_y, 20)
	testEnemy.draw(screen)
	enemies.append(testEnemy)

while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

	background = pygame.Surface(screen.get_size())
	background = background.convert()

	color = (170,238,187)
	warning_text = "SAFE MODE ! FILES WILL NOT BE DELETED"

	if not SAFE_MODE:
		color = (170, 20, 20)
		warning_text = "DANGER MODE ! FILES WILL BE PERMANENTLY DELETED"

	background.fill(color)
	screen.blit(background, (0,0))

	for enemy in enemies:
		enemy.draw(screen)

		if enemy.check_collision(player):
			enemy.die(SAFE_MODE)


	for e in enemies:
		if not e.should_draw:
			enemies.remove(e)

	player.draw(screen)
	keys = pygame.key.get_pressed()

	font = pygame.font.Font(None, 64)
	text = font.render(warning_text, True, (10, 10, 10))
	text_pos = text.get_rect(x = 0, y = 640 )
	screen.blit(text, text_pos)

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
