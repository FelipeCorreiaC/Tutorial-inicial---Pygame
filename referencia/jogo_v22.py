# ===== Inicialização =====
# ----- Importa e inicia pacotes
import pygame
import random
from config import WIDTH, HEIGHT, INIT, GAME, QUIT
from init_screen import init_screen
from game_screen import game_screen


pygame.init()
pygame.mixer.init()

# ----- Gera tela principal
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Navinha')


def game_over_screen(window):
    """
    Exibe tela de Game Over.
    Retorna INIT para reiniciar o jogo ou QUIT para encerrar o programa.
    Teclas:
      - R: reiniciar (vai para INIT)
      - Q ou fechar a janela: sair (QUIT)
      - qualquer tecla (opcional): reiniciar também
    """
    clock = pygame.time.Clock()
    font_big = pygame.font.Font(None, 64)
    font_small = pygame.font.Font(None, 26)

    title_surf = font_big.render("GAME OVER", True, (255, 0, 0))
    info_surf = font_small.render("Press R to restart, Q to quit", True, (255, 255, 255))

    title_rect = title_surf.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 30))
    info_rect = info_surf.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 30))

    while True:
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return QUIT
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    return INIT
                if event.key == pygame.K_q:
                    return QUIT
                # opção: qualquer tecla reinicia
                return INIT

        window.fill((0, 0, 0))
        window.blit(title_surf, title_rect)
        window.blit(info_surf, info_rect)
        pygame.display.flip()


state = INIT
while state != QUIT:
    if state == INIT:
        state = init_screen(window)
    elif state == GAME:
        # Executa a tela principal do jogo até ela terminar.
        # (game_screen roda seu loop e retorna quando o jogo acabar)
        game_screen(window)

        # Quando o jogo acabar, mostra Game Over e pega o novo estado
        state = game_over_screen(window)
    else:
        state = QUIT

# ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados