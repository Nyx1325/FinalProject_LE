import pygame

import random


WIDTH, HEIGHT = 320, 240
GRID_SIZE = 2 

POSSIBLE_CAR_POINTS = [
    (x, y) for x in [23, 100, 143, 226, 265]
             for y in [55, 78, 100, 122, 143, 165, 186]
]

def generate_cars(count):
    return random.sample(POSSIBLE_CAR_POINTS, count) 

def main():
    pygame.init()

    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Rev Up!")
    parking = pygame.image.load("parking_lot.jpg")
    blue_car = pygame.image.load("blue_car.png")
    orange_car = pygame.image.load("orange_car.png")
    purple_car = pygame.image.load("purple_car.png")

    obstacle_cars = [blue_car, orange_car, purple_car]
    obstacles = [(x, y, random.choice(obstacle_cars)) for x, y in generate_cars(5)]


    motorcycle_opt = pygame.image.load("green_motorcycle.png")
    opt_x, opt_y = 0, -1

    motorcycle_player = pygame.image.load("red_motorcycle.png")
    play_x, play_y = WIDTH // 2, HEIGHT // 2
    angle = 0
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
                    angle = 90
                elif event.key == pygame.K_RIGHT:
                    direction = "RIGHT"
                    angle = -90
                elif event.key == pygame.K_UP:
                    direction = "UP"
                    angle = 0
                elif event.key == pygame.K_DOWN:
                    direction = "DOWN"
                    angle = 180

        if moving:
            if direction == "LEFT" and play_x - GRID_SIZE >= 5:
                play_x -= GRID_SIZE
            elif direction == "RIGHT" and play_x + GRID_SIZE <= WIDTH - motorcycle_player.get_width():
                play_x += GRID_SIZE
            elif direction == "UP" and play_y - GRID_SIZE >= 7:
                play_y -= GRID_SIZE
            elif direction == "DOWN" and play_y + GRID_SIZE <= HEIGHT - motorcycle_player.get_width():
                play_y += GRID_SIZE


        rotated_motorcycle = pygame.transform.rotate(motorcycle_player, angle)
        rect = rotated_motorcycle.get_rect(center=(play_x, play_y))

        screen.blit(parking, (0, 0))
        screen.blit(motorcycle_opt, (opt_x, opt_y))
        screen.blit(rotated_motorcycle, rect.topleft)
        pygame.display.flip()
        clock.tick(60)
    pygame.quit()

if __name__ == "__main__":
    main()