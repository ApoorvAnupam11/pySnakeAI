import pygame
import random
from enum import Enum
from collections import namedtuple

pygame.init()


class Direction(Enum):
    RIGHT = 1
    LEFT = 2
    UP = 3
    DOWN = 4


# fixed name tuple for storing every point
Point = namedtuple("Point", "x_cord", "y_cord")

# fixed blosck size
BLOCK_SIZE = 20


class SnakeGame:
    def __init__(self, width=720, height=640):
        self.width = width
        self.height = height

        # init display
        self.display = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Snake")
        self.clock = pygame.time.Clock()

        # init game state
        self.direction = Direction.RIGHT
        self.snake_head = Point(self.width / 2, self.height / 2)
        self.snake_body = [
            self.snake_head,
            Point(self.snake_head.x_cord - BLOCK_SIZE, self.snake_head.y_cord),
            Point(self.snake_head.x_cord - (2 * BLOCK_SIZE), self.snake_head.y_cord),
        ]

        self.score = 0
        self.food = None
        self.place_food()

    # decide where the food goes
    def place_food(self):
        x = random.randint(0, (self.width - BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE
        y = random.randint(0, (self.height - BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE
        self.food = Point(x, y)
        if self.food in self.snake_body:
            self.place_food()

    def play_step(self):
        #step 1 : collect the user input

        #step 2: move the snake

        #step 3: check if the game is over

        #step 4: place new food or just move

        #step 5: update Pygame UI and the clock

        #step 6: return game over and score
        




if __name__ == "__main__":
    game = SnakeGame()

    # game loop
    while True:
        game.play_step()

        # break if game is over

    pygame.quit()
