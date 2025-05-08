import pygame

import random


WIDTH, HEIGHT = 320, 240
GRID_SIZE = 2 

def get_random_direction():
    return random.choice(["LEFT", "RIGHT", "UP", "DOWN"])

def generate_cars(count):
    POSSIBLE_CAR_POINTS = [
    (x, y) for x in [23, 100, 143, 226, 265]
             for y in [55, 78, 100, 122, 143, 165, 186]
    ]
    return random.sample(POSSIBLE_CAR_POINTS, count) 

def check_collision_and_bounce(x, y, direction, obstacles):
    for ox, oy, _ in obstacles:
        if abs(x - ox) < GRID_SIZE and abs(y - oy) < GRID_SIZE:
            if direction == "LEFT":
                return "RIGHT"
            elif direction == "RIGHT":
                return "LEFT"
            elif direction == "UP":
                return "DOWN"
            elif direction == "DOWN":
                return "UP"
    return direction

def main():
    pygame.init()

    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Rev Up!")
    parking = pygame.image.load("parking_lot.jpg")

    obstacle_cars = [
        pygame.image.load("blue_car.png"),
        pygame.image.load("orange_car.png"),
        pygame.image.load("purple_car.png")
    ]
    obstacles = [(x, y, random.choice(obstacle_cars)) for x, y in generate_cars(5)]


    motorcycle_opt = pygame.image.load("green_motorcycle.png")
    opt_x, opt_y = WIDTH // 4, HEIGHT // 4
    opt_angle = 0
    opt_direction = get_random_direction()
    
    motorcycle_play = pygame.image.load("red_motorcycle.png")
    play_x, play_y = WIDTH // 2, HEIGHT // 2
    play_angle = 0
    direction = "UP"
    moving = False

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                moving = True
                if event.key == pygame.K_LEFT:
                    direction = "LEFT"
                    play_angle = 90
                elif event.key == pygame.K_RIGHT:
                    direction = "RIGHT"
                    play_angle = -90
                elif event.key == pygame.K_UP:
                    direction = "UP"
                    play_angle = 0
                elif event.key == pygame.K_DOWN:
                    direction = "DOWN"
                    play_angle = 180

        if random.random() < 0.3:
            opt_direction = get_random_direction()
        else:
            if abs(play_x - opt_x) > abs(play_y - opt_y):
                opt_direction = "LEFT" if play_x < opt_x else "RIGHT"
            else:
                opt_direction = "UP" if play_y < opt_y else "DOWN"
        opt_direction = check_collision_and_bounce(opt_x, opt_y, opt_direction, obstacles)

        if moving:
            direction = check_collision_and_bounce(play_x, play_y, direction, obstacles)
            if direction == "LEFT" and play_x - GRID_SIZE >= 5:
                play_x -= GRID_SIZE
            elif direction == "RIGHT" and play_x + GRID_SIZE <= WIDTH - motorcycle_play.get_width():
                play_x += GRID_SIZE
            elif direction == "UP" and play_y - GRID_SIZE >= 7:
                play_y -= GRID_SIZE
            elif direction == "DOWN" and play_y + GRID_SIZE <= HEIGHT - motorcycle_play.get_width():
                play_y += GRID_SIZE

        rotated_opt_motorcycle = pygame.transform.rotate(motorcycle_opt, opt_angle)
        rect_opt = rotated_opt_motorcycle.get_rect(center=(opt_x, opt_y))
        rotated_play_motorcycle = pygame.transform.rotate(motorcycle_play, play_angle)
        rect = rotated_play_motorcycle.get_rect(center=(play_x, play_y))

        screen.blit(parking, (0, 0))
        screen.blit(rotated_opt_motorcycle, rect_opt.topleft)
        screen.blit(rotated_play_motorcycle, rect.topleft)
        pygame.display.flip()
        clock.tick(60)
    pygame.quit()

if __name__ == "__main__":
    main()