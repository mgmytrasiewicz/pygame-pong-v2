import pygame
import config

# Paddle class definition
class Paddle:
    """
    Represents the player's paddle. Follows the vertical position of the mouse,
    and prevents movement beyond screen borders.
    """
    
    def __init__(self, y, surface):
        self.x = config.SCREEN_WIDTH - config.PADDLE_WIDTH
        self.y = y
        self.surface = surface

    @property
    def rect(self):
        return pygame.Rect(self.x, self.y, config.PADDLE_WIDTH, config.PADDLE_HEIGHT)

    def draw(self, color):
        pygame.draw.rect(self.surface, color, (self.x, self.y, config.PADDLE_WIDTH, config.PADDLE_HEIGHT))

    def update(self):
        mouse_y = pygame.mouse.get_pos()[1]
        newy = mouse_y - config.PADDLE_HEIGHT // 2

        if newy >= config.BORDER and newy + config.PADDLE_HEIGHT <= config.SCREEN_HEIGHT - config.BORDER:
            self.y = newy