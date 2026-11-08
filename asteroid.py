import random
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS, LINE_WIDTH
from logger import log_event
import pygame



class Asteroid (CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position,self.radius, LINE_WIDTH)

    def update(self, dt: float) -> None:
        self.position = self.position + (self.velocity * dt)

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            log_event("asteroid_split")
            self.velocity.rotate(random.uniform(20,50))
            new_radius = self.radius - ASTEROID_MIN_RADIUS

            asteroid = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid.velocity = self.velocity * 1.2


            asteroid = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid.velocity = self.velocity.rotate(random.uniform(-20,-50)) * 1.2
