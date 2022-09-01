# Desenhando objetos na tela

import pygame

from pygame.locals import *

from sys import exit

pygame.init()

LARGURA = 640
ALTURA = 480

tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption('SNAKE')


while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

    pygame.draw.rect(tela, (255,0,0), (200,300,100,100))
    pygame.draw.circle(tela, (0,0,255), (300,260),50)
    pygame.draw.line(tela, (255,255,0), (390,0),(390,600), 20)
        # criada a funcao para: 'desenhar' na tela;
        # cor (rgb); 
        # posiçês orientadas nos eixos x e y;
        # comprimento do retangulo;


           
    pygame.display.update() 
 