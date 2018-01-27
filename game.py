import pygame
from dash import Dash
from level import Level
pygame.init()
gameDisplay = pygame.display.set_mode((512,512))
pygame.display.set_caption('CountDownCatch')
clock = pygame.time.Clock()
white = (255, 255, 255)

def run():
    level = Level()
    level.generate(4,2)

    crashed = False
    while not crashed:
        gameDisplay.fill(white)
        level.render(gameDisplay)
        pygame.display.flip()
        clock.tick(10)
run()
pygame.quit()
