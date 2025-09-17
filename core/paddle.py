import pygame
from config import WHITE, BLACK, BORDER, SCREEN_WIDTH, SCREEN_HEIGHT, PADDLE_HEIGHT, PADDLE_WIDTH

# Paddle class definition
class Paddle:

    def __init__(self, y, surface):
        self.x = SCREEN_WIDTH - PADDLE_WIDTH
        self.y = y
        self.surface = surface

    def draw(self, color):
        pygame.draw.rect(self.surface, color, (self.x, self.y, PADDLE_WIDTH, PADDLE_HEIGHT))

    def update(self):
        newy = pygame.mouse.get_pos()[1] - PADDLE_HEIGHT // 2

        if newy >= BORDER and newy + PADDLE_HEIGHT <= SCREEN_HEIGHT - BORDER:
            #self._draw(BLACK)  # Erase the paddle by drawing it in black
            self.y = pygame.mouse.get_pos()[1] - PADDLE_HEIGHT // 2
            #self._draw(WHITE)  # Draw the paddle in white