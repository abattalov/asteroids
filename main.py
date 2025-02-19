import pygame
import sys
import constants as c
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    print("Starting asteroids!")

    screen = pygame.display.set_mode((c.SCREEN_WIDTH, c.SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    #create groups
    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updateable, drawable)
    Asteroid.containers = (updateable, drawable, asteroids)
    AsteroidField.containers = (updateable)
    Shot.containers = (updateable, drawable, shots)

    #create player and asteroid
    player = Player(c.SCREEN_WIDTH/2, c.SCREEN_HEIGHT/2, c.PLAYER_RAIDUS)
    # asteroid = Asteroid(c.SCREEN_WIDTH/2.5, c.SCREEN_HEIGHT/2.5, c.PLAYER_RAIDUS)
    asteroid_field = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        screen.fill((0,0,0))

        updateable.update(dt)
        for asteroid in asteroids:
            if asteroid.has_collided(player):
                print("Game over!")
                sys.exit()
            for shot in shots:
                if asteroid.has_collided(shot):
                    asteroid.split()
                    shot.kill()
    
        for entity in drawable:
            entity.draw(screen)

        pygame.display.flip()

        dt = clock.tick(60)/1000

if __name__ == "__main__":
    main()