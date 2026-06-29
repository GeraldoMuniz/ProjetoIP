import pygame

biblioteca = pygame.image.load("imagem/mapa_biblioteca.png")

def desenhar(tela):
    tela.blit(biblioteca, (0, 0))
