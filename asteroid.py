
import pygame
from circleshape import CircleShape

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.x = x
        self.y = y

    def draw(self, screen):
        pygame.draw.circle(screen, "white", (self.x,self.y), self.radius, 2)

    def update(self, something):
        pass

    # def move(self, dt):
    #     forward = pygame.Vector2(0, 1).rotate(self.rotation)
    #     self.position += forward * PLAYER_SPEED * dt