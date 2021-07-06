import pygame
import random
from random import randint

if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption('Ritbc')
    icon = pygame.image.load("iconka.png")
    pygame.display.set_icon(icon)
    size = width, height = 700, 700
    screen = pygame.display.set_mode(size)
    clock = pygame.time.Clock()
    running = True
    usr_x = randint(45, 655)
    usr_y = randint(45, 655)
    usr_width = 45
    usr_height = 45
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill((212, 26, 67))
        pygame.draw.rect(screen, (247, 240, 22), (usr_x, usr_y, usr_width, usr_height))
        pygame.display.update()
        pygame.display.flip()
        clock.tick(60)
    pygame.quit()
