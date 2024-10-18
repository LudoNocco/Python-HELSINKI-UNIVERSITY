import pygame

pygame.init()

size = (640, 480)
screen = pygame.display.set_mode(size)
robot_image = pygame.image.load(r"C:\Users\lrnoc\AppData\Local\tmc\vscode\mooc-programming-24\part13-02_robots_row\src\robot.png")

robot_width = robot_image.get_width()

screen.fill((0, 0, 0))

positions = [(75 + robot_width * i, 100) for i in range(10)]
for pos in positions:
    screen.blit(robot_image, pos)

pygame.display.update()

while True:
    if any(event.type == pygame.QUIT for event in pygame.event.get()):
        pygame.quit()
        exit()
