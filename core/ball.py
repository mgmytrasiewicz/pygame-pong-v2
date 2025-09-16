import pygame
from config import BALL_RADIUS, WHITE, BLACK, HEIGHT, BORDER

# Ball class definition
class Ball:

    def __init__(self, x, y, vx, vy, surface):
        
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.surface = surface

    def _draw(self, color):
        
        pygame.draw.circle(self.surface, color, (self.x, self.y), BALL_RADIUS)

    def update(self):
        
        newx = self.x + self.vx
        newy = self.y + self.vy

        # Check for collisions with the walls
        if newx - BALL_RADIUS < BORDER:
            self.vx = -self.vx
        if newy - BALL_RADIUS < BORDER or newy + BALL_RADIUS > HEIGHT - BORDER:
            self.vy = -self.vy

        self._draw(BLACK)  # Erase the ball by drawing it in black
        self.x += self.vx
        self.y += self.vy
        self._draw(WHITE)  # Draw the ball in white