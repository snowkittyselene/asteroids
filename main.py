# import statements
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot


def game_loop(screen):
    # prepare clock and ∆t
    clock = pygame.time.Clock()
    dt = 0
    paused = False

    # prepare sprite groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    Shot.containers = (shots, updatable, drawable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroidfield = AsteroidField()

    # create
    while True:
        # check if quit
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    paused = not paused
                if event.key == pygame.K_ESCAPE:
                    return

        if not paused:
            # update things
            for sprite in updatable:
                sprite.update(dt)

            # check for collision
            for asteroid in asteroids:
                # check player collision
                if asteroid.check_collision(player):
                    print("Game over!")
                    exit()

                # check bullet collision
                for shot in shots:
                    if shot.check_collision(asteroid):
                        shot.kill()
                        asteroid.kill()

            # draw things
            screen.fill("black")
            for sprite in drawable:
                sprite.draw(screen)

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
