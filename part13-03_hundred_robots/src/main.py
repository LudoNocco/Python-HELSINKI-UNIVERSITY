import pygame

pygame.init()

screen = pygame.display.set_mode((640, 480))
robot_image = pygame.image.load(r"C:\Users\lrnoc\AppData\Local\tmc\vscode\mooc-programming-24\part13-01_four_robots\src\robot.png")

robot_w, robot_h = robot_image.get_size()

screen.fill((0, 0, 0))

for row in range(10):
    for col in range(10):
        x = 75 + 10 * row + 40 * col
        y = 100 + 20 * row
        screen.blit(robot_image, (x, y))

pygame.display.update()

while True:
    if pygame.event.get(pygame.QUIT):
        pygame.quit()
        exit()
