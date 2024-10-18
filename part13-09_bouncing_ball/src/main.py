import pygame

pygame.init()

window_width = 640
window_height = 480
window = pygame.display.set_mode((window_width, window_height))
ball = pygame.image.load(r"C:\Users\lrnoc\AppData\Local\tmc\vscode\mooc-programming-24\part13-09_bouncing_ball\src\ball.png")

ball_x, ball_y = 100, 100
ball_velocity_x, ball_velocity_y = 3, 3
clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    ball_x += ball_velocity_x
    ball_y += ball_velocity_y

    if ball_x <= 0 or ball_x >= window_width - ball.get_width():
        ball_velocity_x *= -1
    if ball_y <= 0 or ball_y >= window_height - ball.get_height():
        ball_velocity_y *= -1

    window.fill((0, 0, 0))
    window.blit(ball, (ball_x, ball_y))
    pygame.display.flip()

    clock.tick(60)

pygame.quit()
