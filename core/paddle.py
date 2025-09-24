import pygame
import config
import joblib
import numpy as np

# Paddle class definition
class Paddle:
    """
    Represents the player-controlled paddle.

    Follows the vertical position of the mouse while staying within screen bounds.
    """

    def __init__(self, y, surface, ball):
        # Initialize paddle properties
        self.x = config.SCREEN_WIDTH - config.PADDLE_WIDTH
        self.y = y
        self.surface = surface

        self.ball = ball  # <--- store the instance

        # Load trained model
        self.model = joblib.load('./model/ml_model.pkl')
        self.scaler = joblib.load('./model/scaler.pkl')

    @property
    # Get the rectangular area of the paddle for collision detection
    def rect(self):
        return pygame.Rect(self.x, self.y, config.PADDLE_WIDTH, config.PADDLE_HEIGHT)

    def draw(self, color):
        # Draw the paddle as a rectangle
        pygame.draw.rect(self.surface, color, (self.x, self.y, config.PADDLE_WIDTH, config.PADDLE_HEIGHT))

    def update(self):
        # Update paddle position based on mouse Y position
        features = np.array([[self.ball.x, self.ball.y, self.ball.vx, self.ball.vy]])
        features_scaled = self.scaler.transform(features)
        predicted_y = self.model.predict(features_scaled)[0]

        # Clamp within bounds
        predicted_y = max(config.BORDER, min(predicted_y, config.SCREEN_HEIGHT - config.PADDLE_HEIGHT - config.BORDER))

        self.y = predicted_y