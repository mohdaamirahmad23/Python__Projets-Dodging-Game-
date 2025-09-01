import pygame
import random
import sys

# Initialize pygame
pygame.init()

# Screen dimensions
WIDTH = 600
HEIGHT = 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dodge the Ball Game")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Clock
clock = pygame.time.Clock()

# Player setup
player_size = 50
player_x = WIDTH // 2
player_y = HEIGHT - player_size - 10
player_speed = 7

# Ball setup
ball_size = 30
ball_speed = 5
balls = [
    [random.randint(0, WIDTH - ball_size), random.randint(-150, -30)]
    for _ in range(3)
]

# Font
font = pygame.font.SysFont("Arial", 25)

# Score
score = 0

# Game loop
running = True
while running:
    screen.fill(BLACK)

    # Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Key press
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < WIDTH - player_size:
        player_x += player_speed

    # Draw player
    pygame.draw.rect(screen, BLUE, (player_x, player_y, player_size, player_size))

    # Move and draw balls
    for ball in balls:
        ball[1] += ball_speed
        if ball[1] > HEIGHT:
            ball[0] = random.randint(0, WIDTH - ball_size)
            ball[1] = random.randint(-150, -30)
            score += 1

        pygame.draw.circle(screen, RED, (ball[0], ball[1]), ball_size)

        # Collision detection
        if (
            player_x < ball[0] < player_x + player_size
            and player_y < ball[1] < player_y + player_size
        ):
            running = False

    # Draw score
    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))

    pygame.display.flip()
    clock.tick(30)

pygame.quit()
sys.exit()
