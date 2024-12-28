from Animal import Animal  # Certifique-se de que a classe Animal está correta
import pygame, random

class Planta(Animal):  
    def __init__(self, largura_da_tela, altura_da_tela):
        super().__init__()
        # Carregar as imagens de animação
        self.sprites = []
        self.spriteSelector()
        self.randomW = random.choice([0, 1, 2])

        self.largura_da_tela = largura_da_tela
        self.altura_da_tela = altura_da_tela
        #tamanho ideal
        self.tamanho_sprite = 100
        # Tamanho inicial ideal
        self.imagem = pygame.transform.scale(self.sprites[0], (self.tamanho_sprite / 2, self.tamanho_sprite / 2))  # Primeira imagem (sprite_1)

        # Posição inicial aleatória
        self.posicao_x = random.randint(0, 800)
        self.posicao_y = random.randint(400, 550)
        
        
        self.tipo = 'Herbivoro'
        self.velocidade = random.choice((1, 1.5, 2))
        self.frame_atual = 0  # Índice do quadro atual da animação
        self.tempo_mudanca = 600  # Tempo para trocar de imagem (em milissegundos)
        self.ultimo_tempo = pygame.time.get_ticks()  # Marca o tempo atual
        self.energia = 1000


        self.posicao_x += self.velocidade
        if self.energia < 500:
            self.velocidade = 1
        if self.posicao_x + self.imagem.get_width() > self.largura_da_tela:
            self.posicao_x = 0
            self.posicao_y += 50
        elif self.posicao_y + self.imagem.get_width() > self.altura_da_tela:
            self.posicao_y = 0
        self.energia = self.energia - 1

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
            self.imagem = pygame.transform.scale(self.sprites[self.frame_atual], (largura_original / 2, altura_original/2 ))
            self.ultimo_tempo = tempo_atual  # Atualizar o tempo

    def desenharNaTela(self, tela):
        if self.randomW == 0:
            tela.blit(self.imagem, (self.posicao_x, self.posicao_y))
            tela.blit(self.imagem, (self.posicao_x + 20, self.posicao_y))  
        elif self.randomW == 1:
            tela.blit(self.imagem, (self.posicao_x, self.posicao_y))
            tela.blit(self.imagem, (self.posicao_x + 20, self.posicao_y))
            tela.blit(self.imagem, (self.posicao_x + 40, self.posicao_y))
        elif self.randomW == 2:
            tela.blit(self.imagem, (self.posicao_x, self.posicao_y))
            tela.blit(self.imagem, (self.posicao_x + 20, self.posicao_y))
            tela.blit(self.imagem, (self.posicao_x + 40, self.posicao_y))
            tela.blit(self.imagem, (self.posicao_x + 60, self.posicao_y))

    def spriteSelector(self):
        randomC = random.choice([1, 2])  
        alg = random.choice([8, 12, 16, 20])  

        animal = ''
        if randomC == 1:
            animal = 'Alga Marinha'
        elif randomC == 2:
            animal = 'Alga Marinha'

    
        for i in range(0, 4):  
            self.sprites.append(pygame.image.load(f'src/img/{animal}/sprite_{i + 1 + alg}.png'))
