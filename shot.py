import pygame
from circleshape import CircleShape
from constants import *

class Shot(CircleShape):
    def __init__(self, x, y, shot_radius):
        super().__init__(x, y, shot_radius)
        self.shot_radius = shot_radius
    
    def draw(self, screen):
        pygame.draw.circle(screen, "white", (self.position.x,self.position.y), self.shot_radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt