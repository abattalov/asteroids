import pygame
import constants as c
from player import Player

def main():
    print("Starting asteroids!")
    print(f"Screen width: {c.SCREEN_WIDTH}")
    print(f"Screen height: {c.SCREEN_HEIGHT}")

    screen = pygame.display.set_mode((c.SCREEN_WIDTH, c.SCREEN_HEIGHT))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        screen.fill((0,0,0))
        player = Player(c.SCREEN_WIDTH/2, c.SCREEN_HEIGHT/2, c.PLAYER_RAIDUS)
        player.draw(screen)





        pygame.display.flip()

if __name__ == "__main__":
    main()