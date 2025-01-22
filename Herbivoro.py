from Animal import Animal  # Certifique-se de que a classe Animal está correta
import pygame, random

class Herbivoro(Animal):  
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
        self.frente = 0
        # Posição inicial aleatória
        self.posicao_x = random.randint(0, self.largura_da_tela - self.imagem.get_width())
        self.posicao_y = random.randint(0, self.altura_da_tela - self.imagem.get_height())
        
        self.tipo = 'Herbivoro'
        self.velocidade = random.choice((1, 1.5, 2))
        self.frame_atual = 0  # Índice do quadro atual da animação
        self.tempo_mudanca = 300  # Tempo para trocar de imagem (em milissegundos)
        self.ultimo_tempo = pygame.time.get_ticks()  # Marca o tempo atual
        self.energia = 1000

    def mover(self):
        # Atualizar a posição horizontal
        if self.frente == 0:
            self.posicao_x += self.velocidade
        else:
            self.posicao_x -= self.velocidade

        # Verificar se atingiu a borda horizontal
        if self.posicao_x + self.imagem.get_width() > self.largura_da_tela:
            self.posicao_x = self.largura_da_tela - self.imagem.get_width()  # Corrigir posição
            # Aleatoriamente decidir mover para cima ou para baixo e mudar direção
            self.posicao_y += 50 if random.choice([True, False]) else -50
            self.frente = 1  # Mudar direção para trás
        elif self.posicao_x < 0:
            self.posicao_x = 0  # Corrigir posição
            # Aleatoriamente decidir mover para cima ou para baixo e mudar direção
            self.posicao_y += 50 if random.choice([True, False]) else -50
            self.frente = 0  # Mudar direção para frente

        # Garantir que o herbívoro não ultrapasse os limites verticais
        if self.posicao_y < 0:
            self.posicao_y = 0
        elif self.posicao_y + self.imagem.get_height() > self.altura_da_tela:
            self.posicao_y = self.altura_da_tela - self.imagem.get_height()


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
            animal = 'Peixe2'
        elif randomC == 2:
            animal = 'Peixe1'
        elif randomC == 3:
            animal = 'Peixe2'
        elif randomC == 4:
            animal = 'Agua Viva'
        elif randomC == 5:
            animal = 'Peixe3'
        
        for i in range(0, 4):  
            self.sprites.append(pygame.image.load(f'src/img/{animal}/sprite_{i + 1}.png'))

    def verificar_colisao(self, planta):
        distancia = ((self.posicao_x - planta.posicao_x) ** 2 + (self.posicao_y - planta.posicao_y) ** 2) ** 0.5
        return distancia < 25 