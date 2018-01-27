import pygame
class Dash:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.isVertical = False
        self.horizontal = pygame.image.load('yataycizgi.png')
        self.vertical = pygame.image.load('dikeycizgi.png')
        self._width = 64
        self._height = 64

    def _getImage(self):
        if self.isVertical:
            return self.vertical
        else:
            return self.horizontal

    def render(self,display):
        display.blit(self._getImage(),(self.x * self._width, self.y * self._height))

    def click(self):
        self.isVertical = not self.isVertical
