import random
import pygame
from constants import ASTEROID_MIN_RADIUS, LINE_WIDTH
from circleshape import CircleShape
from logger import log_event


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(
            screen,
            color="white",
            width=LINE_WIDTH,
            radius=self.radius,
            center=(self.position),
        )

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        log_event("asteroid_split")
        random_angle = random.uniform(20, 50)

        new_radius = self.radius - ASTEROID_MIN_RADIUS

        asteroid_movement_1 = self.velocity.rotate(random_angle)
        asteroid_1 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid_1.velocity = asteroid_movement_1 * 1.2

        asteroid_movement_2 = self.velocity.rotate(-random_angle)
        asteroid_2 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid_2.velocity = asteroid_movement_2 * 1.2
