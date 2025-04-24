import sys
import pygame
import os

from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from circleshape import CircleShape

os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "1"
from constants import SCREEN_HEIGHT, SCREEN_WIDTH


def main():
    pygame.init()

    fps = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    color = (225, 225, 225)
    width = 2

    # Shared groups
    updatables = pygame.sprite.Group()
    drawables = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    # Set containers
    Player.containers = (updatables, drawables)
    Asteroid.containers = (asteroids, updatables, drawables)
    AsteroidField.containers = (updatables,)

    # Create player
    player = Player(x, y, color, width)

    # Create asteroid field
    asteroid_field = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill((0, 0, 0))

        for drawable in drawables:
            drawable.draw(screen)

        # Update all updatables
        updatables.update(dt)
        for asteroid in asteroids:
            if player.check_for_collisions(asteroid):
                print("Game over!")
                pygame.quit()
                sys.exit()
        # Draw all drawables

        pygame.display.flip()
        dt = fps.tick(60)


if __name__ == "__main__":
    main()
