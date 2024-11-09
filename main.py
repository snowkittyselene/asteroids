# import statements
import pygame
from constants import *
from player import Player


def game_loop(screen):
    # prepare clock and ∆t
    clock = pygame.time.Clock()
    dt = 0

    # prepare player
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    while True:
        # check if quit
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill("black")
        player.draw(screen)
        pygame.display.flip()

        # go to next frame
        dt = clock.tick(60) / 1000


def main():
    pygame.init()

    # create gui window
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # start game
    game_loop(screen)


if __name__ == "__main__":
    main()
