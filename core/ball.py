import pygame
from config import BALL_RADIUS, WHITE, BLACK, SCREEN_WIDTH, SCREEN_HEIGHT, BORDER, PADDLE_WIDTH, PADDLE_HEIGHT

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

    def update(self, paddle):
        if not self.moving:
            # Stick to the front of the paddle
            self.y = paddle.y + PADDLE_HEIGHT // 2
            self.x = paddle.x - BALL_RADIUS - 1  # Just in front of paddle
            return
        
        newx = self.x + self.vx
        newy = self.y + self.vy

        # Check for collisions with the walls
        if newx - BALL_RADIUS < BORDER:
            self.vx = -self.vx
        elif newy - BALL_RADIUS < BORDER or newy + BALL_RADIUS > SCREEN_HEIGHT - BORDER:
            self.vy = -self.vy
        elif newx + BALL_RADIUS >= SCREEN_WIDTH + PADDLE_WIDTH \
            and abs(newy - paddle.y) <= PADDLE_HEIGHT // 2:
            self.vx = -self.vx  # Bounce off the paddle
     
        #self._draw(BLACK)  # Erase the ball by drawing it in black
        self.x += self.vx
        self.y += self.vy
        #self._draw(WHITE)  # Draw the ball in white