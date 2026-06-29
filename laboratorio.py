import pygame

laboratorio = pygame.image.load("imagem/mapa_laboratorio.png")

def desenhar(tela):
    tela.blit(laboratorio, (0, 0))
