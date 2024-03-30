import pygame
import random
from food import *
from snake import *


def display_score(snake_len: int, add_score: int, lives: int) -> None:
    f1 = pygame.font.Font(None, 24)
    text1 = f1.render(f'Score: {snake_len - 1 + add_score}', 1, black)
    text2 = f1.render(f'Lives: {lives}', 1, red)
    display.blit(text1, (3, 3))
    display.blit(text2, (6, 20))


def out_of_border(x: int, y: int) -> bool:
    if 0 <= x < display_width and 0 <= y < display_height:
        return False
    return True


def random_coordinates() -> (int, int):
    return random.randint(0, display_width // snake_size - 1) * snake_size, \
           random.randint(0, display_height // snake_size - 1) * snake_size


def start_game():
    snake_tail = list()
    snake = Snake(display_width // 2, display_height // 2)
    snake.snake_len = 1
    snake.add_score = 0
    snake.fps = 15

    food = Food(*random_coordinates(), random.choice(food_types))

    lives = 3
    while lives > 0:
        for event in pygame.event.get():
            match event.type:
                case pygame.QUIT:
                    lives = 0
                case pygame.KEYDOWN:
                    snake.change_direction(event.key)

        snake.head_x += snake.x_delta
        snake.head_y += snake.y_delta

        if out_of_border(snake.head_x, snake.head_y):
            lives -= 1
            snake = Snake(display_width // 2, display_height // 2)

        display.fill(green)
        pygame.draw.rect(display, food_colors[food.type],
                         [food.x, food.y, snake_size, snake_size])

        snake_tail.append([snake.head_x, snake.head_y])

        while len(snake_tail) > snake.snake_len:
            del snake_tail[0]
        for i in snake_tail[:-1]:
            if i == snake_tail[-1]:
                lives -= 1
                snake = Snake(display_width // 2, display_height // 2)

        for i in snake_tail:
            pygame.draw.rect(display, blue, [i[0], i[1], snake_size, snake_size])

        display_score(snake.snake_len, snake.add_score, lives)
        pygame.display.update()

        if abs(snake.head_x - food.x) < snake_size and abs(snake.head_y - food.y) < snake_size:
            snake.eat_food(food.type)
            food = Food(*random_coordinates(), random.choice(food_types))
            while [food.x, food.y] in snake_tail:
                food = Food(*random_coordinates(), random.choice(food_types))
        clock.tick(snake.fps)

    pygame.quit()
    quit()


snake_speed = 20
snake_size = 20
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
black = (0, 0, 0)
yellow = (255, 255, 0)
purple = (139, 0, 255)
pink = (255, 192, 203)

pygame.init()

display_width = 800
display_height = 600
display = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Snake')

clock = pygame.time.Clock()

start_game()
