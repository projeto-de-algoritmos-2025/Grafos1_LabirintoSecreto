import pygame
from collections import deque

def bfs_visual(graph, start, end, draw_func):
    queue = deque()
    queue.append((start, [start]))
    visited = set([start])

    while queue:
        current, path = queue.popleft()
        draw_func(current, visited=visited, path=path)
        pygame.time.delay(100)

        if current == end:
            return path

        for neighbor in range(graph.num_vertices):
            if graph.adj_matrix[current][neighbor] == 1 and neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, path + [neighbor]))
    return None

def dfs_visual(graph, start, end, draw_func):
    stack = [(start, [start])]
    visited = set()

    while stack:
        current, path = stack.pop()
        if current in visited:
            continue

        visited.add(current)
        draw_func(current, visited=visited, path=path)
        pygame.time.delay(100)

        if current == end:
            return path

        for neighbor in range(graph.num_vertices):
            if graph.adj_matrix[current][neighbor] == 1 and neighbor not in visited:
                stack.append((neighbor, path + [neighbor]))
    return None
