import pygame

#inicializa
pygame.init()

tamanho_tela = (800, 800)
tela = pygame.display.set_mode(tamanho_tela)
pygame.display.set_caption('Oceano')    

tamanho_peixe = 15
#criando um arquivo do pygame que vai ser desenhado na tela dps
peixe = pygame.Rect(0, 0, tamanho_peixe, tamanho_peixe)
tamanho_planta = 100

qtd_blocos_linha = 8
qtd_linhas_blocos = 5
qtd_total = qtd_blocos_linha * qtd_linhas_blocos

#cria as funcoes
#desenha na tela
#cria loop infinito