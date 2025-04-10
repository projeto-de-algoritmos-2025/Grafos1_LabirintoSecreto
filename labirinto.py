import pygame
import sys
from pygame.locals import *
from config import *
import math 

pygame.init()

# --- Configurações iniciais ---
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Labirinto Secreto")

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

        # --- Configuração visual dos botões ---
        button_width = 360
        button_height = 60
        button_radius = 12

        button_x = (width - button_width) / 2 

        buttons = [
            {"rect": pygame.Rect(button_x, height / 3, button_width, button_height),
            "text": "Jogar",
            "action": lambda: print("Jogar")
            },

            {"rect": pygame.Rect(button_x, height / 3 + height * 0.15, button_width, button_height),
            "text": "Máquina vs Máquina", 
            "action": lambda: print("Máquina vs Máquina")
            },

            {"rect": pygame.Rect(button_x, height / 3 + height * 0.30, button_width, button_height),
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
