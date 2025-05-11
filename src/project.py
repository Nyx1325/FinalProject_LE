import pygame

import random


WIDTH, HEIGHT = 320, 240
GRID_SIZE = 2 

def get_random_direction():
    return random.choice(["LEFT", "RIGHT", "UP", "DOWN"])

def generate_cars(count):
    POSSIBLE_CAR_POINTS = [
    (x, y) for x in [23, 100, 143, 224, 265]
             for y in [55, 78, 100, 124, 145, 169, 194]
    ]
    return random.sample(POSSIBLE_CAR_POINTS, count) 

def check_collision_and_bounce(play_rect, direction, obstacles):
    for _, _, _, car_rect in obstacles:
        if play_rect.colliderect(car_rect):
            if direction == "LEFT":
                return "RIGHT"
            elif direction == "RIGHT":
                return "LEFT"
            elif direction == "UP":
                return "DOWN"
            elif direction == "DOWN":
                return "UP"
    return direction

def particle_trails(screen, play_trail, opt_trail, play_x, play_y, opt_x, opt_y):
    play_trail.append((play_x, play_y))
    opt_trail.append((opt_x, opt_y))

    if len(play_trail) > 300:
        play_trail.pop(0)
    if len(opt_trail) > 300:
        opt_trail.pop(0)

    for pos in play_trail:
        opacity = random.randint(50, 150)
        pygame.draw.circle(screen, (180, 100, 100, opacity), pos, random.randint(2, 6))

    for pos in opt_trail:
        opacity = random.randint(50, 150)
        pygame.draw.circle(screen, (100, 180, 100, opacity), pos, random.randint(2, 6))

    if (play_x, play_y) in opt_trail:
        return play_trail, opt_trail, "Game Over"
    if (opt_x, opt_y) in play_trail:
        return play_trail, opt_trail, "You Win"

    return play_trail, opt_trail, None

def display_endgame_text(message):
    """ Displays Game Over or You Win with a slightly transparent background """
    font = pygame.font.Font(None, 50)
    text = font.render(message, True, (255, 255, 255))
    text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    return text, text_rect

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
    obstacles = []
    for x, y in generate_cars(5):
        car_image = random.choice(obstacle_cars)
        rotated_car = pygame.transform.rotate(car_image, random.choice([-90, 90]))
        car_rect = rotated_car.get_rect()
        car_rect.center = (x, y)
        obstacles.append((x, y, rotated_car, car_rect))

    motorcycle_opt = pygame.image.load("green_motorcycle.png")
    opt_x, opt_y = 300, 20
    opt_angle = 0
    opt_direction = get_random_direction()
    
    motorcycle_play = pygame.image.load("red_motorcycle.png")
    play_x, play_y = 20, 20
    play_angle = 0
    direction = "UP"
    moving = False

    play_trail = []
    opt_trail = []

    running = True
    game_status = None
    change_direction_timer = 0
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

        change_direction_timer += 1
        if change_direction_timer >= 15:
            change_direction_timer = 0
            if random.random() < 0.1:
                opt_direction = get_random_direction()
            else:
                if abs(play_x - opt_x) > abs(play_y - opt_y):
                    opt_direction = "LEFT" if play_x < opt_x else "RIGHT"
                else:
                    opt_direction = "UP" if play_y < opt_y else "DOWN"

        opt_rect = pygame.Rect(opt_x, opt_y, motorcycle_opt.get_width(), motorcycle_opt.get_height())
        play_rect = pygame.Rect(play_x, play_y, motorcycle_play.get_width(), motorcycle_play.get_height())
        opt_direction = check_collision_and_bounce(opt_rect, opt_direction, obstacles)

        if opt_direction == "LEFT":
                    opt_angle = 90
        elif opt_direction == "RIGHT":
                    opt_angle = -90
        elif opt_direction == "UP":
                    opt_angle = 0
        elif opt_direction == "DOWN":
                    opt_angle = 180

        if opt_direction == "LEFT" and opt_x - GRID_SIZE >= 5:
            opt_x -= GRID_SIZE
        elif opt_direction == "RIGHT" and opt_x + GRID_SIZE <= WIDTH - motorcycle_opt.get_width():
            opt_x += GRID_SIZE
        elif opt_direction == "UP" and opt_y - GRID_SIZE >= 7:
            opt_y -= GRID_SIZE
        elif opt_direction == "DOWN" and opt_y + GRID_SIZE <= HEIGHT - motorcycle_opt.get_width():
            opt_y += GRID_SIZE

        if moving:
            direction = check_collision_and_bounce(play_rect, direction, obstacles)
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
        for _, _, obstacle_cars, car_rect in obstacles:
            screen.blit(obstacle_cars, car_rect.topleft)

        play_trail, opt_trail, game_status = particle_trails(screen, play_trail, opt_trail, play_x, play_y, opt_x, opt_y)

        if game_status:
            text_surface, text_rect = display_endgame_text(game_status)
            overlay = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
            overlay.fill((50, 50, 50, 80))
            screen.blit(overlay, (0, 0))
            screen.blit(motorcycle_opt, (opt_x, opt_y))
            screen.blit(motorcycle_play, (play_x, play_y))
            screen.blit(text_surface, text_rect)
            pygame.display.flip()
            waiting = True
            while waiting:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        waiting = False
                        running = False

        screen.blit(rotated_opt_motorcycle, rect_opt.topleft)
        screen.blit(rotated_play_motorcycle, rect.topleft)
        pygame.display.flip()
        clock.tick(60)
    pygame.quit()

if __name__ == "__main__":
    main()