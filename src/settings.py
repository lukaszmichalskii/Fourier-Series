from pygame.math import Vector2


class Settings:
    def __init__(self):
        self.screen_width = 600
        self.screen_height = 400

        self.translate = Vector2(175, self.screen_height/2)

        self.radius = 75
        self.circle_color = (54, 69, 79)
        self.line_color = (255, 255, 255)
