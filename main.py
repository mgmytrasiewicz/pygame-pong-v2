import pygame
import config
from core.game import Game

# Main function to run the game
def main():
    """
    Initialize and run the Pong game loop.

    This function sets up the Pygame environment, creates the game window,
    initializes the Game object, and runs the main game loop. It handles event
    processing, updating game state, rendering frames, and managing frame rate.

    The loop continues until the user quits the game window.

    Raises:
        SystemExit: When the user closes the game window.

    Example:
        >>> main()  # Starts the Pong game
    """

    # Initialize Pygame
    pygame.init()

    # Configuration parameters
    screen = pygame.display.set_mode((config.SCREEN_WIDTH, config.SCREEN_HEIGHT))
    pygame.display.set_caption("The Pong Game")
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