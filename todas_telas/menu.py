import pygame
from todas_telas import tela

def menu():
    pygame.init()
    tela_jogo = tela.criar_tela()
    pygame.display.set_caption("CInBeribe")
    fundo_cin = pygame.image.load ("imagem/Imagem_CIn.png")
    fonte_titulo = pygame.font.SysFont(None,70)
    titulo = fonte_titulo.render("CInBeribe",True,(255,0,0))
    tela_jogo.blit(titulo,(450,120))
    rodando = True
    while rodando:
        for ocorrencia in pygame.event.get ():
            if (ocorrencia.type == pygame.QUIT):
                rodando = False
            elif ocorrencia.type == pygame.MOUSEBUTTONDOWN:
                if ocorrencia.button == 1: 
                    if botao_start.collidepoint(ocorrencia.pos):
                        rodando = False
        tela_jogo.blit (fundo_cin, (0, 0))
        tela_jogo.blit (titulo,(450,120))
        x = 600
        y = 350
        largura = 300
        altura = 80

        botao_start = pygame.Rect( x,y ,largura,altura)
        pygame.draw.rect(tela_jogo ,(255,0,0),botao_start)
        # botao start
        fonte_botao = pygame.font.SysFont(None,50)
        texto_start = fonte_botao.render("Começar",True,(255,255,255))
        tela_jogo.blit(texto_start,(690,370))
        pygame.display.flip()

menu ()