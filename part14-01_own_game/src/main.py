import pygame
import random

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))

try:
    robot_image = pygame.image.load('src/robot.png')
    coin_image = pygame.image.load('src/coin.png')
    monster_image = pygame.image.load('src/monster.png')
except pygame.error as e:
    print(f"Error loading images: {e}")
    pygame.quit()
    exit()

robot_image = pygame.transform.scale(robot_image, (50, 50))
coin_image = pygame.transform.scale(coin_image, (30, 30))
monster_image = pygame.transform.scale(monster_image, (50, 50))

clock = pygame.time.Clock()

robot_pos = [WIDTH // 2, HEIGHT - 60]
coins = [[random.randint(0, WIDTH - 30), -30] for _ in range(3)]
monsters = [[random.randint(0, WIDTH - 50), -50] for _ in range(3)]
velocity = 5
fall_speed = 3
score = 0
level = 1
lives = 3

font = pygame.font.Font(None, 36)

def move_robot(keys_pressed):
    if keys_pressed[pygame.K_LEFT] and robot_pos[0] > 0:
        robot_pos[0] -= velocity
    if keys_pressed[pygame.K_RIGHT] and robot_pos[0] < WIDTH - 50:
        robot_pos[0] += velocity

def move_objects(objects):
    for obj in objects:
        obj[1] += fall_speed
        if obj[1] > HEIGHT:
            obj[0] = random.randint(0, WIDTH - 50 if obj == monsters else WIDTH - 30)
            obj[1] = -50

def check_coin_collision():
    global score, level, fall_speed
    robot_rect = pygame.Rect(robot_pos[0], robot_pos[1], 50, 50)
    for coin in coins:
        coin_rect = pygame.Rect(coin[0], coin[1], 30, 30)
        if robot_rect.colliderect(coin_rect):
            score += 1
            coin[0] = random.randint(0, WIDTH - 30)
            coin[1] = -30
            
            if score % 20 == 0:
                level += 1
                fall_speed += 1

def check_monster_collision():
    global lives
    robot_rect = pygame.Rect(robot_pos[0], robot_pos[1], 50, 50)
    for monster in monsters:
        monster_rect = pygame.Rect(monster[0], monster[1], 50, 50)
        if robot_rect.colliderect(monster_rect):
            lives -= 1
            monster[0] = random.randint(0, WIDTH - 50)
            monster[1] = -50
            if lives == 0:
                return True
    return False

def draw_game():
    screen.fill((255, 255, 255))
    screen.blit(robot_image, robot_pos)

    for coin in coins:
        screen.blit(coin_image, coin)
    for monster in monsters:
        screen.blit(monster_image, monster)

    score_text = font.render(f"Score: {score}", True, (0, 0, 0))
    screen.blit(score_text, (10, 10))
    
    level_text = font.render(f"Level: {level}", True, (0, 0, 0))
    screen.blit(level_text, (10, 50))
    
    lives_text = font.render(f"Lives: {lives}", True, (0, 0, 0))
    screen.blit(lives_text, (10, 90))
    
    pygame.display.flip()

def main():
    global velocity
    running = True
    while running:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys_pressed = pygame.key.get_pressed()
        move_robot(keys_pressed)
        move_objects(coins)
        move_objects(monsters)
        check_coin_collision()

        if check_monster_collision():
            print("Game Over")
            running = False

        draw_game()

    pygame.quit()

if __name__ == "__main__":
    main()
