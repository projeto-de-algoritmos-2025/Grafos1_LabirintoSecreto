from collections import deque

OBSTACLE = 7

class Graph:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.adj_matrix = [[0] * num_vertices for _ in range(num_vertices)]
        self.visited = [False] * num_vertices

    def add_edge(self, v1, v2):
        self.adj_matrix[v1][v2] = 1
        self.adj_matrix[v2][v1] = 1

    def remove_edge(self, v1, v2):
        self.adj_matrix[v1][v2] = 0
        self.adj_matrix[v2][v1] = 0

    def remove_all_edges(self, v):
        for i in range(self.num_vertices):
            self.remove_edge(v, i)

    def clear_visited(self):
        self.visited = [False] * self.num_vertices

    def matrix_to_graph(self, matrix):
        rows, cols = len(matrix), len(matrix[0])
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] != OBSTACLE:
                    current_index = self.coordinates_to_index((i, j), cols)
                    for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                        ni, nj = i + dx, j + dy
                        if 0 <= ni < rows and 0 <= nj < cols and matrix[ni][nj] != OBSTACLE:
                            neighbor_index = self.coordinates_to_index((ni, nj), cols)
                            self.add_edge(current_index, neighbor_index)

    def bfs(self, start, end):
        queue = deque([start])
        visited = [False] * self.num_vertices
        prev = [None] * self.num_vertices
        visited[start] = True

        while queue:
            current = queue.popleft()
            if current == end:
                break
            for neighbor in range(self.num_vertices):
                if self.adj_matrix[current][neighbor] and not visited[neighbor]:
                    queue.append(neighbor)
                    visited[neighbor] = True
                    prev[neighbor] = current

        path = []
        at = end
        while at is not None:
            path.append(at)
            at = prev[at]
        path.reverse()

        return path if path and path[0] == start else None

    def index_to_coordinates(self, index, cols):
        return divmod(index, cols)
    
    def path_to_coordinates(self, path, cols):
        return [self.index_to_coordinates(index, cols) for index in path]

    def coordinates_to_index(self, coordinates, cols):
        row, col = coordinates
        return row * cols + col
    
# Teste de uso

import time
import os

# Tamanho do tabuleiro
rows, cols = 10, 10
board = [[0 for _ in range(cols)] for _ in range(rows)]

# Adiciona obstáculos invisíveis
obstacles = [(3, 3), (3, 4), (4, 4), (5, 4), (6, 4)]
for i, j in obstacles:
    board[i][j] = 7  # invisível

# Posição inicial e final
start_pos = (9, 0)
end_pos = (0, 9)

# Inicializa o grafo e converte a matriz
graph = Graph(rows * cols)
graph.matrix_to_graph(board)

# Converte posições para índices
start_index = graph.coordinates_to_index(start_pos, cols)
end_index = graph.coordinates_to_index(end_pos, cols)

# Encontra o caminho
path = graph.bfs(start_index, end_index)
path_coords = graph.path_to_coordinates(path, cols) if path else []

# Função para imprimir o tabuleiro com o personagem
def print_board(board, char_pos):
    os.system('cls' if os.name == 'nt' else 'clear')
    for i in range(rows):
        for j in range(cols):
            if (i, j) == char_pos:
                print("P", end=" ")  # Personagem
            elif (i, j) == end_pos:
                print("X", end=" ")  # Destino
            elif board[i][j] == 7:
                print(".", end=" ")  # Obstáculo invisível
            else:
                print("_", end=" ")  # Espaço livre
        print()
    time.sleep(0.3)

# Animação da movimentação
if path_coords:
    for coord in path_coords:
        print_board(board, coord)
    print("Chegou ao destino!")
else:
    print("Caminho impossível!")
