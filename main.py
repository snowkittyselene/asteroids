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

        # draw the screen
        screen.fill("black")

        # draw the player
        player.draw(screen)
        player.update(dt)

        # render then go to next frame
        pygame.display.flip()
        dt = clock.tick(60) / 1000


def main():
    pygame.init()

    # create gui window
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Asteroids!")

    # start game
    game_loop(screen)


if __name__ == "__main__":
    main()
