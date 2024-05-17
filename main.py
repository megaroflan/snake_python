import pygame
import random
from food import *
from snake import *
from levels import *
import pygame_menu
from portal import *


def display_score(snake_len: int, add_score: int, lives: int, speed: int) -> None:
    f1 = pygame.font.Font(None, 24)
    text1 = f1.render(f'Score: {snake_len - 1 + add_score}', 1, black)
    text2 = f1.render(f'Lives: {lives}', 1, red)
    text3 = f1.render(f'Speed: {speed}', 1, black)
    display.blit(text1, (3, 3))
    display.blit(text2, (6, 20))
    display.blit(text3, (720, 3))


def out_of_border(x: int, y: int) -> bool:
    if 0 <= x < display_width and 0 <= y < display_height:
        return False
    return True


def random_coordinates() -> (int, int):
    return random.randint(0, display_width // snake_size - 1) * snake_size, \
           random.randint(0, display_height // snake_size - 1) * snake_size


def start_game():
    global best_score
    snake_tail = list()
    snake = Snake(display_width // 2, display_height // 2)
    snake.snake_len = 1
    snake.add_score = 0
    snake.fps = 15
    on_pause = 0
    portal_sound = pygame.mixer.Sound('portal.mp3')
    portal_sound.set_volume(0.25)

    current_level_num = 0
    current_level = levels[current_level_num]

    food = Food(*random_coordinates(), random.choice(food_types))
    while snake.snake_len == 1 and food.type == 'length-1' or [food.x, food.y] in current_level:
        food = Food(*random_coordinates(), random.choice(food_types))

    portals = [Portal(*random_coordinates(), (255, 154, 0)),
               Portal(*random_coordinates(), (39, 167, 216))]
    while [portals[0].x, portals[0].y] in current_level:
        portals[0] = Portal(*random_coordinates(), (255, 154, 0))

    while [portals[1].x, portals[1].y] in current_level:
        portals[1] = Portal(*random_coordinates(), (255, 154, 0))

    lives = 3
    while lives > 0:
        for event in pygame.event.get():
            match event.type:
                case pygame.QUIT:
                    lives = 0
                case pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        lives = 0
                    elif event.key == pygame.K_p:
                        on_pause = (on_pause + 1) % 2
                    if not on_pause:
                        snake.change_direction(event.key)

        if not on_pause:
            snake.head_x += snake.x_delta
            snake.head_y += snake.y_delta
            snake_tail.append([snake.head_x, snake.head_y])

        if out_of_border(snake.head_x, snake.head_y):
            lives -= 1
            best_score = max(best_score, snake.snake_len - 1 + snake.add_score)
            snake = Snake(display_width // 2, display_height // 2)
            while snake.snake_len == 1 and food.type == 'length-1' or [food.x, food.y] in current_level:
                food = Food(*random_coordinates(), random.choice(food_types))

        display.fill(green)
        pygame.draw.ellipse(display, portals[0].color, [portals[0].x - 5, portals[0].y - 5, 30, 30])
        pygame.draw.ellipse(display, portals[1].color, [portals[1].x - 5, portals[1].y - 5, 30, 30])

        pygame.draw.ellipse(display, black, [portals[0].x, portals[0].y, snake_size, snake_size])
        pygame.draw.ellipse(display, black, [portals[1].x, portals[1].y, snake_size, snake_size])

        pygame.draw.rect(display, food_colors[food.type],
                         [food.x, food.y, snake_size, snake_size])

        while len(snake_tail) > snake.snake_len:
            del snake_tail[0]

        for i in snake_tail[:-1]:
            if i == snake_tail[-1]:
                lives -= 1
                best_score = max(best_score, snake.snake_len - 1 + snake.add_score)
                snake = Snake(display_width // 2, display_height // 2)
                while snake.snake_len == 1 and food.type == 'length-1' or [food.x, food.y] in current_level:
                    food = Food(*random_coordinates(), random.choice(food_types))

        if [snake.head_x, snake.head_y] in current_level:
            lives -= 1
            best_score = max(best_score, snake.snake_len - 1 + snake.add_score)
            snake = Snake(display_width // 2, display_height // 2)

        for i in snake_tail:
            pygame.draw.rect(display, blue, [i[0], i[1], snake_size, snake_size])

        for i in current_level.blocks:
            pygame.draw.rect(display, dark_grey, [i[0], i[1], snake_size, snake_size])

        display_score(snake.snake_len, snake.add_score, lives, snake.fps // 3)
        pygame.display.update()

        if abs(snake.head_x - food.x) < snake_size and abs(snake.head_y - food.y) < snake_size:
            snake.eat_food(food.type)
            food = Food(*random_coordinates(), random.choice(food_types))
            while [food.x, food.y] in snake_tail or \
                    [food.x, food.y] in current_level or snake.snake_len == 1 and food.type == 'length-1':
                food = Food(*random_coordinates(), random.choice(food_types))
        if snake.snake_len + snake.add_score >= 30:
            current_level_num = (current_level_num + 1) % 3
            current_level = levels[current_level_num]
            best_score += snake.snake_len - 1 + snake.add_score
            snake = Snake(display_width // 2, display_height // 2)
            portals = [Portal(*random_coordinates(), (255, 154, 0)),
                       Portal(*random_coordinates(), (39, 167, 216))]
            while [portals[0].x, portals[0].y] in current_level:
                portals[0] = Portal(*random_coordinates(), (255, 154, 0))

            while [portals[1].x, portals[1].y] in current_level:
                portals[1] = Portal(*random_coordinates(), (255, 154, 0))
        if abs(snake.head_x - portals[0].x) < snake_size and abs(snake.head_y - portals[0].y) < snake_size:
            snake.head_x = portals[1].x
            snake.head_y = portals[1].y
            portal_sound.play()
        elif abs(snake.head_x - portals[1].x) < snake_size and abs(snake.head_y - portals[1].y) < snake_size:
            snake.head_x = portals[0].x
            snake.head_y = portals[0].y
            portal_sound.play()
        clock.tick(snake.fps)
    best_score += snake.snake_len - 1 + snake.add_score
    menu.disable()
    menu.clear()
    menu.add.label(f'Best score: {best_score}')
    menu.add.button('Play', start_game)
    menu.add.button('Quit', pygame_menu.events.EXIT)
    menu.enable()


snake_speed = 20
snake_size = 20
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
black = (0, 0, 0)
yellow = (255, 255, 0)
purple = (139, 0, 255)
pink = (255, 192, 203)
dark_grey = (71, 64, 64)
WindowClose = 32787
best_score = 0

pygame.init()

display_width = 800
display_height = 600
display = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Snake')

menu = pygame_menu.Menu('Snake', 800, 600,
                        theme=pygame_menu.themes.THEME_GREEN)
menu.add.label(f'Your score: {best_score}')
menu.add.button('Play', start_game)
menu.add.button('Quit', pygame_menu.events.EXIT)
clock = pygame.time.Clock()
pygame.mixer.music.load('guts_theme.mp3')
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.1)
menu.mainloop(display)
