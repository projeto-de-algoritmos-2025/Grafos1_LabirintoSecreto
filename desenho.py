import pygame
from config import *
import random
from grafo import Graph 
from busca import bfs_visual, dfs_visual

CELL_SIZE = 40
ROWS, COLS = 15, 15
WIDTH, HEIGHT = COLS * CELL_SIZE, ROWS * CELL_SIZE

def draw_search_step(current, visited, path, matrix, screen):
    screen.fill(NEON_TRAP)
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            color = NEON_BACKGROUND
            if matrix[i][j] == 7:
                color = NEON_TRAP
            pygame.draw.rect(screen, color, (j * CELL_SIZE, i * CELL_SIZE, CELL_SIZE, CELL_SIZE))
            pygame.draw.rect(screen, NEON_GOAL, (j * CELL_SIZE, i * CELL_SIZE, CELL_SIZE, CELL_SIZE), 1)

    for v in visited:
        x, y = graph.index_to_coordinates(v, matrix)
        pygame.draw.rect(screen, NEON_PATH, (y * CELL_SIZE, x * CELL_SIZE, CELL_SIZE, CELL_SIZE))

    for p in path:
        x, y = graph.index_to_coordinates(p, matrix)
        pygame.draw.rect(screen, NEON_PASSED_TRAP, (y * CELL_SIZE, x * CELL_SIZE, CELL_SIZE, CELL_SIZE))

    x, y = graph.index_to_coordinates(current, matrix)
    pygame.draw.rect(screen, NEON_VISITED, (y * CELL_SIZE, x * CELL_SIZE, CELL_SIZE, CELL_SIZE))

    # Marcar início e fim
    sx, sy = graph.index_to_coordinates(start, matrix)
    ex, ey = graph.index_to_coordinates(end, matrix)
    pygame.draw.rect(screen, NEON_START, (sy * CELL_SIZE, sx * CELL_SIZE, CELL_SIZE, CELL_SIZE))
    pygame.draw.rect(screen, background_color, (ey * CELL_SIZE, ex * CELL_SIZE, CELL_SIZE, CELL_SIZE))

    pygame.display.update()

# ----- MAIN -----
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Labirinto - Busca Visual")

# Gera matriz estilo labirinto simples
board = [[0 for _ in range(COLS)] for _ in range(ROWS)]
for i in range(ROWS):
    for j in range(COLS):
        if random.random() < 0.3:
            board[i][j] = 7
board[0][0] = 0
board[ROWS - 1][COLS - 1] = 0

graph = Graph(ROWS * COLS)
graph.matrix_to_graph(board)
start = graph.coordinates_to_index((0, 0), board)
end = graph.coordinates_to_index((ROWS - 1, COLS - 1), board)

# Loop do jogo
running = True
path = []
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_b:
                path = bfs_visual(graph, start, end, lambda cur, **kwargs: draw_search_step(cur, kwargs.get("visited", set()), kwargs.get("path", []), board, screen))
            if event.key == pygame.K_d:
                path = dfs_visual(graph, start, end, lambda cur, **kwargs: draw_search_step(cur, kwargs.get("visited", set()), kwargs.get("path", []), board, screen))

    pygame.display.update()

pygame.quit()
