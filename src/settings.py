from pygame.math import Vector2


class Settings:
    def __init__(self):
        self.screen_width = 800
        self.screen_height = 600
        self.bg_color = (0,0,0)

        self.translate = Vector2(0, 0)

        self.n = 5

        self.circle_color = (54, 69, 79)
        self.line_color = (255, 255, 255)
