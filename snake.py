# Movendo objetos na tela

import pygame

from pygame.locals import *

from sys import exit

pygame.init()

LARGURA = 640
ALTURA = 480
x = LARGURA/2 # posição do obejto na tela
y = 0

tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption('SNAKE')
relogio = pygame.time.Clock() # controla a taxa de atualização do jogo


while True:
    relogio.tick(30) # framerate
    tela.fill((0,0,0)) # atualiza a tela de preto depois que obejeto passa.
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

    pygame.draw.rect(tela, (255,0,0), (x,y,40,50))

    if y >= ALTURA:
        y = 0
    y = y + 1
    # faz o retângulo sempre reiniciar quando chegar no fim da tela
  
   
    pygame.display.update() 
 