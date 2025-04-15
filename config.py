import pygame
from pygame.locals import *

# --- Paleta Neon Futurista ---
background_color = (10, 10, 30)       # fundo escuro
title_color = (0, 255, 200)           # ciano neon
button_color = (255, 0, 150)          # magenta neon
button_hover = (255, 100, 200)        # hover mais claro
text_color = (255, 255, 255)          # branco puro
shadow_color = (50, 50, 50)           # sombra do título

# --- Cores neon para elementos do jogo ---
NEON_WALL = (0, 255, 200)         # ciano neon (paredes, buracos)
NEON_PLAYER = (255, 0, 150)       # magenta neon (jogador)
NEON_PATH = (255, 100, 200)       # magenta mais claro (caminho alternativo)
NEON_GOAL = (0, 255, 150)         # verde-água neon (objetivo)
NEON_TRAP = (255, 0, 100)         # rosa choque neon (armadilha)
NEON_PASSED_TRAP = (255, 200, 0)  # amarelo neon (armadilha passada)

NEON_BACKGROUND = (0, 255, 200)        # Cor padrão do tabuleiro (cinza escuro)
NEON_OBSTACLE = (255, 0, 100)          # Obstáculos (vermelho)
NEON_START = (255, 200, 0)             # Início (verde)
NEON_END = (255, 100, 200)               # Fim (azul)
NEON_PLAYER = (255, 0, 150)            # Jogador (amarelo)
NEON_VISITED = (255, 200, 0)        # Caminho percorrido (azul claro)


# Configurações do tabuleiro
rows = 15
columns = 15

square_size = 50
square_margin = 3

width = (square_size + square_margin) * columns + square_margin
height = (square_size + square_margin) * rows + square_margin
size = width, height

screen = pygame.display.set_mode(size)