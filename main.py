import pygame
import random
from food import *


def display_score(snake_len: int, add_score: int) -> None:
    f1 = pygame.font.Font(None, 36)
    text1 = f1.render(str(snake_len - 1 + add_score), 1, black)
    display.blit(text1, (3, 3))


def out_of_border(x: int, y: int) -> bool:
    if 0 <= x < display_width and 0 <= y < display_height:
        return False
    return True


def random_coordinates() -> (int, int):
    return random.randint(0, display_width // snake_size - 1) * snake_size, \
           random.randint(0, display_height // snake_size - 1) * snake_size


def start_game():
    head_x, head_y = (display_width // 2, display_height // 2)
    x_delta, y_delta = (0, 0)

    snake = list()
    snake_len = 1
    add_score = 0
    fps = 15

    food = Food(*random_coordinates(), random.choice(food_types))

    game_over = False
    while not game_over:
        for event in pygame.event.get():
            match event.type:
                case pygame.QUIT:
                    game_over = True
                case pygame.KEYDOWN:
                    match event.key:
                        case pygame.K_LEFT:
                            if (x_delta, y_delta) != (snake_speed, 0):
                                x_delta, y_delta = (-snake_speed, 0)
                        case pygame.K_RIGHT:
                            if (x_delta, y_delta) != (-snake_speed, 0):
                                x_delta, y_delta = (snake_speed, 0)
                        case pygame.K_UP:
                            if (x_delta, y_delta) != (0, snake_speed):
                                x_delta, y_delta = (0, -snake_speed)
                        case pygame.K_DOWN:
                            if (x_delta, y_delta) != (0, -snake_speed):
                                x_delta, y_delta = (0, snake_speed)

        head_x += x_delta
        head_y += y_delta

        if out_of_border(head_x, head_y):
            game_over = True

        display.fill(green)
        pygame.draw.rect(display, food_colors[food.type],
                         [food.x, food.y, snake_size, snake_size])

        snake.append([head_x, head_y])

        while len(snake) > snake_len:
            del snake[0]
        for i in snake[:-1]:
            if i == snake[-1]:
                game_over = True

        for i in snake:
            pygame.draw.rect(display, blue, [i[0], i[1], snake_size, snake_size])

        display_score(snake_len, add_score)
        pygame.display.update()

        if abs(head_x - food.x) < snake_size and abs(head_y - food.y) < snake_size:
            match food.type:
                case 'length+1':
                    snake_len += 1
                case 'length-1':
                    snake_len -= 1
                case 'speed+3':
                    if fps != 60:
                        fps += 3
                    snake_len += 1
                case 'speed-3':
                    if fps != 3:
                        fps -= 3
                    snake_len += 1
                case 'points+3':
                    add_score += 2
                    snake_len += 1
                case 'points+5':
                    add_score += 4
                    snake_len += 1
            food = Food(*random_coordinates(), random.choice(food_types))
            while [food.x, food.y] in snake:
                food = Food(*random_coordinates(), random.choice(food_types))
        clock.tick(fps)

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
