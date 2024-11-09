import pygame
import random
from circleshape import CircleShape
from constants import *


class Asteroid(CircleShape):

    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        spawn_angle = random.uniform(20, 50)
        child_one_angle = self.velocity.rotate(spawn_angle)
        child_two_angle = self.velocity.rotate(-spawn_angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        child_one = Asteroid(self.position.x, self.position.y, new_radius)
        child_two = Asteroid(self.position.x, self.position.y, new_radius)

        child_one.velocity = child_one_angle * 1.2
        child_two.velocity = child_two_angle * 1.2
