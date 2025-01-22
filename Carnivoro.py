from Animal import Animal  # Certifique-se de que a classe Animal está correta
import pygame, random

class Carnivoro(Animal):  
    def __init__(self, largura_da_tela, altura_da_tela):
        super().__init__()
        # Carregar as imagens de animação
        self.sprites = []
        self.spriteSelector()

        self.largura_da_tela = largura_da_tela
        self.altura_da_tela = altura_da_tela
        #tamanho ideal
        self.tamanho_sprite = 100
        # Tamanho inicial ideal
        self.imagem = pygame.transform.scale(self.sprites[0], (self.tamanho_sprite / 2, self.tamanho_sprite / 2))  # Primeira imagem (sprite_1)

        # Posição inicial aleatória
        self.posicao_x = random.randint(0, self.largura_da_tela - self.imagem.get_width())
        self.posicao_y = random.randint(0, self.altura_da_tela - self.imagem.get_height())
        
        self.tipo = 'Carnivoro'
        self.velocidade = random.choice((1, 1.5, 2))
        self.frame_atual = 0  
        self.tempo_mudanca = 300  
        self.ultimo_tempo = pygame.time.get_ticks()  
        self.energia = 10


    def mover(self):
        self.posicao_x += self.velocidade
        """ if self.energia < 1:
            self.velocidade = 1 """
        if self.posicao_x + self.imagem.get_width() > self.largura_da_tela:
            self.posicao_x = 0
            self.posicao_y += 50
        elif self.posicao_y + self.imagem.get_width() > self.altura_da_tela:
            self.posicao_y = 0

    def trocar_sprite(self):
        # Verificar se é hora de trocar de imagem
        tempo_atual = pygame.time.get_ticks()
        if tempo_atual - self.ultimo_tempo >= self.tempo_mudanca:
            self.frame_atual += 1
            if self.frame_atual >= len(self.sprites):
                self.frame_atual = 0  # Voltar ao primeiro sprite

            # Redimensionando a imagem para metade do tamanho original
            largura_original = self.tamanho_sprite
            altura_original = self.tamanho_sprite
            self.imagem = pygame.transform.scale(self.sprites[self.frame_atual], (largura_original // 2, altura_original // 2))
            self.ultimo_tempo = tempo_atual  # Atualizar o tempo

    def desenharNaTela(self, tela):
        tela.blit(self.imagem, (self.posicao_x, self.posicao_y))

    def spriteSelector(self):
        randomC = random.choice([1, 2, 3, 4, 5])  
        animal = ''
        if randomC == 1:
            animal = 'Tubarao'
        elif randomC == 2:
            animal = 'Tubarao'
        elif randomC == 3:
            animal = 'Tubarao'
        elif randomC == 4:
            animal = 'Tubarao'
        elif randomC == 5:
            animal = 'Tubarao'
        
        for i in range(0, 4):  
            self.sprites.append(pygame.image.load(f'src/img/{animal}/sprite_{i + 1}.png'))

    def verificar_colisao(self, herbivoro):
        distancia = ((self.posicao_x - herbivoro.posicao_x) ** 2 + (self.posicao_y - herbivoro.posicao_y) ** 2) ** 0.5
        return distancia < 25 