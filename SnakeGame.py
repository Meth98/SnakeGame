#####################################################################################
## Description: Script that uses the Pygame library to create a simple snake game
##
## Author: Matteo Z.
#####################################################################################

import pygame, random

class Snake:
    def __init__(self):
        self.length = 1
        self.positions = [((WIDTH / 2), (HEIGHT / 2))]
        self.direction = random.choice([UP, DOWN, LEFT, RIGHT])
        self.color = RED

    def get_head_position(self):
        return self.positions[0]

    def move(self):
        cur = self.get_head_position()
        x, y = self.direction
        new = (((cur[0] + (x * GRID_SIZE)) % WIDTH), (cur[1] + (y * GRID_SIZE)) % HEIGHT)

        if len(self.positions) > 2 and new in self.positions[2:]:
            self.reset()
        else:
            self.positions.insert(0, new)

            if len(self.positions) > self.length:
                self.positions.pop()

    def reset(self):
        self.length = 1
        self.positions = [((WIDTH / 2), (HEIGHT / 2))]
        self.direction = random.choice([UP, DOWN, LEFT, RIGHT])

    def draw(self, surface):
        for p in self.positions:
            pygame.draw.rect(surface, self.color, (p[0], p[1], GRID_SIZE, GRID_SIZE))

    def handle_keys(self, keys):
        if keys[pygame.K_UP]:
            self.direction = UP
        elif keys[pygame.K_DOWN]:
            self.direction = DOWN
        elif keys[pygame.K_LEFT]:
            self.direction = LEFT
        elif keys[pygame.K_RIGHT]:
            self.direction = RIGHT


def draw_grid(surface):
    for y in range(0, HEIGHT, GRID_SIZE):
        for x in range(0, WIDTH, GRID_SIZE):
            pygame.draw.rect(surface, WHITE, (x, y, GRID_SIZE, GRID_SIZE), 1)


########## MAIN ##########

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 600, 400
FPS = 10
GRID_SIZE = 20
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Create the window
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")
clock = pygame.time.Clock()

UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

snake = Snake()
food = ((random.randint(0, WIDTH // GRID_SIZE - 1) * GRID_SIZE), (random.randint(0, HEIGHT // GRID_SIZE - 1) * GRID_SIZE))
running = True

while running:
    keys = pygame.key.get_pressed()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    snake.handle_keys(keys)
    snake.move()

    if snake.get_head_position() == food:
        snake.length += 1
        food = ((random.randint(0, WIDTH // GRID_SIZE - 1) * GRID_SIZE), (random.randint(0, HEIGHT // GRID_SIZE - 1) * GRID_SIZE))

    win.fill((0, 0, 0))
    draw_grid(win)
    snake.draw(win)
    pygame.draw.rect(win, RED, (food[0], food[1], GRID_SIZE, GRID_SIZE))
    pygame.display.update()
    clock.tick(FPS)

pygame.quit()