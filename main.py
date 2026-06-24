import pygame
import tela
from personagens import boneco
from objetos import chave
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

        #colisao do boneco
        rect_boneco = pygame.Rect(boneco.x, boneco.y, boneco.tamanho, boneco.tamanho)
        #logica chave
        for c in chave.lista_chaves:
            if not c["pegou"]:
                        #rect colisao chave atual
                rect_chave = pygame.Rect(c["x"], c["y"], chave.tamanho, chave.tamanho)
                        
                        #se houver colisao
                if rect_boneco.colliderect(rect_chave):
                    c["pegou"] = True #some
                    chaves_coletadas += 1
                    print(f"Chaves coletadas: {chaves_coletadas}")
        #pinta a tela
        mapa.desenhar(tela_jogo)
        #desenha os boneco
        chave.desenhar_chaves (tela_jogo)
        pygame.draw.rect (tela_jogo, (50, 205, 50), (boneco.x, boneco.y, 40, 40))
        #atualiza a tela
        pygame.display.flip ()
    #encerra o programa
    pygame.quit ()

main ()
