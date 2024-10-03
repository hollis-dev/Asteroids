# the following line allows us to use code from the open-source pygame library throughout this file
import sys
import pygame
from asteroid import Asteroid
from asteroidfield import AsteroidField
from constants import *
from player import Player
from shot import Shot

def main():
	pygame.init()
	clock = pygame.time.Clock()
	dt = 0

	updatable = pygame.sprite.Group()
	drawable = pygame.sprite.Group()
	asteroids = pygame.sprite.Group()
	shots = pygame.sprite.Group()

	AsteroidField.containers = (updatable)
	Asteroid.containers = (asteroids, updatable, drawable)
	Shot.containers = (shots, updatable, drawable)
	Player.containers = (updatable, drawable)

	x = SCREEN_WIDTH / 2
	y = SCREEN_HEIGHT / 2

	asteroid = AsteroidField()
	player1 = Player(x, y)

	print("Starting asteroids!")
	print(f"Screen width: {SCREEN_WIDTH}")
	print(f"Screen width: {SCREEN_HEIGHT}")

	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return

		for item in updatable:
			item.update(dt)

		for asteroid in asteroids:
			if player1.collision_check(asteroid):
				print("Game over!")
				pygame.quit()
				sys.exit()

		for asteroid in asteroids:
			for shot in shots:
				if shot.collision_check(asteroid):
					shot.kill()
					asteroid.split()	

		screen.fill((0, 0, 0))

		for item in drawable:
			item.draw(screen)

		pygame.display.flip()
		clock.tick(60)

		milliseconds_to_seconds = 1000
		dt = clock.tick(60) / milliseconds_to_seconds

		

if __name__ == "__main__":
	main()
