import pygame

#classe base dos coletaveis
class Coletavel:
    tamanho = 20

    def __init__(self, nome, x, y):
        self.nome = nome
        self.x = x
        self.y = y
        self.pegou = False
        self.rect = pygame.Rect(x, y, self.tamanho, self.tamanho)

    def verificar_colisao(self, rect_jogador):
        if not self.pegou and self.rect.colliderect(rect_jogador):
            self.pegou = True
            return True
        return False

    def desenhar(self, tela):
        pass
