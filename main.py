import pygame
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from logger import log_state
from player import Player


def main():
    pygame.init()
    clock_obj = pygame.time.Clock()
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    player_obj = Player(x, y)
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    state = True

    while state:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                state = False
                return

        pygame.Surface.fill(screen, color=(0, 0, 0))
        player_obj.draw(screen=screen)
        dt = clock_obj.tick(60) / 1000
        player_obj.update(dt)
        pygame.display.flip()

    VERSION = pygame.version.ver
    print("Starting Asteroids with pygame version:", VERSION)
    print("Screen width:", SCREEN_WIDTH, "\n", "Screen height:", SCREEN_HEIGHT)


if __name__ == "__main__":
    main()
