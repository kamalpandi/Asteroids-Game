import pygame
from circleshape import CircleShape
from constants import SHOT_RADIUS


class Shot(CircleShape):
    def __init__(self, x, y, radius):
        self.shot_radius = SHOT_RADIUS
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(
            screen,
            (200, 200, 200),
            (int(self.position.x), int(self.position.y)),
            int(self.radius),  # Pass the radius as a separate argument
            2,
        )

    def update(self, dt):
        self.position += self.velocity * (dt / 1000.0)
        pass
