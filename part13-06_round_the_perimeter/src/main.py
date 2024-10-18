import pygame

pygame.init()

window = pygame.display.set_mode((640, 480))
robot = pygame.image.load(r"C:\Users\lrnoc\AppData\Local\tmc\vscode\mooc-programming-24\part13-01_four_robots\src\robot.png")

x, y = 0, 0
velocity = 2
clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    window.fill((0, 0, 0))

    if y == 0 and x < 640 - robot.get_width():
        x += velocity
    elif x == 640 - robot.get_width() and y < 480 - robot.get_height():
        y += velocity
    elif y == 480 - robot.get_height() and x > 0:
        x -= velocity
    elif x == 0 and y > 0:
        y -= velocity

    window.blit(robot, (x, y))
    pygame.display.flip()
    
    clock.tick(60)
