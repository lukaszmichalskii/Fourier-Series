import math

import pygame as pygame
from pygame.math import Vector2

from src.settings import Settings


class FourierSeries:

    def __init__(self):
        pygame.init()
        pygame.event.set_allowed([pygame.QUIT])
        self.clock = pygame.time.Clock()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height),
                                              flags=pygame.DOUBLEBUF | pygame.HWSURFACE | pygame.NOFRAME)

        self.time = 0
        self.signal = []

    def draw(self):
        pygame.draw.circle(self.screen,
                           self.settings.circle_color,
                           self.settings.translate,
                           self.settings.radius, 1)

        x = self.settings.radius * math.cos(self.time)
        y = self.settings.radius * math.sin(self.time)
        self.signal.insert(0, y)

        pygame.draw.line(self.screen, self.settings.line_color,
                         self.settings.translate, self.settings.translate.__add__(Vector2(x, y)), 1)
        pygame.draw.circle(self.screen,
                           self.settings.circle_color,
                           self.settings.translate.__add__(Vector2(x, y)), 4)

        pygame.draw.line(self.screen, self.settings.line_color,
                         self.settings.translate.__add__(Vector2(x, y)),
                         self.settings.translate.__add__(Vector2(self.settings.translate.x, self.signal[0])))

        for i in range(len(self.signal)):
            pygame.draw.circle(self.screen, self.settings.circle_color,
                               self.settings.translate.__add__(Vector2(i/10 + self.settings.translate.x, self.signal[i])), 1)

        self.time += 0.009

    def run(self):
        while 1:
            for event in pygame.event.get():
                if event == pygame.QUIT:
                    pygame.quit()

            if len(self.signal) > 1900:
                self.signal.pop()

            self.screen.fill((0, 0, 0))
            self.draw()
            pygame.display.flip()
            self.clock.tick(200)


if __name__ == '__main__':
    fs = FourierSeries()
    fs.run()
