import pygame


if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption('клетчатое поле')
    size = width, height = 700, 700
    screen = pygame.display.set_mode(size)
    clock = pygame.time.Clock()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill((212, 26, 67))
        pygame.display.flip()
        clock.tick(60)
    pygame.quit()