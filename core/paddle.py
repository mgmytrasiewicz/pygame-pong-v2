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

    def __init__(self, x: int, is_ai: bool, surface: pygame.Surface, ball) -> None:
        # Initialize paddle properties
        self.x = x
        self.y = config.SCREEN_HEIGHT // 2 - config.PADDLE_HEIGHT // 2
        self.is_ai = is_ai
        self.surface = surface
        self.ball = ball  # <--- store the instance
        self._rect = pygame.Rect(self.x, self.y, config.PADDLE_WIDTH, config.PADDLE_HEIGHT)

        if self.is_ai:
            # Load trained model
            self.model = joblib.load('./model/ml_model.pkl')
            self.scaler = joblib.load('./model/scaler.pkl')

    @property
    # Get the rectangular area of the paddle for collision detection
    def rect(self):
        self._rect.y = int(self.y)
        return self._rect

    def draw(self, color: tuple) -> None:
        # Draw the paddle as a rectangle
        pygame.draw.rect(self.surface, color, self.rect)

    def update(self) -> None:
        if not self.is_ai:
            # Follow mouse Y position
            mouse_y = pygame.mouse.get_pos()[1]
            self.y = mouse_y - config.PADDLE_HEIGHT // 2

            # Clamp within bounds
            self.y = max(config.BORDER, min(self.y, config.SCREEN_HEIGHT - config.PADDLE_HEIGHT - config.BORDER))
        else:
            # Update paddle position based on mouse Y position
            features = np.array([[self.ball.x, self.ball.y, self.ball.vx, self.ball.vy]])
            features_scaled = self.scaler.transform(features)
            predicted_y = self.model.predict(features_scaled)[0]

            self.y = (predicted_y - self.y) * 0.1 + self.y  # Smooth movement

            # Clamp within bounds
            self.y = max(config.BORDER, min(self.y, config.SCREEN_HEIGHT - config.PADDLE_HEIGHT - config.BORDER))