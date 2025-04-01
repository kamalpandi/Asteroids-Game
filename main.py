# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
import os

from player import Player

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
    player = Player(x, y, color, width)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        pygame.Surface.fill(screen, (0, 0, 0))
        player.update(dt)
        player.draw(screen)
        pygame.display.flip()
        dt = fps.tick(60)


if __name__ == "__main__":
    main()
