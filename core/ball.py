import pygame
import config

# Ball class definition
class Ball:
    """
    Represents the ball in the Pong game.
    Manages position, movement, collision logic with paddle/walls,
    and plays corresponding sound effects.
    """

    def __init__(self, x, y, vx, vy, surface):
        # Initialize ball properties
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.surface = surface
        self.moving = False # Ball starts stationary

        self.sound_paddle = pygame.mixer.Sound("assets/sounds/rebound-paddle.wav")
        self.sound_wall = pygame.mixer.Sound("assets/sounds/rebound-wall.wav")
        self.sound_miss = pygame.mixer.Sound("assets/sounds/game-over.wav")

    def draw(self, color):
        # Draw the ball as a circle
        pygame.draw.circle(self.surface, color, (self.x, self.y), config.BALL_RADIUS)

    @property
    # Get the rectangular area of the ball for collision detection
    def rect(self):
        return pygame.Rect(self.x - config.BALL_RADIUS, self.y - config.BALL_RADIUS, config.BALL_RADIUS * 2, config.BALL_RADIUS * 2)

    def reset(self, paddle):
        # Reset ball to front of paddle and stop movement.
        self.moving = False
        self.y = paddle.y + config.PADDLE_HEIGHT // 2
        self.x = paddle.x - config.BALL_RADIUS - config.BALL_OFFSET

    def update(self, paddle):
        # Only move if in motion
        if not self.moving:
            # Stick to the front of the paddle
            self.reset(paddle)
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

        # Check for collision with the paddle
        if future_rect.colliderect(paddle.rect):
            self.vx = -self.vx  # Bounce off the paddle
            self.sound_paddle.play()
            return "BOUNCE"

        # Check for collisions with the walls
        elif newx - config.BALL_RADIUS < config.BORDER:
            self.vx = -self.vx
            self.sound_wall.play()
        elif newy - config.BALL_RADIUS < config.BORDER or newy + config.BALL_RADIUS > config.SCREEN_HEIGHT - config.BORDER:
            self.vy = -self.vy
            self.sound_wall.play()

        # Check if the ball has gone past the paddle (missed)
        elif self.x - config.BALL_RADIUS > config.SCREEN_WIDTH:
            self.reset(paddle)
            self.sound_miss.play()
            return "MISS"
     
        self.x += self.vx
        self.y += self.vy