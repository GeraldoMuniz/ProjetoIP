import pygame

mapa = pygame.image.load("assets/mapa.png")

def desenhar(tela):
    tela.blit(mapa, (0, 0))
