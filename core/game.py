import pygame
import config
from core.ball import Ball
from core.paddle import Paddle
from enum import Enum, auto

class GameState(Enum):
    WELCOME = auto()
    PLAYING = auto()
    GAME_OVER = auto()

# Game class definition
class Game:
    """
    Main game controller for the Pong game.

    Manages game states, object updates (ball and paddle), rendering UI screens,
    user interaction, scoring, and game logic transitions.
    """

    def __init__(self, surface):
        # Initialize game objects
        self.surface = surface
        self.ball = Ball(config.SCREEN_WIDTH - config.BALL_RADIUS - config.PADDLE_WIDTH, config.SCREEN_HEIGHT // 2, -config.BALL_SPEED_X, -config.BALL_SPEED_Y, surface)
        self.paddle = Paddle(config.SCREEN_HEIGHT // 2 - config.PADDLE_HEIGHT // 2, surface)
        self.fonts = {
            "title": pygame.font.SysFont('Arial', 64, bold=True),
            "instruction": pygame.font.SysFont('Comic Sans MS', 32, italic=True),
            "default": pygame.font.SysFont(None, 36)
        }
        self.state = GameState.WELCOME  # <- Start at welcome screen
        self.score = 0
        self.lives = 3
        self.sound_welcome = pygame.mixer.Sound(config.SOUND_WELCOME)
        self.welcome_played = False

    def _draw_borders(self):
        # Draw the game borders
        pygame.draw.rect(self.surface, config.WHITE, pygame.Rect(0, 0, config.SCREEN_WIDTH, config.BORDER))  # Top border
        pygame.draw.rect(self.surface, config.WHITE, pygame.Rect(0, config.SCREEN_HEIGHT - config.BORDER, config.SCREEN_WIDTH, config.BORDER))  # Bottom border
        pygame.draw.rect(self.surface, config.WHITE, pygame.Rect(0, 0, config.BORDER, config.SCREEN_HEIGHT))  # Left border

    def update(self):
        """
        Update the game state and handle collisions.

        - Updates paddle position.
        - Moves the ball.
        - Detects bounces and misses.
        - Triggers game over if lives are exhausted.
        """
        
        # Update game objects
        if self.state == GameState.WELCOME:
            return  # No updates in welcome state        
        self.paddle.update()
        # Capture ball return value (did bounce? or missed?)
        result = self.ball.update(self.paddle)

        if result == "BOUNCE":
            self.score += 1

        elif result == "MISS":
            self.lives -= 1
            if self.lives <= 0:
                self.state = GameState.GAME_OVER
            else:
                self.ball.reset(self.paddle)


    def reset_game(self):
        # Reset game to initial state
        self.score = 0
        self.lives = 3
        self.ball.reset(self.paddle)

    def render(self):
        # Render the game objects and UI

        # Fill screen with black
        self.surface.fill(config.BLACK)

        # State-based rendering
        if self.state == GameState.WELCOME:
            if not self.welcome_played:
                self.sound_welcome.play()
                self.welcome_played = True            
            self._render_welcome()
            return

        if self.state == GameState.GAME_OVER:
            self._render_game_over()
            return

        # Playing state
        # Draw borders
        self._draw_borders()
        # Draw paddle and ball
        self.paddle.draw(config.WHITE)
        self.ball.draw(config.WHITE)
        self._render_hud()

        if not self.ball.moving:
            text = self.fonts["default"].render("Click to Start", True, config.WHITE)
            rect = text.get_rect(center=(config.SCREEN_WIDTH//2, config.SCREEN_HEIGHT//2))
            self.surface.blit(text, rect)

    def handle_event(self, event):
        """
        Handle user input events.

        - Mouse click starts the game or restarts after game over.
        """

        # Handle input events
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.state == GameState.WELCOME:
                self.state = GameState.PLAYING
                self.ball.moving = True
            elif self.state == GameState.PLAYING:
                self.ball.moving = True
            elif self.state == GameState.GAME_OVER:
                self.reset_game()
                self.state = GameState.WELCOME

    def _render_welcome(self):
        # Render the welcome screen
        title = self.fonts["title"].render("The Pong Game!", True, config.WHITE)
        instruction = self.fonts["instruction"].render("Click to Start", True, config.WHITE)

        title_rect = title.get_rect(center=(config.SCREEN_WIDTH//2, config.SCREEN_HEIGHT//2 - 30))
        instruction_rect = instruction.get_rect(center=(config.SCREEN_WIDTH//2, config.SCREEN_HEIGHT//2 + 30))

        self.surface.blit(title, title_rect)
        self.surface.blit(instruction, instruction_rect)

    def _render_game_over(self):
        # Render the game over screen
        game_over_text = self.fonts["default"].render("Game Over", True, config.WHITE)
        score_text = self.fonts["default"].render(f"Final Score: {self.score}", True, config.WHITE)
        restart_text = self.fonts["default"].render("Click to Restart", True, config.WHITE)

        game_over_rect = game_over_text.get_rect(center=(config.SCREEN_WIDTH // 2, config.SCREEN_HEIGHT // 2 - 40))
        score_rect = score_text.get_rect(center=(config.SCREEN_WIDTH // 2, config.SCREEN_HEIGHT // 2))
        restart_rect = restart_text.get_rect(center=(config.SCREEN_WIDTH // 2, config.SCREEN_HEIGHT // 2 + 40))

        self.surface.blit(game_over_text, game_over_rect)
        self.surface.blit(score_text, score_rect)
        self.surface.blit(restart_text, restart_rect)

    def _render_hud(self):
        # Render the heads-up display (score and lives)
        score_text = self.fonts["default"].render(f"Score: {self.score}", True, config.WHITE)
        lives_text = self.fonts["default"].render(f"Lives: {self.lives}", True, config.WHITE)

        self.surface.blit(score_text, (config.BORDER + 10, config.BORDER + 10))
        self.surface.blit(lives_text, (config.SCREEN_WIDTH - lives_text.get_width() - config.BORDER - 10, config.BORDER + 10))