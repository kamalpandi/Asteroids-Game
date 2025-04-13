import pygame
from circleshape import CircleShape


class Asteroid:
    containers = ()
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        pass

    def draw(self, screen):
        pygame.draw.circle(
            screen,
            (200, 200, 200),
            ((int(self.position.x), int(self.position.y)), self.radius, 2),
        )

    def update(self, dt):
        self.position += self.velocity * (dt / 1000.0)
        pass
