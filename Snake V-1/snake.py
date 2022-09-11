# Músicas e Sons

import pygame
from pygame.locals import *
from sys import exit
from random import randint

pygame.init()

pygame.mixer.music.set_volume(0.1)
musica_de_fundo = pygame.mixer.music.load('sons/01.mp3')
barulho_colisao = pygame.mixer.Sound('sons/smw_coin.wav')
pygame.mixer.music.play(-1)
# inicia o player de música, e configura volume.

LARGURA = 640
ALTURA = 480
x = LARGURA/2 
y = ALTURA/2

x_azul = randint(40, 600)
y_azul = randint(50, 430)

pontos = 0
fonte = pygame.font.SysFont('arial', 40, bold=True, italic=True)

tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption('SNAKE')
relogio = pygame.time.Clock() 

while True:
    relogio.tick(30) 
    tela.fill((0,0,0)) 
    mensagem = f'Pontos:{pontos}'
    texto_formatado = fonte.render(mensagem, False, (255, 255, 255))
    
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

    ret_vermelho = pygame.draw.rect(tela, (255,0,0), (x,y,40,50))
    ret_azul = pygame.draw.rect(tela, (0,0,255), (x_azul,y_azul,40,50))
    
    if ret_vermelho.colliderect(ret_azul):
        x_azul = randint(40, 600)
        y_azul = randint(50, 430)
        pontos += 1
        barulho_colisao.play()
 
    tela.blit(texto_formatado, (450, 40)) 
    pygame.display.update() 
 