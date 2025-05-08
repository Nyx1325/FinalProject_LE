import pygame

import math


WIDTH, HEIGHT = 320, 240
GRID_SIZE = 2 

def main():
    pygame.init()

    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Rev Up!")
    parking = pygame.image.load("parkinglot.jpg")
    motorcycle_opt = pygame.image.load("green motorcycle.png")
    opt_x, opt_y = 0, -1

    motorcycle_player = pygame.image.load("Red motorcycle.png")
    play_x, play_y = WIDTH // 2, HEIGHT // 2
    angle = 0
    direction = "UP"  # Default direction
    moving = False  # Starts stationary

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                moving = True  # Start moving
                if event.key == pygame.K_LEFT:
                    direction = "LEFT"
                    angle = 90  # Snap rotation to left
                elif event.key == pygame.K_RIGHT:
                    direction = "RIGHT"
                    angle = -90  # Snap rotation to right
                elif event.key == pygame.K_UP:
                    direction = "UP"
                    angle = 0  # Facing upward
                elif event.key == pygame.K_DOWN:
                    direction = "DOWN"
                    angle = 180  # Facing downward

        if moving:
            if direction == "LEFT" and play_x - GRID_SIZE >= 0:
                play_x -= GRID_SIZE
            elif direction == "RIGHT" and play_x + GRID_SIZE <= WIDTH - motorcycle_player.get_width():
                play_x += GRID_SIZE
            elif direction == "UP" and play_y - GRID_SIZE >= 0:
                play_y -= GRID_SIZE
            elif direction == "DOWN" and play_y + GRID_SIZE <= HEIGHT - motorcycle_player.get_height():
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