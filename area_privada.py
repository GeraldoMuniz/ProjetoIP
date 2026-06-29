import pygame

biblioteca = pygame.image.load("imagem/mapa_area_privada.png")

def desenhar(tela):
    tela.blit(biblioteca, (0, 0))
