import pygame
import sys
import random

# Inicializa o Pygame
pygame.init()

# Configurações da tela
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Ecossistema de Fazenda")

# Cores
white = (255, 255, 255)
black = (0, 0, 0)
blue = (0, 0, 255)

# Tamanho dos quadrados
square_size = 25  # Lado de cada quadrado

# Carregar as imagens que você deseja exibir
image_humano = pygame.image.load('img/humano.webp')  # Exemplo de imagem
image_planta = pygame.image.load('img/planta.png')  # Exemplo de imagem
image_animal = pygame.image.load('img/animal.png')  # Exemplo de imagem
image_estranho = pygame.image.load('img/estranho.png')  # Exemplo de imagem

# Lista de imagens
image_list = [image_humano, image_planta, image_estranho]

# Lista para armazenar os conteúdos (imagens ou quadrados vazios) a serem exibidos
square_contents = []

# Preenche a lista com conteúdos aleatórios: imagens ou espaços vazios (brancos)
for row in range(0, screen_height, square_size):
    row_contents = []
    for col in range(0, screen_width, square_size):
        if random.choice([True, False, False, False, False, False, False, False, False, False, False]):  # 50% de chance de ser imagem ou vazio
            row_contents.append(random.choice(image_list))  # Escolhe uma imagem aleatória
        else:
            row_contents.append(None)  # Nenhuma imagem (espaço vazio)
    square_contents.append(row_contents)

# Configurações do botão
button_width = 100
button_height = 40
button_x = 10
button_y = screen_height - 50  # Botão no canto inferior esquerdo
button_rect = pygame.Rect(button_x, button_y, button_width, button_height)

# Loop principal
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Detecta cliques do mouse
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            # Verifica se o clique foi no botão
            if button_rect.collidepoint(mouse_x, mouse_y):
                # Torna o primeiro quadrado humano quando o botão é clicado
                square_contents[0][0] = image_humano  # Altera a imagem do primeiro quadrado

    # Preenche a tela com cor de fundo
    screen.fill(white)

    # Desenha a grade de quadrados com imagens ou vazios
    for row in range(0, screen_height, square_size):
        for col in range(0, screen_width, square_size):
            # Retângulo da posição atual
            rect = pygame.Rect(col, row, square_size, square_size)

            content = square_contents[row // square_size][col // square_size]
            if content is None:  # Se o conteúdo for None, desenha um quadrado vazio (branco)
                pygame.draw.rect(screen, white, rect)  # Preenchimento branco
            else:  # Caso contrário, desenha a imagem
                img_resized = pygame.transform.scale(content, (square_size, square_size))
                screen.blit(img_resized, rect.topleft)  # Desenha a imagem no quadrado

            # Desenha a borda preta
            pygame.draw.rect(screen, black, rect, 1)

    # Desenha o botão
    pygame.draw.rect(screen, blue, button_rect)  # Preenchimento do botão
    pygame.draw.rect(screen, black, button_rect, 2)  # Borda do botão

    # Desenha o texto do botão
    font = pygame.font.Font(None, 24)
    text_surface = font.render("Humano", True, white)
    text_rect = text_surface.get_rect(center=button_rect.center)
    screen.blit(text_surface, text_rect)

    # Atualiza a tela
    pygame.display.flip()

# Encerra o Pygame
pygame.quit()
sys.exit()
