import pygame
import random

pygame.init()

window_width = 640
window_height = 480
window = pygame.display.set_mode((window_width, window_height))
robot = pygame.image.load(r"C:\Users\lrnoc\AppData\Local\tmc\vscode\mooc-programming-24\part13-10_robot_invasion\src\robot.png")

robots = []
clock = pygame.time.Clock()

class Robot:
    def __init__(self):
        self.x = random.randint(0, window_width - robot.get_width())
        self.y = 0
        self.velocity_y = random.randint(2, 5)
        self.direction_x = random.choice([-1, 1])

    def move(self):
        if self.y < window_height - robot.get_height():
            self.y += self.velocity_y
        else:
            self.x += self.direction_x * 2
        return self.x > window_width or self.x < -robot.get_width()

    def draw(self):
        window.blit(robot, (self.x, self.y))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    window.fill((0, 0, 0))

    if random.random() < 0.05:
        robots.append(Robot())

    for r in robots[:]:
        r.draw()
        if r.move():
            robots.remove(r)

    pygame.display.flip()

    clock.tick(60)

pygame.quit()
