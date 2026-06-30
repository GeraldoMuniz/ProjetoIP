import pygame

robocin = pygame.image.load("imagem/mapa_robocin.png")

def desenhar(tela):
    tela.blit(robocin, (0, 0))
