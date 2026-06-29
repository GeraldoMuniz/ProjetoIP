import pygame
import tela
from personagens.boneco import Boneco
from personagens.vilao import Inimigo
from objetos import chave
import mapa 

def main ():
    pygame.init ()
    #cria a tela
    tela_jogo = tela.criar_tela ()
    #cria o personagem
    boneco_jogo = Boneco (vida = 3)
    inimigo_jogo = Inimigo (x = 200, y = 200, velocidade = 0.8) #cria o vilao

    chaves_coletadas = 0

    flag_rodar = True

    while (flag_rodar):
        for ocorrencia in pygame.event.get ():
            #se apertar no botão de sair, sai.
            if (ocorrencia.type == pygame.QUIT):
                flag_rodar = False
        #movimento do boneco
        boneco_jogo.movimento ()

        inimigo_jogo.perseguir (boneco_jogo)        #interações do vilao
        inimigo_jogo.verificar_colisao (boneco_jogo)


        #logica chave
        for c in chave.lista_chaves:
            if not c["pegou"]:
                        #rect colisao chave atual
                rect_chave = pygame.Rect(c["x"], c["y"], chave.tamanho, chave.tamanho)
                        
                        #se houver colisao
                if boneco_jogo.rect.colliderect(rect_chave):
                    c["pegou"] = True #some
                    chaves_coletadas += 1
                    print(f"Chaves coletadas: {chaves_coletadas}")
        #pinta a tela
        mapa.desenhar(tela_jogo)
        #desenha os objetos
        chave.desenhar_chaves (tela_jogo)
        #desenhar inimigos
        pygame.draw.rect (tela_jogo, (50, 205, 50), boneco_jogo.rect)
        pygame.draw.rect (tela_jogo, (255, 0, 0), inimigo_jogo.rect)
        #atualiza a tela
        pygame.display.flip ()
    #encerra o programa
    pygame.quit ()

main ()
