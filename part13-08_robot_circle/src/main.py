import pygame
import math

pygame.init()

window = pygame.display.set_mode((640, 480))
robot = pygame.image.load(r"C:\Users\lrnoc\AppData\Local\tmc\vscode\mooc-programming-24\part13-01_four_robots\src\robot.png")

center_x, center_y = 320, 240
radius = 150
angle = 0
clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    window.fill((0, 0, 0))

    for i in range(10):
        robot_x = center_x + radius * math.cos(angle + i * math.pi / 5) - robot.get_width() // 2
        robot_y = center_y + radius * math.sin(angle + i * math.pi / 5) - robot.get_height() // 2
        window.blit(robot, (robot_x, robot_y))

    angle += 0.02
    pygame.display.flip()

    clock.tick(60)
