from dataclasses import dataclass
import pygame


@dataclass
class Snake:
    head_x: int
    head_y: int
    x_delta: int = 0
    y_delta: int = 0
    snake_len: int = 1
    add_score: int = 0
    fps: int = 15

    def eat_food(self, food_type: str):
        eat_sound = pygame.mixer.Sound('eat.mp3')
        eat_sound.set_volume(0.25)
        eat_sound.play()
        match food_type:
            case 'length+1':
                self.snake_len += 1
            case 'length-1':
                self.snake_len -= 1
            case 'speed+3':
                if self.fps != 60:
                    self.fps += 3
                self.snake_len += 1
            case 'speed-3':
                if self.fps != 3:
                    self.fps -= 3
                self.snake_len += 1
            case 'points+3':
                self.add_score += 2
                self.snake_len += 1
            case 'points+5':
                self.add_score += 4
                self.snake_len += 1

    def change_direction(self, key):
        snake_speed = 20
        match key:
            case pygame.K_LEFT:
                if (self.x_delta, self.y_delta) != (snake_speed, 0):
                    self.x_delta, self.y_delta = (-snake_speed, 0)
            case pygame.K_RIGHT:
                if (self.x_delta, self.y_delta) != (-snake_speed, 0):
                    self.x_delta, self.y_delta = (snake_speed, 0)
            case pygame.K_UP:
                if (self.x_delta, self.y_delta) != (0, snake_speed):
                    self.x_delta, self.y_delta = (0, -snake_speed)
            case pygame.K_DOWN:
                if (self.x_delta, self.y_delta) != (0, -snake_speed):
                    self.x_delta, self.y_delta = (0, snake_speed)
