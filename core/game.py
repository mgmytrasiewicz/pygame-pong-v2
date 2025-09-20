import pygame
import config
from core.ball import Ball
from core.paddle import Paddle

# Game class definition
class Game:
    """
    Main controller for the Pong game. Handles game states (welcome, playing),
    input events, object updates, rendering, score, and lives.
    """

    def __init__(self, surface):
        # Initialize game objects
        self.surface = surface
        self.ball = Ball(config.SCREEN_WIDTH - config.BALL_RADIUS - config.PADDLE_WIDTH, config.SCREEN_HEIGHT // 2, -config.BALL_SPEED_X, -config.BALL_SPEED_Y, surface)
        self.paddle = Paddle(config.SCREEN_HEIGHT // 2 - config.PADDLE_HEIGHT // 2, surface)
        self.font = pygame.font.SysFont(None, 36)
        self.state = "WELCOME"  # <- Start at welcome screen
        self.score = 0
        self.lives = 3
        self.sound_welcome = pygame.mixer.Sound("assets/sounds/start-game.wav")
        self.welcome_played = False

    def _draw_borders(self):
        # Draw the game borders
        pygame.draw.rect(self.surface, config.WHITE, pygame.Rect(0, 0, config.SCREEN_WIDTH, config.BORDER))  # Top border
        pygame.draw.rect(self.surface, config.WHITE, pygame.Rect(0, config.SCREEN_HEIGHT - config.BORDER, config.SCREEN_WIDTH, config.BORDER))  # Bottom border
        pygame.draw.rect(self.surface, config.WHITE, pygame.Rect(0, 0, config.BORDER, config.SCREEN_HEIGHT))  # Left border

    def update(self):
        # Update game objects
        if self.state == "WELCOME":
            return  # No updates in welcome state        
        self.paddle.update()
        # Capture ball return value (did bounce? or missed?)
        result = self.ball.update(self.paddle)

        if result == "BOUNCE":
            self.score += 1

        elif result == "MISS":
            self.lives -= 1
            if self.lives <= 0:
                self.state = "GAME_OVER"
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
        if self.state == "WELCOME":
            if not self.welcome_played:
                self.sound_welcome.play()
                self.welcome_played = True            
            self._render_welcome()
            return
        
        elif self.state == "GAME_OVER":
            self._render_game_over()
        
        elif self.state == "PLAYING":        
            # Game state rendering
            # Draw borders
            self._draw_borders()
            # Draw paddle and ball
            self.paddle.draw(config.WHITE)
            self.ball.draw(config.WHITE)
            self._render_hud()

        if not self.ball.moving and self.state != "GAME_OVER":
            text = self.font.render("Click to Start", True, config.WHITE)
            rect = text.get_rect(center=(config.SCREEN_WIDTH//2, config.SCREEN_HEIGHT//2))
            self.surface.blit(text, rect)

    def handle_event(self, event):
        # Handle input events
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.state == "WELCOME":
                self.state = "PLAYING"
                self.ball.moving = True
            elif self.state == "PLAYING":
                self.ball.moving = True
            elif self.state == "GAME_OVER":
                self.reset_game()
                self.state = "WELCOME"        

    def _render_welcome(self):
        # Render the welcome screen
        # Larger font for the title
        title_font = pygame.font.SysFont('Arial', 64, bold=True)
        # Smaller font for instructions
        instruction_font = pygame.font.SysFont('Comic Sans MS', 32, italic=True)

        title = title_font.render("The Pong Game!", True, config.WHITE)
        instruction = instruction_font.render("Click to Start", True, config.WHITE)

        title_rect = title.get_rect(center=(config.SCREEN_WIDTH//2, config.SCREEN_HEIGHT//2 - 30))
        instruction_rect = instruction.get_rect(center=(config.SCREEN_WIDTH//2, config.SCREEN_HEIGHT//2 + 30))

        self.surface.blit(title, title_rect)
        self.surface.blit(instruction, instruction_rect)

    def _render_game_over(self):
        # Render the game over screen
        game_over_text = self.font.render("Game Over", True, config.WHITE)
        score_text = self.font.render(f"Final Score: {self.score}", True, config.WHITE)
        restart_text = self.font.render("Click to Restart", True, config.WHITE)

        game_over_rect = game_over_text.get_rect(center=(config.SCREEN_WIDTH // 2, config.SCREEN_HEIGHT // 2 - 40))
        score_rect = score_text.get_rect(center=(config.SCREEN_WIDTH // 2, config.SCREEN_HEIGHT // 2))
        restart_rect = restart_text.get_rect(center=(config.SCREEN_WIDTH // 2, config.SCREEN_HEIGHT // 2 + 40))

        self.surface.blit(game_over_text, game_over_rect)
        self.surface.blit(score_text, score_rect)
        self.surface.blit(restart_text, restart_rect)

    def _render_hud(self):
        # Render the heads-up display (score and lives)
        score_text = self.font.render(f"Score: {self.score}", True, config.WHITE)
        lives_text = self.font.render(f"Lives: {self.lives}", True, config.WHITE)

        self.surface.blit(score_text, (config.BORDER + 10, config.BORDER + 10))
        self.surface.blit(lives_text, (config.SCREEN_WIDTH - lives_text.get_width() - config.BORDER - 10, config.BORDER + 10))