import pygame
import random


def out_of_border(x: int, y: int) -> bool:
    if 0 <= x < display_width and 0 <= y < display_height:
        return False
    return True


def start_game():
    head_x, head_y = (300, 300)

    x_delta, y_delta = (0, 0)

    snake = list()
    snake_len = 1

    food_x = random.randrange(0, display_width // snake_size - 1) * snake_size
    food_y = random.randrange(0, display_height // snake_size - 1) * snake_size

    game_over = False
    while not game_over:
        for event in pygame.event.get():
            match event.type:
                case pygame.QUIT:
                    game_over = True
                case pygame.KEYDOWN:
                    match event.key:
                        case pygame.K_LEFT:
                            if (x_delta, y_delta) != TURN_RIGHT:
                                x_delta, y_delta = TURN_LEFT
                        case pygame.K_RIGHT:
                            if (x_delta, y_delta) != TURN_LEFT:
                                x_delta, y_delta = TURN_RIGHT
                        case pygame.K_UP:
                            if (x_delta, y_delta) != TURN_DOWN:
                                x_delta, y_delta = TURN_UP
                        case pygame.K_DOWN:
                            if (x_delta, y_delta) != TURN_UP:
                                x_delta, y_delta = TURN_DOWN

        head_x += x_delta
        head_y += y_delta

        if out_of_border(head_x, head_y):
            game_over = True

        display.fill(green)
        pygame.draw.rect(display, red, [food_x, food_y, snake_size, snake_size])

        snake.append([head_x, head_y])

        if len(snake) > snake_len:
            del snake[0]
        for i in snake[:-1]:
            if i == snake[-1]:
                game_over = True

        for i in snake:
            pygame.draw.rect(display, blue, [i[0], i[1], snake_size, snake_size])

        f1 = pygame.font.Font('digitalcyrillic1.otf', 36)
        text1 = f1.render(str(snake_len - 1), 1, black)
        display.blit(text1,(3, 3))

        pygame.display.update()

        if abs(head_x - food_x) < snake_size and abs(head_y - food_y) < snake_size:
            food_x = random.randrange(0, display_width // snake_size - 1) * snake_size
            food_y = random.randrange(0, display_height // snake_size - 1) * snake_size
            snake_len += 1

        clock.tick(15)

    pygame.quit()
    quit()


pygame.init()
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
black = (0, 0, 0)

display_width = 800
display_height = 600
display = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Snake')

snake_speed = 20
snake_size = 20
TURN_LEFT = (-snake_speed, 0)
TURN_RIGHT = (snake_speed, 0)
TURN_UP = (0, -snake_speed)
TURN_DOWN = (0, snake_speed)

clock = pygame.time.Clock()

start_game()
