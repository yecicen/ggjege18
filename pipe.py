import pygame


class Pipe:
    def __init__(self, level, x, y):
        self.x = x
        self.y = y
        self.level = level
        self.angle = 0
        self.image = pygame.image.load('images/top_bottom.png')

        self._width = 64
        self._height = 64

    def render(self, display):
        surf = pygame.transform.rotate(self.image, self.angle)

        rect = self.get_rect()
        display.blit(surf, rect)

    def click(self, pos):
        if self.get_rect().collidepoint(pos):
            self.angle += 90
            self.angle %= 360

    def get_rect(self):
        rect = self.image.get_rect()
        rect.x = self.x * self._width
        rect.y = self.y * self._height

        rect.x += self.level.x
        rect.y += self.level.y
        return rect

    def setPipeType(self, type):
        if type == 1:
            self.image = pygame.image.load('images/top_bottom.png')
        elif type == 2:
            self.image = pygame.image.load('images/left_corner.png')
        elif type == 3:
            self.image = pygame.image.load('images/bottom_up.png')
        elif type == 4:
            self.image = pygame.image.load('images/four_Way.png')
        else:
            print("Pipe Type Error, please use range (1,4)")
