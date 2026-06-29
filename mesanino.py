import pygame

mesanino = pygame.image.load("imagem/mapa_mesanino.png")

def desenhar(tela):
    tela.blit(mesanino, (0, 0))
