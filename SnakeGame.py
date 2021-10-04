# importar toda a biblioteca do pygame e a biblioteca de gerar números aleatórios
import pygame
from pygame.locals import *
import random

# define uma função para que a maçã sempre seja gerada em pixel com valor inteiro, pra que ela apareça sempre dentro do grid do jogo (cujos valores são sempre inteiros)
def on_grid_random():
    x = random.randrange(0, 590, 10)
    y = random.randrange(0, 590, 10)
    return (x, y)

# define as colisões
def collision (c1, c2):
    return (c1[0] == c2[0]) and (c1[1] == c2[1])

# direções para as quais a cobrinha vai andar
UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3

# inicia o jogo e define uma tela 600x600px
pygame.init()
screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Snake game!")

# cria a cobrinha
snake = [(200, 200), (210, 200), (220, 200)] # direção
snake_skin = pygame.Surface((10, 10)) # tamanho
snake_skin.fill((0, 179, 89)) # cor
direction = RIGHT
# as tuplas são os valores de x e y, e ficam dentro de uma lista pois a cobra é uma lista de segmentos
# aumentar o valor de x significa que a cobrinha está indo pro lado direito; aumentar o valor de y significa que está indo pra baixo

# cria a maçã
apple_pos = on_grid_random() # gera uma posição aleatória nos eixos x e y
apple = pygame.Surface((10, 10)) # tamanho
apple.fill((255, 0, 0)) # cor

# controla a velocidade que serão mostrados os frames
clock = pygame.time.Clock()

game_over = False

# fecha a janela do jogo
while not game_over:
    clock.tick(15)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

# recebe o input do teclado e move a cobrinha
    if event.type == KEYDOWN:
        if event.key == K_UP:
            direction = UP
        if event.key == K_DOWN:
            direction = DOWN
        if event.key == K_LEFT:
            direction = LEFT
        if event.key == K_RIGHT:
            direction = RIGHT

# COLISÕES
# 1) quando a cabeça da cobrinha colide com a maçã, um append a faz aumentar de tamanho
    if collision(snake[0], apple_pos):
        apple_pos = on_grid_random()
        snake.append((0, 0))

# 2) quando a cobra colide com os limites da tela
    if snake[0][0] == 600 or snake[0][1] == 600 or snake[0][0] < 0 or snake[0][1] < 0:
        game_over = True
        break

# 3) quando a cobra colide com ela mesma
    for c in range (1, len(snake) - 1):
        if snake[0][0] == snake[c][0] and snake[0][1] == snake[c][1]:
            game_over = True
            break

# finaliza o jogo
    if game_over:
        break

# rabo da cobra
    for t in range(len(snake) - 1, 0, -1):
        snake[t] = (snake[t - 1][0], snake[t - 1][1])

# define pra onde vai o corpo da cobrinha no eixo cartesiano
    if direction == UP:
        snake[0] = (snake[0][0], snake[0][1] - 10)
    if direction == DOWN:
        snake[0] = (snake[0][0], snake[0][1] + 10)
    if direction == LEFT:
        snake[0] = (snake[0][0] - 10, snake[0][1])
    if direction == RIGHT:
        snake[0] = (snake[0][0] + 10, snake[0][1])


    screen.fill((0, 0, 26)) # pinta a tela de azul marinho
    for pos in snake:
        screen.blit(snake_skin, pos)
        screen.blit(apple, apple_pos)
    pygame.display.update()