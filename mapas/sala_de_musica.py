import pygame

sala_musica = pygame.image.load("imagem/mapa_sala_de_musica.png")

def desenhar(tela):
    tela.blit(sala_musica, (0, 0))
