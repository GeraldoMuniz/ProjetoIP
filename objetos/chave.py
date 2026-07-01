import pygame
from objetos.coletavel import Coletavel

class Chave(Coletavel):
    def __init__(self, nome, cor, x, y, porta, mapa):
        super().__init__(nome, x, y)
        self.cor = cor
        self.porta = porta  # qual porta essa chave abre
        self.mapa = mapa    # em qual sala essa chave aparece

        if nome == "Chave Vermelha":
            self.imagem = pygame.image.load("imagem/chave_vermelha_transparente.png").convert_alpha()

        elif nome == "Chave Azul":
            self.imagem = pygame.image.load("imagem/chave_azul_transparente.png").convert_alpha()

        elif nome == "Chave Mestra":
            self.imagem = pygame.image.load("imagem/chave_mestra_transparente.png").convert_alpha()

        self.imagem = pygame.transform.scale(self.imagem, (64, 64))

    def desenhar(self, tela):
        if not self.pegou:
            tela.blit(self.imagem, self.rect)

# chaves do jogo (posições x e y zeradas aguardando o Integrante 5)
# vermelha: fica na sala de música -> abre a área privada
# azul: fica na área privada -> abre a entrada do laboratório de hardware
# mestra: fica no robôcin -> abre a saída do laboratório de hardware
lista_chaves = [
    Chave("Chave Vermelha", (220, 20, 60),  900,  500, "Área Privada",    "sala_musica"),
    Chave("Chave Azul",     (0, 120, 255),  1000, 350, "Laboratório",    "area_privada"),
    Chave("Chave Mestra",   (255, 215, 0),  1100, 550, "Saída Hardware", "robocin"),
]

def desenhar_chaves(tela, mapa_atual):
    for chave in lista_chaves:
        if chave.mapa == mapa_atual:
            chave.desenhar(tela)
