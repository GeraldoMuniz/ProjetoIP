import pygame
from objetos.coletavel import Coletavel

class Chave(Coletavel):
    def __init__(self, nome, cor, x, y, porta):
        super().__init__(nome, x, y)
        self.cor = cor
        self.porta = porta  #qual porta essa chave abre

    def desenhar(self, tela):
        if not self.pegou:
            pygame.draw.rect(tela, self.cor, self.rect)

#chaves do jogo
#azul -> biblioteca -> abre o laboratorio
#vermelha -> helpdesk -> abre o robocin
#mestra -> mesanino -> abre a area privada (saida)
lista_chaves = [
    Chave("Chave Azul",     (0, 120, 255),  300,  200, "Laboratório"),
    Chave("Chave Vermelha", (220, 20, 60),  1500, 850, "RobôCIn"),
    Chave("Chave Mestra",   (255, 215, 0),  1200, 700, "Área Privada"),
]

def desenhar_chaves(tela):
    for chave in lista_chaves:
        chave.desenhar(tela)
