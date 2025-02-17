import pygame
import constants as c
from player import Player
from asteroid import Asteroid

def main():
    print("Starting asteroids!")

    screen = pygame.display.set_mode((c.SCREEN_WIDTH, c.SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = clock.tick(60)/1000

    #create groups
    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    Player.containers = (updateable, drawable)
    Asteroid.containers = (updateable, drawable)

    #create player
    player = Player(c.SCREEN_WIDTH/2, c.SCREEN_HEIGHT/2, c.PLAYER_RAIDUS)
    asteroid = Asteroid(c.SCREEN_WIDTH/2.5, c.SCREEN_HEIGHT/2.5, c.PLAYER_RAIDUS)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        screen.fill((0,0,0))

        for entity in updateable:
            entity.update(dt)
    
        for entity in drawable:
            entity.draw(screen)





        pygame.display.flip()

if __name__ == "__main__":
    main()