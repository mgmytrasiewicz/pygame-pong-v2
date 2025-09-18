import pygame
from config import BALL_RADIUS, BALL_OFFSET, SCREEN_WIDTH, SCREEN_HEIGHT, BORDER, PADDLE_HEIGHT
from core import paddle

# Ball class definition
class Ball:

    def __init__(self, x, y, vx, vy, surface):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.surface = surface
        self.moving = False # Ball starts stationary

    def draw(self, color):
        pygame.draw.circle(self.surface, color, (self.x, self.y), BALL_RADIUS)

    @property
    def rect(self):
        return pygame.Rect(self.x - BALL_RADIUS, self.y - BALL_RADIUS, BALL_RADIUS * 2, BALL_RADIUS * 2)
    
    def reset(self, paddle):
        # Reset ball to front of paddle and stop movement.
        self.moving = False
        self.y = paddle.y + PADDLE_HEIGHT // 2
        self.x = paddle.x - BALL_RADIUS - BALL_OFFSET

    def update(self, paddle):
        if not self.moving:
            # Stick to the front of the paddle
            self.reset(paddle)
            return
        
        if self.x > SCREEN_WIDTH:
            self.reset(paddle)
            return

        newx = self.x + self.vx
        newy = self.y + self.vy

        # Check for collisions with the walls
        if newx - BALL_RADIUS < BORDER:
            self.vx = -self.vx
        elif newy - BALL_RADIUS < BORDER or newy + BALL_RADIUS > SCREEN_HEIGHT - BORDER:
            self.vy = -self.vy
        elif self.rect.colliderect(paddle.rect):
            self.vx = -self.vx  # Bounce off the paddle
     
        self.x += self.vx
        self.y += self.vy
