import pygame
import tela
import boneco
import chave
import mapa

def main ():
    pygame.init ()
    #cria a tela
    tela_jogo = tela.criar_tela ()

    chaves_coletadas = 0

    flag_rodar = True

    while (flag_rodar):
        for ocorrencia in pygame.event.get ():
            #se apertar no botão de sair, sai.
            if (ocorrencia.type == pygame.QUIT):
                flag_rodar = False
        #vê o movimento do boneco
        boneco.movimento ()

        #colisao do boneco e chave
        rect_boneco = pygame.Rect(boneco.x, boneco.y, boneco.tamanho, boneco.tamanho)
        rect_chave = pygame.Rect(chave.x, chave.y, chave.tamanho, chave.tamanho)
        #se colidir, soma a chave
        if (rect_boneco.colliderect (rect_chave)):
            chaves_coletadas += 1
            chave.chaves_posicionar()
            print (f"{chaves_coletadas}")
        #pinta a tela
        mapa.desenhar(tela_jogo)
        #desenha os objetos
        pygame.draw.rect(tela_jogo, (255, 215, 0), (chave.x, chave.y, chave.tamanho, chave.tamanho))
        pygame.draw.rect (tela_jogo, (50, 205, 50), (boneco.x, boneco.y, 40, 40))
        #atualiza a tela
        pygame.display.flip ()
    #encerra o programa
    pygame.quit ()

main ()
