import pygame
from grafo import Graph  
from config import *  
from tabuleiro import create_board, draw_board, animate_path 

pygame.init()

rows, cols = 10, 10
square_size = 40
square_margin = 2
screen_width = cols * (square_size + square_margin) + square_margin
screen_height = rows * (square_size + square_margin) + square_margin
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Labirinto Secreto")

# Dados iniciais
start_pos = (9, 0)
end_pos = (0, 9)
obstacles = [(3, 3), (3, 4), (4, 4), (5, 4), (6, 4)]
board = create_board(rows, cols, obstacles, start_pos, end_pos)

# Busca caminho
graph = Graph(rows * cols)
graph.matrix_to_graph(board)
start_index = graph.coordinates_to_index(start_pos, cols)
end_index = graph.coordinates_to_index(end_pos, cols)
path = graph.bfs(start_index, end_index)
path_coords = graph.path_to_coordinates(path, cols) if path else []

# Loop principal
running = True
while running:
    screen.fill((0, 0, 0))
    draw_board(board, screen, square_size, square_margin)
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

    if path_coords:
        animate_path(screen, board, path_coords, square_size, square_margin)
        print("Chegou ao destino!")
    else:
        print("Caminho impossível!")

    pygame.time.wait(2000)
    running = False

pygame.quit()
