import pygame, random

# Configurações básicas
pygame.init()
tela = pygame.display.set_mode((400, 300))
relogio = pygame.time.Clock()

# Animal
tamanho_casa = 100
animal = pygame.Rect(200, 150, tamanho_casa, tamanho_casa)  

cor_animal = (255, 0, 0)

# Loop principal
rodando = True
while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

    # Movimento aleatório: apenas uma "casa"
    dx, dy = random.choice([(0, -1), (0, 1), (-1, 0), (1, 0)])  # Cima, baixo, esquerda, direita
    animal.x += dx * tamanho_casa
    animal.y += dy * tamanho_casa

    # Limitar dentro da tela
    animal.x = max(0, min(400 - tamanho_casa, animal.x))
    animal.y = max(0, min(300 - tamanho_casa, animal.y))

    # Atualizar tela
    tela.fill((0, 0, 0))  # Fundo preto
    pygame.draw.rect(tela, cor_animal, animal)
    pygame.display.flip()

    relogio.tick(1 )  # Atualizações por segundo

pygame.quit()
