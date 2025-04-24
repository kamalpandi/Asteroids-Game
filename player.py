import pygame
from circleshape import CircleShape
from constants import PLAYER_RADIUS, PLAYER_SPEED, PLAYER_TURN_SPEED


class Player(CircleShape):
    containers = ()

    def __init__(self, x, y, color, width):
        pygame.sprite.Sprite.__init__(self, self.containers)  # add to groups
        CircleShape.__init__(self, x, y, PLAYER_RADIUS)
        self.color = color
        self.width = width
        self.rotation = 0
        super().__init__(x, y, PLAYER_RADIUS)

    def triangle(self) -> list:
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        points = self.triangle()
        pygame.draw.polygon(screen, points=points, color=self.color, width=self.width)

    def update(self, dt):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.move(PLAYER_SPEED * dt)

        if keys[pygame.K_a]:
            self.rotate(-PLAYER_TURN_SPEED * dt)

        if keys[pygame.K_s]:
            self.move(-PLAYER_SPEED * dt)

        if keys[pygame.K_d]:
            self.rotate(PLAYER_TURN_SPEED * dt)

    def rotate(self, angle_change):
        self.rotation += angle_change

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt
