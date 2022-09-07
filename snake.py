
import pygame
import os
from pygame.locals import *
from sys import exit
from random import randrange # trocar a biblioteca para poder utilizar iintervalos de 20
from time import sleep

pygame.init()

pygame.mixer.music.set_volume(0.1)
musica_de_fundo = pygame.mixer.music.load('sons/01.mp3')
barulho_colisao = pygame.mixer.Sound('sons/smw_coin.wav')
som_game_over = pygame.mixer.Sound('sons/smw_game_over.wav')
up_level = pygame.mixer.Sound('sons/smw_power-up.wav')
end_game_song = pygame.mixer.Sound('sons/smw_castle_clear.wav')
pygame.mixer.music.play(-1)

LARGURA = 640
ALTURA = 640
x_cobra = int(LARGURA/2) 
y_cobra = int(ALTURA/2)

velocidade = 20 #mudança na velocidade para andar em bloco de 20px
x_controle = velocidade
y_controle = 0

lista_cobra = []
x_maca = randrange(0, 620, 20) # 640 // 20 = 32
y_maca = randrange(0, 620, 20) # 480 //20 = 24

level = 1
pontos = 0
#mensagem_tela = []
fonte = pygame.font.SysFont('arial', 20, bold=True, italic=True)

tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption('SNAKE')
relogio = pygame.time.Clock() 
#lista_cobra = []
comprimento_inicial = 5
morreu = False

#def mensagem_tela():
    #fonte = pygame.font.SysFont('arial', 20, bold=True, italic=True)

def level_up():
    up_level.play()

def pause():
    paused = True
    while paused:
        tela.fill((255,255,255))
        fonte2 = pygame.font.SysFont('arial', 20, True, True)
        mensagem = 'PAUSE Pressione a tecla C para continuar e Q para sair'
        texto_formatado = fonte2.render(mensagem, True, (0,0,0))
        ret_texto = texto_formatado.get_rect()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    paused = False
                elif event.key == K_q:
                    pygame.quit()
                    quit()

            ret_texto.center = (LARGURA//2, ALTURA//2)
            tela.blit(texto_formatado, ret_texto)  # centralizar o texto      
            pygame.display.update()
        
            
def limite_tela(x_cobra, y_cobra):
    if x_cobra >= LARGURA or x_cobra <= 0 - 10 or y_cobra < 0-10 or y_cobra > ALTURA:
        return True
    else:
        return False


def aumenta_cobra(lista_cobra):
    for XeY in lista_cobra:
        #XeY = [x, y]
        #XeY[0] = x
        #XeY[1] = y
        #XeY[1] = y

        pygame.draw.rect(tela, (255,255,255),(XeY[0],XeY[1],20,20)) #branca
       
        if pontos >= 3:
            pygame.draw.rect(tela, (0,255,0),(XeY[0],XeY[1],20,20))   #verde       
                    
        if pontos >= 5:
            pygame.draw.rect(tela, (0,0,255),(XeY[0],XeY[1],20,20)) #azul

        if pontos >= 8:
            pygame.draw.rect(tela, (255,255,0),(XeY[0],XeY[1],20,20)) #amarela
                          
        if pontos >= 10:
            pygame.draw.rect(tela, (255,0,255),(XeY[0],XeY[1],20,20)) #rosa

#def morreu_end():
  
def reiniciar_jogo():
    global pontos, comprimento_inicial, x_cobra, y_cobra, lista_cobra, lista_cabeca, x_maca, y_maca, morreu
    musica_de_fundo = pygame.mixer.music.load('sons/01.mp3')
    pygame.mixer.music.play(-1)
    pontos = 0
    comprimento_inicial = 5
    x_cobra = int(LARGURA/2) 
    y_cobra = int(ALTURA/2)
    lista_cobra = []
    lista_cabeca = []
    x_maca = randrange(0, 620, 20) 
    y_maca = randrange(0, 620, 20) 
    morreu = False
    

while True:
    relogio.tick(30) 
    tela.fill((0,0,0)) 
    mensagem = f'Pontos:{pontos}'
    mensagem2 = f'Level:{level}'
    
    texto_formatado = fonte.render(mensagem, False, (255, 255, 255))
    texto_formatado2 = fonte.render(mensagem2, False, (255, 255,0))
   
    
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

            if event.key == K_SPACE:
                pause()
                

    sleep(0.10) #sleep a cada passo da cobrinha       
    x_cobra = x_cobra + x_controle
    y_cobra = y_cobra + y_controle
    

    cobra = pygame.draw.rect(tela, (0,255,0), (x_cobra,y_cobra,20,20))
    maca = pygame.draw.rect(tela, (255,0,0), (x_maca,y_maca,20,20))
    
    if cobra.colliderect(maca):
        x_maca = randrange(0, 620, 20) 
        y_maca = randrange(0, 620, 20) 
        pontos += 1
        comprimento_inicial += 1 
        barulho_colisao.play()
 
        if pontos == 3:
            level_up()
            level += 1
        if pontos == 5:
            level_up()
            level += 1
        if pontos == 8:
            level_up()
            level += 1
        if pontos == 10:
            level_up()
            level += 1
    

    lista_cabeca = []   
    lista_cabeca.append(x_cobra)
    lista_cabeca.append(y_cobra)

    lista_cobra.append(lista_cabeca)



    if lista_cobra.count(lista_cabeca) > 1 or limite_tela(x_cobra, y_cobra) == True: 
        fonte2 = pygame.font.SysFont('arial', 20, True, True)
        mensagem = 'Game over! Pressione a tecla ESPAÇO para jogar novamente'
        texto_formatado = fonte2.render(mensagem, True, (0,0,0))
        musica_de_fundo = pygame.mixer.music.pause()
        ret_texto = texto_formatado.get_rect()

        som_game_over.play()

        #morreu_end()

        morreu = True
        while morreu:
            tela.fill((255,255,255))
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    exit()
                if event.type == KEYDOWN:
                    if event.key == K_SPACE:
                        reiniciar_jogo()

                        

            ret_texto.center = (LARGURA//2, ALTURA//2)
            tela.blit(texto_formatado, ret_texto)  # centralizar o texto      
            pygame.display.update()
        

    if len(lista_cobra) > comprimento_inicial:
        del lista_cobra[0]


    aumenta_cobra(lista_cobra)
    
    tela.blit(texto_formatado, (540, 20)) 
    tela.blit(texto_formatado2, (540, 40)) 

    pygame.display.update() 
 
    

 # importar a biblioteca sleep e fazer a cobra se mover em blocos de 20
 # correção para nao deixar que a cobra passe meio corpo para fora da tela
 # adicionada musica de game-over
 # corrgido som pausar ao reiniciar
 # adicionada função de trocar de cor da cobrinha em level_up
 # criado contador de level na tela


 # criar uma função pause no game
 # bug: - corrigir problema da maça respaunar em algum espaço que ja esteja o corpo da cobra(porem nao espauno dentro dos blocos de 20) (da erro quando reinicia o jogo)
 