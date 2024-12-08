import pygame
import sys
from Herbivoro import Herbivoro  # Importar corretamente a classe Herbivoro

pygame.init()

# Configurações da tela
largura_tela = 800
altura_tela = 600
tela = pygame.display.set_mode((largura_tela, altura_tela))

# Título
pygame.display.set_caption('Ecossistema Marinho')

# Background
imagem_fundo = pygame.image.load("src/img/background.jpg")
imagem_fundo = pygame.transform.scale(imagem_fundo, (largura_tela, altura_tela))

# Criar instância do Herbívoro
peixe = Herbivoro(largura_tela, altura_tela)
peixe2 = Herbivoro(largura_tela, altura_tela)
peixe3 = Herbivoro(largura_tela, altura_tela)
# Variável de execução
executando = True

# Loop principal
while executando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            executando = False

    # Atualizar o movimento e animação do peixe
    peixe.mover()
    peixe.trocar_sprite() 
    peixe2.mover()
    peixe2.trocar_sprite()
    peixe3.mover()
    peixe3.trocar_sprite()

    # Desenhar o fundo e o peixe
    tela.blit(imagem_fundo, (0, 0))
    peixe.desenharNaTela(tela)
    peixe2.desenharNaTela(tela)
    peixe3.desenharNaTela(tela)

    # Atualizar a tela
    pygame.display.flip()

    # Controlar a taxa de quadros por segundo
    pygame.time.Clock().tick(60)

# Encerrar o pygame
pygame.quit()
sys.exit()
