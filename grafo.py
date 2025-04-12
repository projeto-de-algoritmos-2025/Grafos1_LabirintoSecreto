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
    

