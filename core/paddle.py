import pygame
import config

# Paddle class definition
class Paddle:
    """
    Represents the player's paddle. Follows the vertical position of the mouse,
    and prevents movement beyond screen borders.
    """

    def __init__(self, y, surface):
        # Initialize paddle properties
        self.x = config.SCREEN_WIDTH - config.PADDLE_WIDTH
        self.y = y
        self.surface = surface

    @property
    # Get the rectangular area of the paddle for collision detection
    def rect(self):
        return pygame.Rect(self.x, self.y, config.PADDLE_WIDTH, config.PADDLE_HEIGHT)

    def draw(self, color):
        # Draw the paddle as a rectangle
        pygame.draw.rect(self.surface, color, (self.x, self.y, config.PADDLE_WIDTH, config.PADDLE_HEIGHT))

    def update(self):
        # Update paddle position based on mouse Y position
        mouse_y = pygame.mouse.get_pos()[1]
        newy = mouse_y - config.PADDLE_HEIGHT // 2

        if newy >= config.BORDER and newy + config.PADDLE_HEIGHT <= config.SCREEN_HEIGHT - config.BORDER:
            self.y = newy