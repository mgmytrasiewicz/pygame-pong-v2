import pygame

# Initialize Pygame
pygame.init()

# Configuration parameters
BORDER = 10
WIDTH, HEIGHT = 800, 600
VELOCITY = 4

# Ball class definition
class Ball:

    RADIUS = 10

    def __init__(self, x, y, vx, vy):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy

    def show(self, color):
        global screen
        pygame.draw.circle(screen, color, (self.x, self.y), self.RADIUS)

    def update(self):
        self.show(pygame.Color("black"))  # Erase the ball by drawing it in black
        self.x += self.vx
        self.y += self.vy
        self.show(pygame.Color("white"))  # Draw the ball in white

# Initialize the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
screen.fill(pygame.Color("black"))

# Set window title
pygame.display.set_caption("The Pong Game")

# Draw borders
pygame.draw.rect(screen, pygame.Color("white"),\
                pygame.Rect(0, 0, WIDTH, BORDER))  # Top border
pygame.draw.rect(screen, pygame.Color("white"),\
                pygame.Rect(0, HEIGHT - BORDER, WIDTH, BORDER))  # Bottom border
pygame.draw.rect(screen, pygame.Color("white"),\
                pygame.Rect(0, 0, BORDER, HEIGHT))  # Left border

# Draw the ball
ball = Ball(WIDTH-Ball.RADIUS, HEIGHT//2, -VELOCITY, 0)
ball.show(pygame.Color("white"))

# Update the display
pygame.display.flip()

# Main loop to keep the window open
while True:
    e = pygame.event.poll()
    if e.type == pygame.QUIT:
        break
    ball.update()
    pygame.display.flip()

pygame.quit()