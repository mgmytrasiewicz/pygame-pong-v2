import pygame
from config import WIDTH, HEIGHT
from core.game import Game

# Main function to run the game
def main():

    # Initialize Pygame
    pygame.init()

    # Configuration parameters
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("The Pong Game")

    game = Game(screen)

    # Main loop to keep the window open
    running = True
    while running:
        e = pygame.event.poll()
        if e.type == pygame.QUIT:
            running = False
        
        game.update()
        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()