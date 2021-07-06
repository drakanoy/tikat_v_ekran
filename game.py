import pygame
from random import randint
from черновик import color


class Cletka:
    def __init__(self, color):
        self.color = color
        self.height = 45
        self.wight = 45


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
    kvadrat = Cletka(color())
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos[0], event.pos[1]
                if usr_x < x < usr_x + 45 and usr_y < y < usr_y + 45:
                    kvadrat = Cletka(color())
        screen.fill((212, 26, 67))
        pygame.draw.rect(screen, kvadrat.color, (usr_x, usr_y, kvadrat.wight, kvadrat.height))
        pygame.display.update()
        pygame.display.flip()
        clock.tick(60)
    pygame.quit()
