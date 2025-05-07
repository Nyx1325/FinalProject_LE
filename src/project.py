import pygame

import math


WIDTH, HEIGHT = 320, 240
GRID_SIZE = 10 

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
    speed = GRID_SIZE

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    angle += 10 
                elif event.key == pygame.K_RIGHT:
                    angle -= 10
                elif event.key == pygame.K_UP:
                    play_x += speed * math.cos(math.radians(angle))
                    play_y -= speed * math.sin(math.radians(angle))
                elif event.key == pygame.K_DOWN:
                    play_x -= speed * math.cos(math.radians(angle))
                    play_y += speed * math.sin(math.radians(angle))

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