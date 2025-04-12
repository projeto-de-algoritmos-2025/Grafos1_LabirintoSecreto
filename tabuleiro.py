import random
import pygame
from pygame.locals import *
from config import *

def create_board(rows, cols, obstacles, start_pos, end_pos):
    board = [[0 for _ in range(cols)] for _ in range(rows)]

    for i in range(2):
        for j in range(cols):
            board[i][j] = 5
            if (i == 0 and j % 2 == 0) or (i == 1 and j % 2 != 0):
                board[i][j] = 3 

    for j in range(cols):
        board[rows - 1][j] = 6

    for i in range(2, rows - 1):
        holes = random.sample(range(cols), 2)
        for j in holes:
            board[i][j] = 1

    for i, j in obstacles:
        board[i][j] = 7

    return board


def draw_square(row, col, color, screen, square_size, square_margin):
    x = col * (square_size + square_margin) + square_margin
    y = row * (square_size + square_margin) + square_margin
    rect = pygame.Rect(x, y, square_size, square_size)
    pygame.draw.rect(screen, color, rect)

def draw_board(board, screen, square_size, square_margin):
    tile_colors = {
        0: NEON_WALL,
        1: NEON_WALL,
        4: NEON_PATH,
        5: NEON_GOAL,
        6: NEON_TRAP,
        7: NEON_PASSED_TRAP
    }

    for row in range(len(board)):
        for column in range(len(board[0])):
            tile = board[row][column]

            if tile == 2:  # posição do jogador
                draw_square(row, column, NEON_PLAYER, screen, square_size, square_margin)
            elif tile in tile_colors:
                draw_square(row, column, tile_colors[tile], screen, square_size, square_margin)

def animate_path(screen, board, path_coords, square_size, square_margin, delay=300):
    clock = pygame.time.Clock()
    for (i, j) in path_coords:
        screen.fill((0, 0, 0))
        temp_board = [row.copy() for row in board]
        temp_board[i][j] = 2  # jogador na posição atual
        draw_board(temp_board, screen, square_size, square_margin)
        pygame.display.flip()
        pygame.time.delay(delay)
        clock.tick(60)

