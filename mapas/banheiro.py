import pygame

banheiro = pygame.image.load("imagem/mapa_banheiro.png")

def desenhar(tela):
    tela.blit(banheiro, (0, 0))
