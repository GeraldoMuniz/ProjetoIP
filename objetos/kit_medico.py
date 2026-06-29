import pygame
from objetos.coletavel import Coletavel

#substitui as baterias, recupera 1 coracao do jogador
class KitMedico(Coletavel):
    cor_fundo = (255, 50, 50)
    cor_cruz = (255, 255, 255)

    def __init__(self, x, y):
        super().__init__("Kit Médico", x, y)

    def usar(self, personagem):
        if personagem.vidas < personagem.VIDAS_MAX:
            personagem.curar(1)
            print("kit medico usado! +1 coracao")
        else:
            print("vida cheia!")

    def desenhar(self, tela):
        if not self.pegou:
            pygame.draw.rect(tela, self.cor_fundo, self.rect)
            #desenha a cruz
            cx = self.rect.centerx
            cy = self.rect.centery
            t = self.tamanho
            pygame.draw.rect(tela, self.cor_cruz, (cx - t//6, cy - t//3, t//3, t*2//3))
            pygame.draw.rect(tela, self.cor_cruz, (cx - t//3, cy - t//6, t*2//3, t//3))

#posicoes dos kits no mapa (ajustar depois com o pessoal dos mapas)
lista_kits = [
    KitMedico(600,  400),
    KitMedico(1000, 500),
    KitMedico(800,  750),
]

def desenhar_kits(tela):
    for kit in lista_kits:
        kit.desenhar(tela)
