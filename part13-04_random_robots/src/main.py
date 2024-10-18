import pygame
from random import randint

pygame.init()

screen = pygame.display.set_mode((640, 480))
robot = pygame.image.load(r"C:\Users\lrnoc\AppData\Local\tmc\vscode\mooc-programming-24\part13-01_four_robots\src\robot.png")

robot_w, robot_h = robot.get_size()

screen.fill((0, 0, 0))

random_positions = [(randint(0, 640 - robot_w), randint(0, 480 - robot_h)) for _ in range(1000)]
for pos in random_positions:
    screen.blit(robot, pos)

pygame.display.update()

while True:
    if pygame.event.peek(pygame.QUIT):
        pygame.quit()
        exit()
