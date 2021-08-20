from pygame.math import Vector2


class Settings:
    def __init__(self):
        self.screen_width = 600
        self.screen_height = 400

        self.translate = Vector2(self.screen_width/3, self.screen_height/2)

        self.radius = self.screen_height/4
        self.circle_color = (255, 255, 255)
        self.line_color = (255, 255, 255)