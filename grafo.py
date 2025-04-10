from collections import deque

class Graph:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.adj_matrix = [[0] * num_vertices for _ in range(num_vertices)]
        self.visited = [False] * num_vertices

    def add_edge(self, v1, v2):
        self.adj_matrix[v1][v2] = 1
        self.adj_matrix[v2][v1] = 1

    def clear_visited(self):
        self.visited = [False] * self.num_vertices

    def matrix_to_graph(self, matrix):
        rows, cols = len(matrix), len(matrix[0])
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] != 7:  # 7 é obstáculo
                    index = self.coordinates_to_index((i, j), cols)
                    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
                    for dx, dy in directions:
                        ni, nj = i + dx, j + dy
                        if 0 <= ni < rows and 0 <= nj < cols and matrix[ni][nj] != 7:
                            neighbor_index = self.coordinates_to_index((ni, nj), cols)
                            self.add_edge(index, neighbor_index)

    def dfs(self, start, end):
        self.visited[start] = True
        if start == end:
            return [start]
        for v in range(self.num_vertices):
            if self.adj_matrix[start][v] == 1 and not self.visited[v]:
                path = self.dfs(v, end)
                if path:
                    return [start] + path
        return None

    def bfs(self, start, end):
        queue = deque()
        queue.append(start)
        visited = [False] * self.num_vertices
        prev = [None] * self.num_vertices

        visited[start] = True

        while queue:
            current = queue.popleft()
            if current == end:
                break
            for neighbor in range(self.num_vertices):
                if self.adj_matrix[current][neighbor] == 1 and not visited[neighbor]:
                    queue.append(neighbor)
                    visited[neighbor] = True
                    prev[neighbor] = current

        path = []
        at = end
        while at is not None:
            path.append(at)
            at = prev[at]
        path.reverse()

        if path and path[0] == start:
            return path
        return None

    def coordinates_to_index(self, coordinates, cols):
        row, col = coordinates
        return row * cols + col

    def index_to_coordinates(self, index, cols):
        return divmod(index, cols)

    def path_to_coordinates(self, path, cols):
        return [self.index_to_coordinates(i, cols) for i in path]

# Criação do tabuleiro
def create_board(rows, cols):
    board = []
    for i in range(rows):
        row = []
        for j in range(cols):
            if i < 2:  # linha de chegada
                row.append(5)
                if (i == 0 and j % 2 == 0) or (i == 1 and j % 2 != 0):
                    row[j] = 3
            elif i == rows - 1:  # linha de partida
                row.append(6)
            else:
                row.append(0)
        board.append(row)
    return board

# Adiciona obstáculos no tabuleiro
def add_obstacles(board, obstacle_coords):
    for r, c in obstacle_coords:
        board[r][c] = 7

# Exibe o caminho no terminal
def print_path(label, path, graph, cols):
    if path:
        coords = graph.path_to_coordinates(path, cols)
        print(f"{label} Path (índices): {path}")
        print(f"{label} Path (coordenadas): {coords}")
    else:
        print(f"{label} Path: Nenhum caminho encontrado.")

# === Código principal de teste ===
if __name__ == "__main__":
    rows, cols = 15, 15
    board = create_board(rows, cols)

    # Obstáculos de exemplo
    obstacles = [(10, 7), (11, 7), (12, 7), (13, 7), (9, 7), (9, 6)]
    add_obstacles(board, obstacles)

    graph = Graph(rows * cols)
    graph.matrix_to_graph(board)

    # Ponto inicial (linha de partida) e final (linha de chegada)
    start_coord = (14, 0)
    end_coord = (0, 2)
    start_index = graph.coordinates_to_index(start_coord, cols)
    end_index = graph.coordinates_to_index(end_coord, cols)

    # Executa DFS
    graph.clear_visited()
    dfs_path = graph.dfs(start_index, end_index)
    print_path("DFS", dfs_path, graph, cols)

    # Executa BFS
    bfs_path = graph.bfs(start_index, end_index)
    print_path("BFS", bfs_path, graph, cols)
