import pygame
from level import Level

pygame.init()
gameDisplay = pygame.display.set_mode((512, 512))
pygame.display.set_caption('CountDownCatch')
clock = pygame.time.Clock()
white = (255, 255, 255)


def run():
    level = Level(128, 196)
    level.generate(4, 2)

    crashed = False
    while not crashed:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                crashed = True
            elif event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                level.click(pos)

        gameDisplay.fill(white)
        level.render(gameDisplay)
        pygame.display.flip()
        clock.tick(60)


run()
pygame.quit()
