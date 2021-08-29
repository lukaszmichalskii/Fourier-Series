import math

import pygame as pygame
from pygame.math import Vector2

from src.discrete_fourier_transform import discrete_fourier_transform
from src.settings import Settings
from src.signal_generator import SignalGenerator


class FourierSeries:

    def __init__(self):
        pygame.init()
        pygame.event.set_allowed([pygame.QUIT])
        self.clock = pygame.time.Clock()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height),
                                              flags=pygame.DOUBLEBUF | pygame.HWSURFACE | pygame.NOFRAME)

        self.signal_generator = SignalGenerator()

        self.x_signal = self.signal_generator.generate_signal()[0]
        self.y_signal = self.signal_generator.generate_signal()[1]

        self.fourierX = discrete_fourier_transform(self.x_signal)
        self.fourierY = discrete_fourier_transform(self.y_signal)

        self.time = 0
        self.signal = []

    def _check_events(self):
        for event in pygame.event.get():
            if event == pygame.QUIT:
                pygame.quit()

    def _set_position(self):
        vector_x = self._draw_fourier(self.settings.screen_width * 5 / 7,
                                    self.settings.screen_height / 5, 0, self.fourierX)
        vector_y = self._draw_fourier(self.settings.screen_width / 7,
                                    self.settings.screen_height / 2, math.pi / 2, self.fourierY)
        vector = Vector2(vector_x.x, vector_y.y)

        return {'vector_x': vector_x, 'vector_y': vector_y, 'vector': vector}

    def _draw_fourier(self,x, y, rotation, fourier):
        for i in range(len(fourier)):
            # tracking x, y coordinates
            prev_x = x
            prev_y = y

            freq = fourier[i].get('freq')
            radius = fourier[i].get('amp')
            phase = fourier[i].get('phase')
            x += radius * math.cos(freq * self.time + phase + rotation)
            y += radius * math.sin(freq * self.time + phase + rotation)

            pygame.draw.circle(self.screen,
                               self.settings.circle_color,
                               self.settings.translate.__add__(Vector2(prev_x, prev_y)),
                               radius, 1)

            pygame.draw.line(self.screen, self.settings.line_color,
                             self.settings.translate.__add__(Vector2(prev_x, prev_y)),
                             self.settings.translate.__add__(Vector2(x, y)), 1)

        return Vector2(x, y)

    def _draw_signal(self, surface, signal, color):
        for i in range(len(signal)-1):
            # pygame.draw.circle(self.screen, self.settings.line_color,
            #                    self.settings.translate.__add__(Vector2(self.signal[i].x, self.signal[i].y)),1)
            pygame.draw.line(surface, color,
                             (signal[i].x, signal[i].y), (signal[i+1].x, signal[i+1].y))

    def _draw_position_lines(self, surface, vector_x, vector_y, vector, color):
        pygame.draw.line(surface, color, (vector_x.x, vector_x.y), (vector.x, vector.y))
        pygame.draw.line(surface, color, (vector_y.x, vector_y.y), (vector.x, vector.y))

        # epicycles control
        if self.time > math.pi * 2:
            self.time = 0
            self.signal = []

    def _draw(self):
        vectors = self._set_position()
        vector_x = vectors['vector_x']
        vector_y = vectors['vector_y']
        vector = vectors['vector']
        self.signal.insert(0, vector)

        # drawing section
        self._draw_position_lines(self.screen, vector_x, vector_y, vector, self.settings.line_color)
        self._draw_signal(self.screen, self.signal, self.settings.line_color)

        dt = 2 * math.pi / len(self.fourierY)
        self.time += dt

    def run(self):
        while 1:
            self._check_events()

            self.screen.fill(self.settings.bg_color)
            self._draw()
            self.clock.tick(60)
            pygame.display.flip()


if __name__ == '__main__':
    fs = FourierSeries()
    fs.run()
