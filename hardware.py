import pygame

hardware = pygame.image.load("imagem/mapa_lab_hardware.png")

def desenhar(tela):
    tela.blit(hardware, (0, 0))
