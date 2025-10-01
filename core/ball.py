import pygame
import config


# Ball class definition
class Ball:
    """
    Represents the ball in the Pong game.

    Handles movement, collision detection with walls and paddle,
    and plays sound effects for events like rebound and miss.
    """

    def __init__(self, x, y, vx, vy, surface):
        # Initialize ball properties
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.surface = surface
        self.moving = False # Ball starts stationary
        self.last_hit = None  # Track last paddle that hit the ball

        self.sound_paddle = pygame.mixer.Sound(config.SOUND_PADDLE)
        self.sound_wall = pygame.mixer.Sound(config.SOUND_WALL)
        self.sound_miss = pygame.mixer.Sound(config.SOUND_MISS)

    def draw(self, color: tuple) -> None:
        # Draw the ball as a circle
        pygame.draw.circle(self.surface, color, (self.x, self.y), config.BALL_RADIUS)

    @property
    # Get the rectangular area of the ball for collision detection
    def rect(self):
        return pygame.Rect(self.x - config.BALL_RADIUS, self.y - config.BALL_RADIUS, config.BALL_RADIUS * 2, config.BALL_RADIUS * 2)

    def reset(self, paddle) -> None:
        # Reset ball to front of paddle and stop movement.
        self.moving = False
        self.last_hit = paddle
        self.y = paddle.y + config.PADDLE_HEIGHT // 2
        if paddle.x < config.SCREEN_WIDTH // 2:
            self.x = paddle.x + config.PADDLE_WIDTH + config.BALL_RADIUS + config.BALL_OFFSET
        else:
            self.x = paddle.x - config.BALL_RADIUS - config.BALL_OFFSET

    def update(self, left_paddle, right_paddle) -> str | None:
        """
        Update the ball's position based on current velocity.

        Args:
            left_paddle (Paddle): The left human's paddle for collision detection.
            right_paddle (Paddle): The right AI's paddle for collision detection.

        Returns:
            str: "BOUNCE" if it hits the paddle, "MISS" if it goes out of bounds,
                None otherwise.
        """
        
        # Only move if in motion
        if not self.moving:
            # Stick to the front of the paddle
            self.reset(self.last_hit)
            return
        
        
        # Calculate new position
        newx = self.x + self.vx
        newy = self.y + self.vy

        # Construct future rect for accurate collision detection
        future_rect = pygame.Rect(
            newx - config.BALL_RADIUS,
            newy - config.BALL_RADIUS,
            config.BALL_RADIUS * 2,
            config.BALL_RADIUS * 2
        )

        for paddle in [left_paddle, right_paddle]:
            if future_rect.colliderect(paddle.rect):
                # Determine side of collision
                dx = min(abs(future_rect.right - paddle.rect.left), abs(future_rect.left - paddle.rect.right))
                dy = min(abs(future_rect.bottom - paddle.rect.top), abs(future_rect.top - paddle.rect.bottom))

                if dx < dy:
                    self.vx = -self.vx  # Horizontal bounce (side of paddle)
                else:
                    self.vy = -self.vy  # Vertical bounce (top/bottom of paddle)

                self.last_hit = paddle
                self.sound_paddle.play()
                return "BOUNCE"

        # Check for collisions with the walls
        if newy - config.BALL_RADIUS < config.BORDER or newy + config.BALL_RADIUS > config.SCREEN_HEIGHT - config.BORDER:
            self.vy = -self.vy
            self.sound_wall.play()

        # Check if the ball has gone past the paddle (missed)
        if newx + config.BALL_RADIUS < 0:
            self.reset(left_paddle)
            self.sound_miss.play()
            return "LEFT_MISS"

        if newx - config.BALL_RADIUS > config.SCREEN_WIDTH:
            self.reset(right_paddle)
            self.sound_miss.play()
            return "RIGHT_MISS"
     
        self.x += self.vx
        self.y += self.vy