import pygame
import config
from core.game import Game

# Main function to run the game
def main():
    """
    Entry point for the Pong game.

    Initializes Pygame, sets up the display and clock, and runs the main game loop.
    Handles event polling, game state updates, rendering, and frame rate control.

    Raises:
        SystemExit: If the user quits the game window.
    """

    # Initialize Pygame
    pygame.init()

    # Configuration parameters
    screen = pygame.display.set_mode((config.SCREEN_WIDTH, config.SCREEN_HEIGHT))
    pygame.display.set_caption("The ML-Pong Game")
    clock = pygame.time.Clock()
    game = Game(screen)

    # Main loop to keep the window open
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            game.handle_event(event)
        
        game.update()
        game.render()
        pygame.display.flip()
        clock.tick(config.FPS)

    pygame.quit()

if __name__ == "__main__":
    main()