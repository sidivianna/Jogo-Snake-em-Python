# Movendo objetos na tela

import pygame
from pygame.locals import *
from sys import exit
from random import randint

pygame.init()

LARGURA = 640
ALTURA = 480
x = LARGURA/2 
y = ALTURA/2

X_AZUL = randint(40, 600)
Y_AZUL = randint(50, 430)
# define posições randomizadas para o retângulo azul na tela.

tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption('SNAKE')
relogio = pygame.time.Clock() 

while True:
    relogio.tick(30) 
    tela.fill((0,0,0)) 
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

    if pygame.key.get_pressed()[K_RIGHT]:
        x = x + 20
    if pygame.key.get_pressed()[K_LEFT]:
        x = x - 20
    if pygame.key.get_pressed()[K_UP]:
        y = y - 20
    if pygame.key.get_pressed()[K_DOWN]:
        y = y + 20

    RET_VERMELHO = pygame.draw.rect(tela, (255,0,0), (x,y,40,50))
    RET_AZUL = pygame.draw.rect(tela, (0,0,255), (X_AZUL,Y_AZUL,40,50))
    # define os dois retangulos como variáveis
    
    if RET_VERMELHO.colliderect(RET_AZUL):
        X_AZUL = randint(40, 600)
        Y_AZUL = randint(50, 430)
        # cria a função colisão e faz com que sempre que haja colisão o trinagulo azul mude de posição.

        

    pygame.draw.rect(tela, (255,0,0), (x,y,40,50))
   
    pygame.display.update() 
 