import pygame
from config import SCREEN_WIDTH, SCREEN_HEIGHT
from core.game import Game

# Main function to run the game
def main():

    # Initialize Pygame
    pygame.init()

    # Configuration parameters
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("The Pong Game")

    game = Game(screen)

    # Main loop to keep the window open
    running = True
    while running:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                running = False

            # Start the ball movement on mouse click
            if e.type == pygame.MOUSEBUTTONDOWN:
                game.ball.moving = True
        
        game.update()
        game.render()
        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()