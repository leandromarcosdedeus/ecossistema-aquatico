import pygame
import random
import sys
from Herbivoro import Herbivoro
from Planta import Planta
from Carnivoro import Carnivoro

pygame.init()

larguraTela = 800
alturaTela = 600
tela = pygame.display.set_mode((larguraTela, alturaTela))

pygame.display.set_caption('Ecossistema Marinho')

imagemFundo = pygame.image.load("src/img/background.jpg")
imagemFundo = pygame.transform.scale(imagemFundo, (larguraTela, alturaTela))

herbivoros = []
for i in range(random.choice([3, 4, 5, 6, 7])):
    herbivoros.append(Herbivoro(larguraTela, alturaTela))

carnivoros = []
for i in range(random.choice([3, 4, 5, 6, 7])):
    carnivoros.append(Carnivoro(larguraTela, alturaTela))

planta = []
for i in range(10):
    planta.append(Planta(larguraTela, alturaTela))

botaoCor = (0, 128, 255)
botaoHoverCor = (0, 150, 255)
botaoTextoCor = (0, 0, 0)
botaoLargura = 120
botaoAltura = 40
botaoX = 0
botaoY = 0

fonte = pygame.font.Font(None, 36)

def desenharBotao(tela, texto, x, y, largura, altura, cor, textoCor, hover=False):
    if hover:
        cor = botaoHoverCor
    pygame.draw.rect(tela, cor, (x, y, largura, altura))
    textoSurface = fonte.render(texto, True, textoCor)
    textoRect = textoSurface.get_rect(center=(x + largura // 2, y + altura // 2))
    tela.blit(textoSurface, textoRect)

executando = True
fps = 60
tempoClicado = None

tempoUltimaGeracao = pygame.time.get_ticks()

while executando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            executando = False

    mouseX, mouseY = pygame.mouse.get_pos()

    botaoHover = botaoX <= mouseX <= botaoX + botaoLargura and botaoY <= mouseY <= botaoY + botaoAltura

    if evento.type == pygame.MOUSEBUTTONDOWN and botaoHover:
        fps = 120
        tempoClicado = pygame.time.get_ticks()

    if tempoClicado is not None and pygame.time.get_ticks() - tempoClicado >= 5000:
        fps = 60

    tela.fill((0, 0, 0))
    tela.blit(imagemFundo, (0, 0))

    desenharBotao(tela, "Acelerar", botaoX, botaoY, botaoLargura, botaoAltura, botaoCor, botaoTextoCor, botaoHover)

    if pygame.time.get_ticks() - tempoUltimaGeracao >= 10000:
        planta.append(Planta(larguraTela, alturaTela))
        herbivoros.append(Herbivoro(larguraTela, alturaTela))
        carnivoros.append(Carnivoro(larguraTela, alturaTela))
        tempoUltimaGeracao = pygame.time.get_ticks()

    for herb in herbivoros:
        herb.mover()
        herb.trocar_sprite()
        herb.desenharNaTela(tela)
        for pl in planta:
            if herb.verificar_colisao(pl):
                herb.energia += 10
                planta.remove(pl)

    for carn in carnivoros:
        carn.mover()
        carn.trocar_sprite()
        carn.desenharNaTela(tela)
        for herb in herbivoros:
            if carn.verificar_colisao(herb):
                carn.energia += 10
                herbivoros.remove(herb)

    for pl in planta:
        pl.trocar_sprite()
        pl.desenharNaTela(tela)

    for herb in herbivoros:
        herb.energia -= 1
    for carn in carnivoros:
        carn.energia -= 1
    for pl in planta:
        pl.energia -= 1

    pygame.display.flip()

    pygame.time.Clock().tick(fps)

pygame.quit()
sys.exit()
