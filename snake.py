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

        # definidas as funções de movimentos para os botões.

    pygame.draw.rect(tela, (255,0,0), (x,y,40,50))
   
    pygame.display.update() 
 