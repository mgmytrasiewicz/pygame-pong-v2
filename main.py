import pygame

# Initialize Pygame
pygame.init()

# Set up display
BORDER = 10
WIDTH, HEIGHT = 800, 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
screen.fill(pygame.Color("black"))

pygame.display.set_caption("The Pong Game")

pygame.draw.rect(screen, pygame.Color("white"),\
                 pygame.Rect(0, 0, WIDTH, BORDER))  # Top border
pygame.draw.rect(screen, pygame.Color("white"),\
                    pygame.Rect(0, HEIGHT - BORDER, WIDTH, BORDER))  # Bottom border
pygame.draw.rect(screen, pygame.Color("white"),\
                    pygame.Rect(0, 0, BORDER, HEIGHT))  # Left border

pygame.display.flip()
while True:
    e = pygame.event.poll()
    if e.type == pygame.QUIT:
        break

pygame.quit()