import pygame

pygame.init()

window = pygame.display.set_mode((640, 480))
robot = pygame.image.load(r"C:\Users\lrnoc\AppData\Local\tmc\vscode\mooc-programming-24\part13-10_robot_invasion\src\robot.png")

player1_x = 320
player1_y = 240
player2_x = 100
player2_y = 100
velocity = 5
clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    # Player 1 (Arrow keys)
    if keys[pygame.K_LEFT] and player1_x > 0:
        player1_x -= velocity
    if keys[pygame.K_RIGHT] and player1_x < 640 - robot.get_width():
        player1_x += velocity
    if keys[pygame.K_UP] and player1_y > 0:
        player1_y -= velocity
    if keys[pygame.K_DOWN] and player1_y < 480 - robot.get_height():
        player1_y += velocity

    # Player 2 (WASD keys)
    if keys[pygame.K_a] and player2_x > 0:
        player2_x -= velocity
    if keys[pygame.K_d] and player2_x < 640 - robot.get_width():
        player2_x += velocity
    if keys[pygame.K_w] and player2_y > 0:
        player2_y -= velocity
    if keys[pygame.K_s] and player2_y < 480 - robot.get_height():
        player2_y += velocity

    window.fill((0, 0, 0))
    window.blit(robot, (player1_x, player1_y))
    window.blit(robot, (player2_x, player2_y))
    pygame.display.flip()

    clock.tick(60)

pygame.quit()
