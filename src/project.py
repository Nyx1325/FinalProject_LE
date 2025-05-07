import pygame



WIDTH, HEIGHT = 320, 240
GRID_SIZE = 10 

def main():
    pygame.init()

    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Rev Up!")
    parking = pygame.image.load("background.jpg")
    motorcycle_opt = pygame.image.load("oponent.png")
    opt_x, opt_y = 0, 0
    motorcycle_player = pygame.image.load("character.png")
    play_x, play_y = 0, 0

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    play_x -= GRID_SIZE
                elif event.key == pygame.K_RIGHT:
                    play_x += GRID_SIZE
                elif event.key == pygame.K_UP:
                    play_y -= GRID_SIZE
                elif event.key == pygame.K_DOWN:
                    play_y += GRID_SIZE

        screen.blit(parking, (0, 0))
        screen.blit(motorcycle_opt, (opt_x, opt_y))
        screen.blit(motorcycle_player, (play_x, play_y))
        pygame.display.flip()
        clock.tick(60)
    pygame.quit()

if __name__ == "__main__":
    main()