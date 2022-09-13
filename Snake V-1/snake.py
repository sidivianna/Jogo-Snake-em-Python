# 

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

velocidade = 10
x_controle = velocidade
y_controle = 0

x_maca = randint(40, 600)
y_maca = randint(50, 430)

pontos = 0
fonte = pygame.font.SysFont('arial', 40, bold=True, italic=True)

tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption('SNAKE')
relogio = pygame.time.Clock() 
lista_cobra = []
comprimento_inicial = 5

def aumenta_cobra(lista_cobra):
    for XeY in lista_cobra:
        pygame.draw.rect(tela, (0,255,0),(XeY[0],XeY[1],20,20))
        
while True:
    relogio.tick(30) 
    tela.fill((0,0,0)) 
    mensagem = f'Pontos:{pontos}'
    texto_formatado = fonte.render(mensagem, False, (255, 255, 255))
    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

        if event.type == KEYDOWN:
            if event.key == K_LEFT:
                if x_controle == velocidade:
                    pass
                else:
                    x_controle = -velocidade
                    y_controle = 0

            if event.key == K_RIGHT:
                if x_controle == -velocidade:
                    pass
                else:
                    x_controle = velocidade
                    y_controle = 0

            if event.key == K_UP:
                if y_controle == velocidade:
                    pass
                else:
                    y_controle = -velocidade
                    x_controle = 0

            if event.key == K_DOWN:
                if y_controle == -velocidade:
                    pass
                else:
                    y_controle = velocidade
                    x_controle = 0
                        # criada a funcionalidade de bloquear o botao que manda a cobra ir para o sentido contrário ao qual ela está indo.(pass)
    x_cobra = x_cobra + x_controle
    y_cobra = y_cobra + y_controle
    # controles para a cobra seguir andando sozinha

    

    cobra = pygame.draw.rect(tela, (0,255,0), (x_cobra,y_cobra,20,20))
    maca = pygame.draw.rect(tela, (255,0,0), (x_maca,y_maca,20,20))
    
    if cobra.colliderect(maca):
        x_maca = randint(40, 600)
        y_maca = randint(50, 430)
        pontos += 1
        comprimento_inicial += 1 # crescer
        barulho_colisao.play()

    lista_cabeca = []   
    lista_cabeca.append(x_cobra)
    lista_cabeca.append(y_cobra)

    lista_cobra.append(lista_cabeca)

    if len(lista_cobra) > comprimento_inicial:
        del lista_cobra[0]
        # função de apagar a posição zero do corpo para não crescer indefinidamente
    

    aumenta_cobra(lista_cobra)
    
 
    tela.blit(texto_formatado, (450, 40)) 

    pygame.display.update() 
 



