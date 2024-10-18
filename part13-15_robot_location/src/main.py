import pygame
import random

pygame.init()

window = pygame.display.set_mode((640, 480))
robot = pygame.image.load(r"C:\Users\lrnoc\AppData\Local\tmc\vscode\mooc-programming-24\part13-10_robot_invasion\src\robot.png")

robot_x = random.randint(0, 640 - robot.get_width())
robot_y = random.randint(0, 480 - robot.get_height())

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            if robot_x <= event.pos[0] <= robot_x + robot.get_width() and robot_y <= event.pos[1] <= robot_y + robot.get_height():
                robot_x = random.randint(0, 640 - robot.get_width())
                robot_y = random.randint(0, 480 - robot.get_height())

        if event.type == pygame.QUIT:
            running = False

    window.fill((0, 0, 0))
    window.blit(robot, (robot_x, robot_y))
    pygame.display.flip()

pygame.quit()
