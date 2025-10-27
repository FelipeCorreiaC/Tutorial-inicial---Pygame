# ===== Inicialização =====
# ----- Importa e inicia pacotes
import pygame

pygame.init()

# ----- Gera tela principal
window = pygame.display.set_mode((600, 300))
pygame.display.set_caption('Jogo do Felipe')

# ----- Inicia estruturas de dados
game = True

# ===== Loop principal =====
while game:
    # ----- Trata eventos
    for event in pygame.event.get():
        # ----- Verifica consequências
        if event.type == pygame.QUIT:
            game = False
        
        if event.type == pygame.KEYUP:
            game = False

    # ----- Gera saídas
    window.fill((0, 200, 0))  # Preenche com a cor verde
    cor = (255, 240, 0) # Preenche com a cor amarela 
    vertices = [(300, 0), (600, 150), (300, 300), (0, 150)] # Dimensões do poligono, redimensionadas para se adequar a tela
    cor_circulo = (0, 0, 200) #deixa azul, não é 255 pq fica muito claro, 200 fica mais escuro
    pygame.draw.polygon(window, cor, vertices) # Poligono feito
    pygame.draw.circle(window, cor_circulo, (300, 150), 100) # Fazendo circulo (sobreposição)

    # ----- Atualiza estado do jogo
    pygame.display.update()  # Mostra o novo frame para o jogador

# ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados