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
x_cobra = int(LARGURA/2) 
y_cobra = int(ALTURA/2)

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
comprimento_inicial = 3
morreu = False

def limite_tela(x_cobra, y_cobra):
    if x_cobra >= LARGURA or x_cobra <= 0 or y_cobra < 0 or y_cobra > ALTURA:
        return True
    else:
        return False
        # função que define os limites da tela e termina o jogo se houver colisão nestas.
def aumenta_cobra(lista_cobra):
    for XeY in lista_cobra:
        #XeY = [x, y]
        #XeY[0] = x
        #XeY[1] = y

        pygame.draw.rect(tela, (0,255,0),(XeY[0],XeY[1],20,20))

def reiniciar_jogo():
    global pontos, comprimento_inicial, x_cobra, y_cobra, lista_cobra, lista_cabeca, x_maca, y_maca, morreu
    pontos = 0
    comprimento_inicial = 5
    x_cobra = int(LARGURA/2) 
    y_cobra = int(ALTURA/2)
    lista_cobra = []
    lista_cabeca = []
    x_maca = randint(40, 600)
    y_maca = randint(50, 430)
    morreu = False

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
                       
    x_cobra = x_cobra + x_controle
    y_cobra = y_cobra + y_controle
    

    cobra = pygame.draw.rect(tela, (0,255,0), (x_cobra,y_cobra,20,20))
    maca = pygame.draw.rect(tela, (255,0,0), (x_maca,y_maca,20,20))
    
    if cobra.colliderect(maca):
        x_maca = randint(40, 600)
        y_maca = randint(50, 430)
        pontos += 1
        comprimento_inicial += 1 
        barulho_colisao.play()

    lista_cabeca = []   
    lista_cabeca.append(x_cobra)
    lista_cabeca.append(y_cobra)

    lista_cobra.append(lista_cabeca)

    if lista_cobra.count(lista_cabeca) > 1 or limite_tela(x_cobra, y_cobra) == True: # reinicia o jogo se sair dos limites da tela
        fonte2 = pygame.font.SysFont('arial', 20, True, True)
        mensagem = 'Game over! Pressione a tecla ESPAÇO para jogar novamente'
        texto_formatado = fonte2.render(mensagem, True, (0,0,0))
        ret_texto = texto_formatado.get_rect()
        # criar o texto para ser exibido na tela

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
                        # funcionalidade para reiniciar o jog quando a cabeça tocar no corpo da cobra.

            ret_texto.center = (LARGURA//2, ALTURA//2)
            tela.blit(texto_formatado, ret_texto)  # centralizar o texto      
            pygame.display.update()

    

    '''if x_cobra > LARGURA:
        x_cobra = 0
    if x_cobra < 0:
        x_cobra = LARGURA
    if y_cobra < 0:
        y_cobra = ALTURA
    if y_cobra > ALTURA:
        y_cobra = 0'''
        # reiniciar no lado oposo sempre que a cobra sair da tela.


    if len(lista_cobra) > comprimento_inicial:
        del lista_cobra[0]

    aumenta_cobra(lista_cobra)
    
 
    tela.blit(texto_formatado, (450, 40)) 

    pygame.display.update() 
 