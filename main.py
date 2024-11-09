# import statements
import pygame
from constants import *


def game_loop(screen):
    while True:
        # check if quit
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill((0, 0, 0))
    pygame.display.flip()


def main():
    pygame.init()

    # create gui window
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # start game
    game_loop(screen)


if __name__ == "__main__":
    main()
