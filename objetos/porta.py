import pygame

class Porta:
    def __init__(self, x, y, largura, altura, nome, chave):
        self.nome_porta = nome
        self.chave_necessaria = chave
        self.trancada = True
        self.rect = pygame.Rect(x, y, largura, altura)
        self.cor_fechada = (139, 69, 19)
        
    def tentar_abrir(self, inventario):
        # se a porta nao tiver trancada deixa passar
        if self.trancada == False:
            return True
        else:
            # ve se o inventario tem a chave
            tem_chave = inventario.tem_chave(self.chave_necessaria)
            
            if tem_chave == True:
                self.trancada = False
                print("porta " + self.nome_porta + " abriu!")
                return True
            else:
                print("porta trancada, precisa da " + self.chave_necessaria)
                return False

    def desenhar(self, tela):
        if self.trancada == True:
            pygame.draw.rect(tela, self.cor_fechada, self.rect)
