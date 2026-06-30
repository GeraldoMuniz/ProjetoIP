import pygame
from objetos.coletavel import Coletavel

class Chave(Coletavel):
    def __init__(self, nome, cor, x, y, porta):
        super().__init__(nome, x, y)
        self.cor = cor
        self.porta = porta  # qual porta essa chave abre

    def desenhar(self, tela):
        if not self.pegou:
            pygame.draw.rect(tela, self.cor, self.rect)

# chaves do jogo (posições x e y zeradas aguardando o Integrante 5)
# vermelha: fica na sala de música -> abre a área privada
# azul: fica na área privada -> abre a entrada do laboratório de hardware
# mestra: fica no robôcin -> abre a saída do laboratório de hardware
lista_chaves = [
    Chave("Chave Vermelha", (220, 20, 60),  0, 0, "Área Privada"),
    Chave("Chave Azul",     (0, 120, 255),  0, 0, "Entrada do Laboratório"),
    Chave("Chave Mestra",   (255, 215, 0),  0, 0, "Saída do Laboratório"),
]

def desenhar_chaves(tela):
    for chave in lista_chaves:
        chave.desenhar(tela)
