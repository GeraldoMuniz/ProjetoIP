import pygame
from objetos.coletavel import Coletavel

class Dica(Coletavel):
    def __init__(self, nome, cor, x, y, mapa):
        super().__init__(nome, x, y)
        self.cor = cor
        self.mapa = mapa  #em qual sala essa dica aparece

    def desenhar(self, tela):
        if not self.pegou:
            pygame.draw.rect(tela, self.cor, self.rect)

#dicas do jogo
#o nome ja é o texto da dica

lista_dicas = [
    Dica("A chave vermelha está onde a música toca",                            (220, 20, 60),  700,  400, "principal"),
    Dica("A chave azul está onde poucos têm acesso",                            (0, 120, 255),  700,  450, "biblioteca"),
    Dica("A chave mestra está onde os robôs competem",                          (255, 215, 0),  600,  500, "mesanino"),
]

def desenhar_dicas(tela, mapa_atual):
    for dica in lista_dicas:
        if dica.mapa == mapa_atual:
            dica.desenhar(tela)
