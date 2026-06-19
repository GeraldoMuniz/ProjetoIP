import pygame
#esta função gerencia o tamanho da tela a ser mostrada.
def criar_tela ():
    largura = 1920
    altura = 1080
    janela = pygame.display.set_mode ((largura, altura))

    return janela
