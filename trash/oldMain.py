import pygame
import sys
import random

# Inicializa o Pygame
pygame.init()

# Configurações da tela
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Ecossistema de Aquario")

# Cores
white = (255, 255, 255)
black = (0, 0, 0)
blue = (0, 0, 255)

square_size = 25  

# Carregar as imagens que você deseja exibir
image_background = pygame.image.load('img/background.png')  # Exemplo de imagem
imagem_peixe1 = pygame.image.load('img/peixe1.png')
imagem_peixe2 = pygame.image.load('img/peixe2.png')
imagem_carn1 = pygame.image.load('img/carn1.png')
imagem_carn2 = pygame.image.load('img/carn2.png')
# Lista de imagens
image_list = [imagem_peixe1, imagem_peixe2, imagem_carn1, imagem_carn2]

# Lista para armazenar os conteúdos (imagens ou quadrados vazios) a serem exibidos
# Preenche a lista com conteúdos aleatórios
square_contents = []
num_rows = screen_height // square_size
num_cols = screen_width // square_size

for row in range(num_rows):
    row_contents = []
    for col in range(num_cols):
        if row == num_rows - 1:  
            row_contents.append(pygame.image.load('img/image.png'))  
        else:
            if random.choice([True, False, False, False, False, False, False, False, False, False, False]):
                row_contents.append(random.choice(image_list))  
            else:
                row_contents.append(image_background)  
    square_contents.append(row_contents)


button_width = 100
# Configurações do botão
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
            
    screen.fill(white)

    for row in range(0, screen_height, square_size):
        for col in range(0, screen_width, square_size):
            rect = pygame.Rect(col, row, square_size, square_size)

            content = square_contents[row // square_size][col // square_size]
            if content is None:  
                pygame.draw.rect(screen, white, rect)  
            else: 
                img_resized = pygame.transform.scale(content, (square_size, square_size))
                screen.blit(img_resized, rect.topleft)  


    # Desenha o botão
    """ pygame.draw.rect(screen, blue, button_rect)  # Preenchimento do botão
    pygame.draw.rect(screen, black, button_rect, 2)  # Borda do botão
 """
    # Atualiza a tela
    pygame.display.flip()

# Encerra o Pygame
pygame.quit()
sys.exit()
