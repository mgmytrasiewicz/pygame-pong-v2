import pygame
from config import SCREEN_WIDTH, SCREEN_HEIGHT, BORDER, BALL_SPEED_X, BALL_SPEED_Y, BALL_RADIUS, PADDLE_WIDTH, PADDLE_HEIGHT, WHITE, BLACK
from core.ball import Ball
from core.paddle import Paddle

# Game class definition
class Game:

    def __init__(self, surface):
        self.surface = surface
        self._draw_borders()
        self.ball = Ball(SCREEN_WIDTH - BALL_RADIUS - PADDLE_WIDTH, SCREEN_HEIGHT // 2, -BALL_SPEED_X, -BALL_SPEED_Y, surface)
        self.paddle = Paddle(SCREEN_HEIGHT // 2 - PADDLE_HEIGHT // 2, surface)

    def _draw_borders(self):
        pygame.draw.rect(self.surface, pygame.Color("white"),\
                        pygame.Rect(0, 0, SCREEN_WIDTH, BORDER))  # Top border
        pygame.draw.rect(self.surface, pygame.Color("white"),\
                        pygame.Rect(0, SCREEN_HEIGHT - BORDER, SCREEN_WIDTH, BORDER))  # Bottom border
        pygame.draw.rect(self.surface, pygame.Color("white"),\
                        pygame.Rect(0, 0, BORDER, SCREEN_HEIGHT))  # Left border

    def update(self):
        self.ball.update(self.paddle)
        self.paddle.update()

    def render(self):
        # Fill screen with black
        self.surface.fill(BLACK)

        # Draw borders
        self._draw_borders()

        # Draw paddle and ball
        self.paddle.draw(WHITE)
        self.ball.draw(WHITE)