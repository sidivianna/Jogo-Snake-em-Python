# Criar cobra, maça e corpo da cobra aumentar.

import pygame
from pygame.locals import *
from sys import exit
from random import randint

pygame.init()

pygame.mixer.music.set_volume(0.1)
musica_de_fundo = pygame.mixer.music.load('sons/01.mp3')
barulho_colisao = pygame.mixer.Sound('sons/smw_coin.wav')
pygame.mixer.music.play(-1)


LARGURA = 640
ALTURA = 480
x_cobra = LARGURA/2 
y_cobra = ALTURA/2

x_maca = randint(40, 600)
y_maca = randint(50, 430)

pontos = 0
fonte = pygame.font.SysFont('arial', 40, bold=True, italic=True)

tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption('SNAKE')
relogio = pygame.time.Clock() 
lista_cobra = []

def aumenta_cobra(lista_cobra):
    for XeY in lista_cobra:
        pygame.draw.rect(tela, (0,255,0),(XeY[0],XeY[1],20,20))
        # função que desenha o corpo da cobra.

while True:
    relogio.tick(30) 
    tela.fill((0,0,0)) # cor da tela
    mensagem = f'Pontos:{pontos}'
    texto_formatado = fonte.render(mensagem, False, (255, 255, 255))
    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

    if pygame.key.get_pressed()[K_RIGHT]:
        x_cobra = x_cobra + 20
    if pygame.key.get_pressed()[K_LEFT]:
        x_cobra = x_cobra - 20
    if pygame.key.get_pressed()[K_UP]:
        y_cobra = y_cobra - 20
    if pygame.key.get_pressed()[K_DOWN]:
        y_cobra = y_cobra + 20

    cobra = pygame.draw.rect(tela, (0,255,0), (x_cobra,y_cobra,20,20))
    maca = pygame.draw.rect(tela, (255,0,0), (x_maca,y_maca,20,20))
    
    if cobra.colliderect(maca):
        x_maca = randint(40, 600)
        y_maca = randint(50, 430)
        pontos += 1
        barulho_colisao.play()

    lista_cabeca = []   
    lista_cabeca.append(x_cobra)
    lista_cabeca.append(y_cobra)
    lista_cobra.append(lista_cabeca)
    #lista para armazenar a posição da cabeça da cobra.

    aumenta_cobra(lista_cobra)
    # Chama a função do corpo da cobra crescer
 
    tela.blit(texto_formatado, (450, 40)) 

    pygame.display.update() 
 



