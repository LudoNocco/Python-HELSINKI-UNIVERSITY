import pygame
import random

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

WHITE = (255, 255, 255)

robot_img = pygame.image.load(r'C:\Users\lrnoc\AppData\Local\tmc\vscode\mooc-programming-24\part13-17_asteroids\src\robot.png')
asteroid_img = pygame.image.load(r'C:\Users\lrnoc\AppData\Local\tmc\vscode\mooc-programming-24\part13-17_asteroids\src\rock.png')

robot_width = robot_img.get_width()
robot_height = robot_img.get_height()
robot_x = SCREEN_WIDTH // 2 - robot_width // 2
robot_y = SCREEN_HEIGHT - robot_height - 10
robot_speed = 5

asteroid_width = asteroid_img.get_width()
asteroid_height = asteroid_img.get_height()
asteroid_speed = 5
asteroid_x = random.randint(0, SCREEN_WIDTH - asteroid_width)
asteroid_y = 0 - asteroid_height

score = 0
game_over = False

font = pygame.font.Font(None, 36)

clock = pygame.time.Clock()

running = True
while running:
    screen.fill(WHITE)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and robot_x > 0:
        robot_x -= robot_speed
    if keys[pygame.K_RIGHT] and robot_x < SCREEN_WIDTH - robot_width:
        robot_x += robot_speed

    asteroid_y += asteroid_speed

    if asteroid_y + asteroid_height >= robot_y and asteroid_x + asteroid_width > robot_x and asteroid_x < robot_x + robot_width:
        score += 1
        asteroid_x = random.randint(0, SCREEN_WIDTH - asteroid_width)
        asteroid_y = 0 - asteroid_height
        asteroid_speed += 0.5

    if asteroid_y > SCREEN_HEIGHT:
        game_over = True

    screen.blit(robot_img, (robot_x, robot_y))
    screen.blit(asteroid_img, (asteroid_x, asteroid_y))

    score_text = font.render(f"Score: {score}", True, (0, 0, 0))
    screen.blit(score_text, (10, 10))

    if game_over:
        game_over_text = font.render("Game Over", True, (0, 0, 0))
        screen.blit(game_over_text, (SCREEN_WIDTH // 2 - 80, SCREEN_HEIGHT // 2))
        pygame.display.flip()
        pygame.time.wait(2000)
        running = False

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
