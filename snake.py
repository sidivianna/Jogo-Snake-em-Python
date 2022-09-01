
import pygame

from pygame.locals import *

from sys import exit

pygame.init()

LARGURA = 640
ALTURA = 480

tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption('Snake')

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

    pygame.display.update()