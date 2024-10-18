import pygame

pygame.init()

window = pygame.display.set_mode((640, 480))
robot = pygame.image.load(r"C:\Users\lrnoc\AppData\Local\tmc\vscode\mooc-programming-24\part13-10_robot_invasion\src\robot.png")

robot_x = 320
robot_y = 240
velocity = 5
clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and robot_x > 0:
        robot_x -= velocity
    if keys[pygame.K_RIGHT] and robot_x < 640 - robot.get_width():
        robot_x += velocity
    if keys[pygame.K_UP] and robot_y > 0:
        robot_y -= velocity
    if keys[pygame.K_DOWN] and robot_y < 480 - robot.get_height():
        robot_y += velocity

    window.fill((0, 0, 0))
    window.blit(robot, (robot_x, robot_y))
    pygame.display.flip()

    clock.tick(60)

pygame.quit()
