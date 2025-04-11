import random
import pygame
from pygame.locals import *

# --- Cores neon para elementos do jogo ---
NEON_WALL = (0, 255, 200)         # ciano neon (paredes, buracos)
NEON_PLAYER = (255, 0, 150)       # magenta neon (jogador)
NEON_PATH = (255, 100, 200)       # magenta mais claro (caminho alternativo)
NEON_GOAL = (0, 255, 150)         # verde-água neon (objetivo)
NEON_TRAP = (255, 0, 100)         # rosa choque neon (armadilha)
NEON_PASSED_TRAP = (255, 200, 0)  # amarelo neon (armadilha passada)

def create_board(rows, cols):
    board = [[0 for _ in range(cols)] for _ in range(rows)]

    # Linha de chegada
    for i in range(2):
        for j in range(cols):
            board[i][j] = 5
            if (i == 0 and j % 2 == 0) or (i == 1 and j % 2 != 0):
                board[i][j] = 3 

    # Última linha com valor 6
    for j in range(cols):
        board[rows - 1][j] = 6

    # Adiciona buracos (valor 1) entre as linhas 2 e a penúltima
    for i in range(2, rows - 1):
        holes = random.sample(range(cols), 2)  # evita buracos na mesma posição
        for j in holes:
            board[i][j] = 1

    return board

def draw_square(row, col, color, screen, square_size, square_margin):
    x = col * (square_size + square_margin) + square_margin
    y = row * (square_size + square_margin) + square_margin
    rect = pygame.Rect(x, y, square_size, square_size)
    pygame.draw.rect(screen, color, rect)

def draw_board(board):
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
                draw_square(row, column, NEON_PLAYER)
            elif tile in tile_colors:
                draw_square(row, column, tile_colors[tile])
