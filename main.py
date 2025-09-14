import pygame

# Initialize Pygame
pygame.init()

# Set up display
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("The Pong Game")

while True:
    e = pygame.event.poll()
    if e.type == pygame.QUIT:
        break

quit
                           