import pygame
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from logger import log_state


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    state = True
    while state:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        pygame.Surface.fill(screen, color=(0, 0, 0))
        pygame.display.flip()
    VERSION = pygame.version.ver
    print("Starting Asteroids with pygame version:", VERSION)
    print("Screen width:", SCREEN_WIDTH, "\n", "Screen height:", SCREEN_HEIGHT)


if __name__ == "__main__":
    main()
