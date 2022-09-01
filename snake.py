# Início do Projeto

import pygame

from pygame.locals import *

from sys import exit

pygame.init()

largura = 640
altura = 480

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Jogo')
# criando a janela do jogo.

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

            # loop para seguira atualizando o jogo e criar a função de fechar o jogo.

    pygame.display.update() 
    # atualiza a tela do jogo a cada interação do loop principal.