from random import choice, randint


class Food:

    def __init__(self, display_width, display_height, snake_size):
        self.x = randint(0, display_width // snake_size - 1) * snake_size
        self.y = randint(0, display_height // snake_size - 1) * snake_size
        self.display_width = display_width
        self.display_height = display_height
        self.snake_size = snake_size
        self.type = choice(food_types)

    def __contains__(self, item):
        return [self.x, self.y] in item

    def generate(self):
        self.x, self.y = randint(0, self.display_width // self.snake_size - 1) * self.snake_size, \
                         randint(0, self.display_height // self.snake_size - 1) * self.snake_size
        self.type = choice(food_types)


food_types = ['length+1', 'length-1', 'speed+3', 'speed-3', 'points+3', 'points+5']
food_colors = {'length+1': (255, 0, 0), 'length-1': (255, 255, 0),
               'speed+3': (139, 0, 255), 'speed-3': (255, 192, 203),
               'points+3': (255, 0, 0), 'points+5': (255, 0, 0)}