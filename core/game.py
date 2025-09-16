import pygame
from config import WIDTH, HEIGHT, BORDER, VELOCITY, BALL_RADIUS
from core.ball import Ball

# Game class definition
class Game:

    def __init__(self, surface):
        self.surface = surface
        self._draw_borders()
        self.ball = Ball(WIDTH - BALL_RADIUS, HEIGHT // 2, -VELOCITY, 0, surface)

    def _draw_borders(self):
        pygame.draw.rect(self.surface, pygame.Color("white"),\
                        pygame.Rect(0, 0, WIDTH, BORDER))  # Top border
        pygame.draw.rect(self.surface, pygame.Color("white"),\
                        pygame.Rect(0, HEIGHT - BORDER, WIDTH, BORDER))  # Bottom border
        pygame.draw.rect(self.surface, pygame.Color("white"),\
                        pygame.Rect(0, 0, BORDER, HEIGHT))  # Left border
        
    def update(self):
        self.ball.update()

    def render(self):
        pass