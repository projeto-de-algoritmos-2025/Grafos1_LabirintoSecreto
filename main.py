import pygame
import sys
from pygame.locals import *
from config import *
import math 
import random
from grafo import Graph 
from busca import bfs_visual, dfs_visual

# --- Configurações iniciais ---
pygame.init()
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Labirinto Secreto")

# --- Configurações do Labirinto ---
CELL_SIZE = 40
ROWS, COLS = 15, 15
MAZE_WIDTH, MAZE_HEIGHT = COLS * CELL_SIZE, ROWS * CELL_SIZE

# Gera matriz do labirinto
board = [[0 for _ in range(COLS)] for _ in range(ROWS)]
for i in range(ROWS):
    for j in range(COLS):
        if random.random() < 0.3:
            board[i][j] = 7
board[0][0] = 0
board[ROWS - 1][COLS - 1] = 0

# Cria grafo
graph = Graph(ROWS * COLS)
graph.matrix_to_graph(board)
start = graph.coordinates_to_index((0, 0), board)
end = graph.coordinates_to_index((ROWS - 1, COLS - 1), board)

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

def generate_solvable_maze(rows, cols, obstacle_prob=0.3):
    # Inicializa o labirinto com paredes (7 = obstáculo)
    maze = [[7 for _ in range(cols)] for _ in range(rows)]
    
    # Cria um caminho aleatório do início (0, 0) ao fim (rows-1, cols-1)
    stack = [(0, 0)]
    maze[0][0] = 0  # Início sempre livre
    
    while stack:
        x, y = stack[-1]
        neighbors = []
        
        # Verifica células vizinhas não visitadas
        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < rows and 0 <= ny < cols and maze[nx][ny] == 7:
                neighbors.append((nx, ny))
        
        if neighbors:
            nx, ny = random.choice(neighbors)
            maze[nx][ny] = 0  # Abre caminho
            stack.append((nx, ny))
            
            # Chegou ao fim? Interrompe
            if (nx, ny) == (rows-1, cols-1):
                break
        else:
            stack.pop()
    
    # Adiciona obstáculos aleatórios, exceto no caminho principal
    for i in range(rows):
        for j in range(cols):
            if maze[i][j] == 7 and random.random() < obstacle_prob:
                maze[i][j] = 7  # Mantém obstáculo
            else:
                maze[i][j] = 0  # Caminho livre
    
    return maze

def run_maze_simulation(algorithm):
    # Configuração do labirinto
    maze_screen = pygame.display.set_mode((MAZE_WIDTH, MAZE_HEIGHT))
    pygame.display.set_caption(f"Labirinto - {algorithm}")

    # Gera um labirinto com caminho garantido
    board = generate_solvable_maze(ROWS, COLS, obstacle_prob=0.3)
    board[0][0] = 0  # Início livre
    board[ROWS-1][COLS-1] = 0  # Fim livre

    # Cria grafo
    graph = Graph(ROWS * COLS)
    graph.matrix_to_graph(board)
    start = graph.coordinates_to_index((0, 0), board)
    end = graph.coordinates_to_index((ROWS - 1, COLS - 1), board)

    # Executa o algoritmo selecionado
    if algorithm == "BFS":
        path = bfs_visual(graph, start, end, 
                        lambda cur, **kwargs: (
                            draw_search_step(cur, kwargs.get("visited", set()), kwargs.get("path", []), board, maze_screen),
                            pygame.time.delay(100)
                        ))
    elif algorithm == "DFS":
        path = dfs_visual(graph, start, end, 
                        lambda cur, **kwargs: (
                            draw_search_step(cur, kwargs.get("visited", set()), kwargs.get("path", []), board, maze_screen),
                            pygame.time.delay(100)
                        ))

    if algorithm == "PLAYER":
        # Posição inicial do jogador (0, 0)
        player_pos = [0, 0]
        running = True
        
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN:
                    # Movimento com teclas de seta
                    if event.key == pygame.K_UP and player_pos[0] > 0 and board[player_pos[0]-1][player_pos[1]] != 7:
                        player_pos[0] -= 1
                    elif event.key == pygame.K_DOWN and player_pos[0] < ROWS-1 and board[player_pos[0]+1][player_pos[1]] != 7:
                        player_pos[0] += 1
                    elif event.key == pygame.K_LEFT and player_pos[1] > 0 and board[player_pos[0]][player_pos[1]-1] != 7:
                        player_pos[1] -= 1
                    elif event.key == pygame.K_RIGHT and player_pos[1] < COLS-1 and board[player_pos[0]][player_pos[1]+1] != 7:
                        player_pos[1] += 1
                    elif event.key == pygame.K_ESCAPE:  # Volta ao menu
                        running = False

            # Verifica se chegou ao final
            if player_pos == [ROWS-1, COLS-1]:
                pygame.time.delay(1000)  # Mostra vitória por 1 segundo
                running = False

            # Desenha o labirinto e o jogador
            screen.fill(NEON_TRAP)
            for i in range(ROWS):
                for j in range(COLS):
                    color = NEON_BACKGROUND if board[i][j] == 0 else NEON_TRAP
                    pygame.draw.rect(screen, color, (j * CELL_SIZE, i * CELL_SIZE, CELL_SIZE, CELL_SIZE))
                    pygame.draw.rect(screen, NEON_GOAL, (j * CELL_SIZE, i * CELL_SIZE, CELL_SIZE, CELL_SIZE), 1)

            # Desenha jogador (círculo verde)
            pygame.draw.circle(screen, NEON_START, 
                              (player_pos[1] * CELL_SIZE + CELL_SIZE//2, player_pos[0] * CELL_SIZE + CELL_SIZE//2),
                              CELL_SIZE//2 - 2)

            # Desenha início e fim
            pygame.draw.rect(screen, NEON_START, (0, 0, CELL_SIZE, CELL_SIZE))
            pygame.draw.rect(screen, NEON_GOAL, ((COLS-1)*CELL_SIZE, (ROWS-1)*CELL_SIZE, CELL_SIZE, CELL_SIZE))

            pygame.display.update()

        pygame.display.set_mode((width, height))  # Volta ao menu
        return

def main_menu():
    clock = pygame.time.Clock()
    
    while True:
        screen.fill(background_color)
        MENU_MOUSE_POS = pygame.mouse.get_pos()

        # Animação do título (pulsando)
        time_ms = pygame.time.get_ticks() / 500
        scale_factor = 1 + 0.05 * math.sin(time_ms)
        base_font_size = 35
        pulsing_size = int(base_font_size * scale_factor)

        title_font = pygame.font.Font("PressStart2P.ttf", pulsing_size)
        title_text = "Labirinto Secreto"

        title_shadow = title_font.render(title_text, True, shadow_color)
        title_rendered = title_font.render(title_text, True, title_color)

        title_rect = title_rendered.get_rect(center=(width / 2, height * 0.2))
        shadow_rect = title_rect.copy()
        shadow_rect.move_ip(4, 4)

        screen.blit(title_shadow, shadow_rect)
        screen.blit(title_rendered, title_rect)

        # --- Configuração dos botões ---
        button_width = 360
        button_height = 60
        button_radius = 12

        button_x = (width - button_width) / 2 

        buttons = [
            {"rect": pygame.Rect(button_x, height / 3, button_width, button_height),
            "text": "Jogar",
            "action": lambda: run_maze_simulation("PLAYER")  # Novo modo!
            },
            {"rect": pygame.Rect(button_x, height / 3 + height * 0.15, button_width, button_height),
            "text": "BFS", 
            "action": lambda: run_maze_simulation("BFS")
            },
            {"rect": pygame.Rect(button_x, height / 3 + height * 0.30, button_width, button_height),
            "text": "DFS", 
            "action": lambda: run_maze_simulation("DFS")
            },
            {"rect": pygame.Rect(button_x, height / 3 + height * 0.45, button_width, button_height),
            "text": "Sair", 
            "action": lambda: sys.exit()
            }
        ]

        for btn in buttons:
            is_hovered = btn["rect"].collidepoint(MENU_MOUSE_POS)
            color = button_hover if is_hovered else button_color

            pygame.draw.rect(screen, color, btn["rect"], border_radius=button_radius)

            btn_font = pygame.font.Font("PressStart2P.ttf", 14)
            btn_text = btn_font.render(btn["text"], True, text_color)
            text_rect = btn_text.get_rect(center=btn["rect"].center)
            screen.blit(btn_text, text_rect)

        # --- Eventos ---
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                for btn in buttons:
                    if btn["rect"].collidepoint(MENU_MOUSE_POS):
                        btn["action"]()

        pygame.display.update()
        clock.tick(60)

main_menu()
pygame.quit()