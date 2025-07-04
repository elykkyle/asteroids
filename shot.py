import pygame
from circleshape import CircleShape
from constants import *

class Shot(CircleShape):
    def __init__(self, x, y, angle):
        super().__init__(x, y, 5)
        self.velocity = pygame.Vector2(0,1)
        self.velocity.rotate(angle)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, SHOT_RADIUS)

    def update(self, dt):
        self.position += (self.velocity * dt)
