import pygame
import random
#tamanho da chave
tamanho = 20
#spawn inicial
x = random.randint (50, 750)
y = random.randint (50, 550)
#cor da chave
chave = (255, 215, 0)
#posicionamento da chave
def chaves_posicionar ():
    global x, y

    x = random.randint (50, 750)
    y = random.randint (50, 550)
#desenho da chave
def chaves_desenhar (tela):
    pygame.draw.rect(tela, chave, (x, y, tamanho, tamanho))