import pygame
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from logger import log_state

if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    VERSION = pygame.version.ver
    print("Starting Asteroids with pygame version:", VERSION)
    print("Screen width:", SCREEN_WIDTH, "\n", "Screen height:", SCREEN_HEIGHT)
