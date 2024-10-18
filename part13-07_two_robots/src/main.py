import pygame

pygame.init()

window = pygame.display.set_mode((640, 480))
robot = pygame.image.load(r"C:\Users\lrnoc\AppData\Local\tmc\vscode\mooc-programming-24\part13-01_four_robots\src\robot.png")

robot1_x = 0
robot2_x = 0
robot1_velocity = 1
robot2_velocity = 2
clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    window.fill((0, 0, 0))

    robot1_x += robot1_velocity
    robot2_x += robot2_velocity

    if robot1_velocity > 0 and robot1_x + robot.get_width() >= 640:
        robot1_velocity = -robot1_velocity
    if robot1_velocity < 0 and robot1_x <= 0:
        robot1_velocity = -robot1_velocity

    if robot2_velocity > 0 and robot2_x + robot.get_width() >= 640:
        robot2_velocity = -robot2_velocity
    if robot2_velocity < 0 and robot2_x <= 0:
        robot2_velocity = -robot2_velocity

    window.blit(robot, (robot1_x, 100))
    window.blit(robot, (robot2_x, 300))
    pygame.display.flip()

    clock.tick(60)
