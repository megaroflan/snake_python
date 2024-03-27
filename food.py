from dataclasses import dataclass


@dataclass
class Food:
    x: int
    y: int
    type: str


food_types = ['length+1', 'length-1', 'speed+3', 'speed-3', 'points+3', 'points+5']
food_colors = {'length+1': (255, 0, 0), 'length-1': (255, 255, 0),
               'speed+3': (139, 0, 255), 'speed-3': (255, 192, 203),
               'points+3': (255, 0, 0), 'points+5': (255, 0, 0)}
