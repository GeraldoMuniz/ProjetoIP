import pygame
import tela
from personagens.boneco import Boneco
from personagens.vilao import Inimigo
from objetos import chave
import mapa
import biblioteca

def desenhar_coracoes (tela_jogo, vida_atual):
    largura_coracao = 20
    espacamento = 10
    pos_x_inicial = 20  
    pos_y = 20          
    for i in range(vida_atual):
        x = pos_x_inicial + (i * (largura_coracao + espacamento))
        pygame.draw.circle(tela_jogo, (255, 0, 0), (x + 5, pos_y + 5), 6)
        pygame.draw.circle(tela_jogo, (255, 0, 0), (x + 15, pos_y + 5), 6)
        pygame.draw.polygon(tela_jogo, (255, 0, 0), [(x, pos_y + 7), (x + 20, pos_y + 7), (x + 10, pos_y + 18)])

def main ():
    pygame.init ()
    #cria a tela
    tela_jogo = tela.criar_tela ()
    #cria o personagem
    boneco_jogo = Boneco (vida = 3)
    inimigo_jogo = Inimigo (x = 200, y = 200, velocidade = 0.8) #cria o vilao

    chaves_coletadas = 0
    
    mapa_atual = "principal"

    mapas = {
    "principal": mapa.desenhar,
    "biblioteca": biblioteca.desenhar
    }

    fonte = pygame.font.SysFont(None, 28) #REMOVER

    flag_rodar = True

    while (flag_rodar):
        porta_biblioteca = pygame.Rect(
            317,
            248,
            60,
            60
        )

        porta_saida_biblioteca = pygame.Rect(
                1251,
                817,
                60,
                60
            )
        
        for ocorrencia in pygame.event.get ():
            #se apertar no botão de sair, sai.
            if (ocorrencia.type == pygame.QUIT):
                flag_rodar = False
        #movimento do boneco
        boneco_jogo.movimento ()
        if mapa_atual == "principal":
            if boneco_jogo.rect.colliderect(porta_biblioteca):
                mapa_atual = "biblioteca"

                # personagem aparece dentro da biblioteca
                boneco_jogo.rect.x = 1120
                boneco_jogo.rect.y = 760

        elif mapa_atual == "biblioteca":

            if boneco_jogo.rect.colliderect(porta_saida_biblioteca):
                mapa_atual = "principal"

                # personagem volta para o corredor
                boneco_jogo.rect.x = 340
                boneco_jogo.rect.y = 340

        inimigo_jogo.perseguir (boneco_jogo)        #interações do vilao
        inimigo_jogo.verificar_colisao (boneco_jogo)

        #logica chave
        chave.desenhar_chaves (tela_jogo)
        #pinta a tela
        mapas[mapa_atual](tela_jogo)
        
        #desenha os objetos
        chave.desenhar_chaves (tela_jogo)
        #desenhar inimigos
        pygame.draw.rect (tela_jogo, (50, 205, 50), boneco_jogo.rect)
        pygame.draw.rect (tela_jogo, (255, 0, 0), inimigo_jogo.rect)

        desenhar_coracoes (tela_jogo, boneco_jogo.vida)     #vida do personagem

        mx, my = pygame.mouse.get_pos()
        print(mx, my)
        texto = fonte.render(
            f"Mouse: ({mx}, {my})",
            True,
            (255,255,255)
        )

        tela_jogo.blit(texto, (10,10))

        #atualiza a tela
        pygame.display.flip ()
    #encerra o programa
    pygame.quit ()

main ()
