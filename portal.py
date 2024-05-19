from dataclasses import dataclass

from random import randint


class Portal:
    def __init__(self, color, display_width, display_height, snake_size):
        self.x = randint(0, display_width // snake_size - 1) * snake_size
        self.y = randint(0, display_height // snake_size - 1) * snake_size
        self.color = color
        self.display_width = display_width
        self.display_height = display_height
        self.snake_size = snake_size

    def generate(self):
        self.x = randint(0, self.display_width // self.snake_size - 1) * self.snake_size
        self.y = randint(0, self.display_height // self.snake_size - 1) * self.snake_size

    def __contains__(self, item):
        return [self.x, self.y] in item
