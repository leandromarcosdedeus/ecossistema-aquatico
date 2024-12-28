import pygame, random
import sys
from Herbivoro import Herbivoro  # Importar corretamente a classe Herbivoro
from Planta import Planta
from Carnivoro import Carnivoro
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
herbivoros = []
for i in range(random.choice([3,4,5,6, 7])):
    herbivoros.append(Herbivoro(largura_tela, altura_tela))


# Criar instância do Carnivoros
carnivoros = []
for i in range(random.choice([3,4,5,6, 7])):
    carnivoros.append(Carnivoro(largura_tela, altura_tela))

planta = []
for i in range(10):
    planta.append(Planta(largura_tela, altura_tela))

# Variável de execução
executando = True

# Loop principal
while executando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            executando = False

    # Atualizar o movimento e animação do peixe
    for herb in herbivoros:
        herb.mover()
        herb.trocar_sprite()
        herb.desenharNaTela(tela)
        for pl in planta:
                if herb.verificar_colisao(pl):
                    herb.energia += 10
                    planta.remove(pl)

    for herb in carnivoros:
        herb.mover()
        herb.trocar_sprite()
        herb.desenharNaTela(tela)
        for pl in herbivoros:
                if herb.verificar_colisao(pl):
                    herb.energia += 10
                    herbivoros.remove(pl)

    tela.blit(imagem_fundo, (0, 0))


    for herb in herbivoros:

        herb.desenharNaTela(tela)

    for herb in carnivoros:

        herb.desenharNaTela(tela)
    #gerando as plantas
    for i in range(len(planta)):
        planta[i].trocar_sprite()
        planta[i].desenharNaTela(tela)


    
    # Atualizar a tela
    pygame.display.flip()

    # Controlar a taxa de quadros por segundo
    pygame.time.Clock().tick(60)

# Encerrar o pygame
pygame.quit()
sys.exit()
