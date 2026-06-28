import pygame
#esta função gerencia o tamanho da tela a ser mostrada.
def criar_tela ():
    largura = 1672
    altura = 941
    janela = pygame.display.set_mode ((largura, altura))

    return janela
