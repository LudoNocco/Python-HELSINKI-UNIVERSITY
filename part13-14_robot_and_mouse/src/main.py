import pygame

pygame.init()

window_width, window_height = 640, 480
window = pygame.display.set_mode((window_width, window_height))
robot = pygame.image.load(r"C:\Users\lrnoc\AppData\Local\tmc\vscode\mooc-programming-24\part13-10_robot_invasion\src\robot.png")

clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    mouse_x, mouse_y = pygame.mouse.get_pos()

    robot_x = mouse_x - robot.get_width() // 2
    robot_y = mouse_y - robot.get_height() // 2

    # Ensure the robot stays within the window's boundaries
    if robot_x < 0:
        robot_x = 0
    if robot_x > window_width - robot.get_width():
        robot_x = window_width - robot.get_width()

    if robot_y < 0:
        robot_y = 0
    if robot_y > window_height - robot.get_height():
        robot_y = window_height - robot.get_height()

    window.fill((0, 0, 0))
    window.blit(robot, (robot_x, robot_y))
    pygame.display.flip()

    clock.tick(60)

pygame.quit()
