import pygame
import math
import time

pygame.init()

window = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Clock")

clock_radius = 200
center_x, center_y = 320, 240
clock_color = (255, 0, 0)
hour_color = (0, 0, 255)
minute_color = (0, 255, 0)
second_color = (255, 255, 0)
clock = pygame.time.Clock()

title_length = 185

def draw_hand(angle, length, color):
    end_x = center_x + length * math.cos(angle)
    end_y = center_y + length * math.sin(angle)
    pygame.draw.line(window, color, (center_x, center_y), (end_x, end_y), 5)

def center_text_in_title(system_time, total_length):
    # Calculate how many spaces to pad on both sides
    padding = (total_length - len(system_time)) // 2
    return ' ' * padding + system_time + ' ' * padding

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    current_time = time.localtime()
    system_time = time.strftime("%H:%M:%S", current_time)

    # Center the system time in the window title
    centered_time = center_text_in_title(system_time, title_length)
    pygame.display.set_caption(centered_time)

    window.fill((0, 0, 0))

    pygame.draw.circle(window, clock_color, (center_x, center_y), clock_radius, 5)

    second_angle = math.radians(270 + (current_time.tm_sec * 6))
    minute_angle = math.radians(270 + (current_time.tm_min * 6))
    hour_angle = math.radians(270 + ((current_time.tm_hour % 12) * 30) + (current_time.tm_min * 0.5))

    draw_hand(hour_angle, clock_radius - 80, hour_color)
    draw_hand(minute_angle, clock_radius - 50, minute_color)
    draw_hand(second_angle, clock_radius - 30, second_color)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
