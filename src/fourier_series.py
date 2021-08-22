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
        x = 0
        y = 0

        for i in range(self.settings.n):
            # tracking x, y coordinates
            prev_x = x
            prev_y = y

            n = i * 2 + 1
            x += self.settings.radius * (4 / (n * math.pi)) * math.cos(n * self.time)
            y += self.settings.radius * (4 / (n * math.pi)) * math.sin(n * self.time)

            pygame.draw.circle(self.screen,
                               self.settings.circle_color,
                               self.settings.translate.__add__(Vector2(prev_x, prev_y)),
                               self.settings.radius * (4 / (n * math.pi)), 1)

            pygame.draw.line(self.screen, self.settings.line_color,
                             self.settings.translate.__add__(Vector2(prev_x, prev_y)),
                             self.settings.translate.__add__(Vector2(x, y)), 1)

            # pygame.draw.circle(self.screen,
            #                    self.settings.circle_color,
            #                    self.settings.translate.__add__(Vector2(x, y)), 4)

        self.signal.insert(0, y)

        pygame.draw.line(self.screen, self.settings.line_color,
                         self.settings.translate.__add__(Vector2(x, y)),
                         self.settings.translate.__add__(Vector2(self.settings.translate.x, self.signal[0])))

        for i in range(len(self.signal)):
            pygame.draw.circle(self.screen, self.settings.line_color,
                               self.settings.translate.__add__(Vector2(i/5+self.settings.translate.x, self.signal[i])),1)

            if i / 5 + self.settings.translate.x * 2 >= self.settings.screen_width:
                # removing last value from list: time complexity O(1)
                self.signal.pop()

        self.time += 0.005

    def run(self):
        while 1:
            for event in pygame.event.get():
                if event == pygame.QUIT:
                    pygame.quit()

            self.screen.fill(self.settings.bg_color)
            self.draw()
            pygame.time.wait(1)
            pygame.display.flip()


if __name__ == '__main__':
    fs = FourierSeries()
    fs.run()
