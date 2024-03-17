import pygame


def out_of_border(x: int, y: int) -> bool:
    if 0 <= x < display_width and 0 <= y < display_height:
        return False
    return True


def start_game():
    head_x, head_y = (300, 300)

    x_delta, y_delta = (0, 0)

    snake_speed = 2.5
    snake_size = 10
    snake_tail = list()
    snake_len = 1

    game_over = False
    while not game_over:
        for event in pygame.event.get():
            match event.type:
                case pygame.QUIT:
                    game_over = True
                case pygame.KEYDOWN:
                    match event.key:
                        case pygame.K_LEFT:
                            x_delta, y_delta = (-snake_speed, 0)
                        case pygame.K_RIGHT:
                            x_delta, y_delta = (snake_speed, 0)
                        case pygame.K_UP:
                            x_delta, y_delta = (0, -snake_speed)
                        case pygame.K_DOWN:
                            x_delta, y_delta = (0, snake_speed)
        head_x += x_delta
        head_y += y_delta

        if out_of_border(head_x, head_y):
            game_over = True

        display.fill(green)
        pygame.draw.rect(display, blue, [head_x, head_y, snake_size, snake_size])
        pygame.display.update()

        clock.tick(144)
    pygame.quit()
    quit()


pygame.init()
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

display_width = 800
display_height = 600
display = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Snake')

clock = pygame.time.Clock()

start_game()
