import pygame



WIDTH, HEIGHT = 320, 240
GRID_SIZE = 10 

def main():
    pygame.init()

    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Rev Up!")
    parking = pygame.image.load("background.jpg")
    motorcycle = pygame.image.load("character.png")
    char_x, char_y = 0, 0  # Start position (grid-based)

    running = True
    while running:
        

        screen.blit(parking, (0, 0))
        screen.blit(motorcycle, (char_x, char_y))
        pygame.display.flip()
        clock.tick(60)
    pygame.quit()

if __name__ == "__main__":
    main()