import pygame
from constants import SHOT_RADIUS, LINE_WIDTH
from circleshape import CircleShape


class Shot(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(
            screen,
            color="white",
            width=LINE_WIDTH,
            radius=SHOT_RADIUS,
            center=(self.position),
        )

    def collides_with(self, other):
        return super().collides_with(other)

    def update(self, dt):
        self.position += self.velocity * dt
