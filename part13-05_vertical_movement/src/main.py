import pygame

pygame.init()

window = pygame.display.set_mode((640, 480))
robot = pygame.image.load(r"C:\Users\lrnoc\AppData\Local\tmc\vscode\mooc-programming-24\part13-01_four_robots\src\robot.png")

y = 0
velocity = 1
clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    window.fill((0, 0, 0))
    window.blit(robot, (320 - robot.get_width() // 2, y))
    pygame.display.flip()

    y += velocity
    if velocity > 0 and y + robot.get_height() >= 480:
        velocity = -velocity
    if velocity < 0 and y <= 0:
        velocity = -velocity

    clock.tick(60)