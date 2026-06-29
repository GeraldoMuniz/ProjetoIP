import pygame
import tela
from personagens.boneco import Boneco
from personagens.vilao import Inimigo
from objetos import chave
import mapa
import biblioteca
import hardware
import area_privada
import robocin
import sala_de_musica

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
    "biblioteca": biblioteca.desenhar,
    "hardware": hardware.desenhar,
    "area_privada": area_privada.desenhar
    "robocin": robocin.desenhar,
    "sala_musica": sala_musica.desenhar
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

        porta_hardware = pygame.Rect(
                322,
                852,
                80,
                60
            )

        porta_saida_hardware = pygame.Rect(
                819,
                63,
                80,
                60
            )

        porta_area_privada = pygame.Rect(
                1318,
                215,
                60,
                60
            )
            
        porta_saida_area_privada = pygame.Rect(
                364,
                848,
                60,
                60
            )

        porta_robocin = pygame.Rect(
                1378,
                406,
                60,
                60
            )
            
            porta_saida_robocin = pygame.Rect(
                218,
                428,
                60,
                60
            )

        porta_sala_musica = pygame.Rect(
                1325,
                632,
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

                #personagem aparece dentro da biblioteca
                boneco_jogo.rect.x = 1120
                boneco_jogo.rect.y = 760

            elif boneco_jogo.rect.colliderect(porta_area_privada):
                mapa_atual = "area_privada"
            
                boneco_jogo.rect.x = 339
                boneco_jogo.rect.y = 798

            elif boneco_jogo.rect.colliderect(porta_robocin):
                mapa_atual = "robocin"
            
                boneco_jogo.rect.x = 280
                boneco_jogo.rect.y = 428

            elif boneco_jogo.rect.colliderect(porta_sala_musica):
            mapa_atual = "sala_musica"
        
            #posição temporária
            boneco_jogo.rect.x = 300
            boneco_jogo.rect.y = 300

        elif mapa_atual == "biblioteca":

            if boneco_jogo.rect.colliderect(porta_saida_biblioteca):
                mapa_atual = "principal"

                #personagem volta para o corredor
                boneco_jogo.rect.x = 340
                boneco_jogo.rect.y = 340

            if boneco_jogo.rect.colliderect(porta_hardware):
                mapa_atual = "hardware"
            
                #aparece logo abaixo da porta norte
                boneco_jogo.rect.x = 820
                boneco_jogo.rect.y = 140

        elif mapa_atual == "hardware":

            if boneco_jogo.rect.colliderect(porta_saida_hardware):
        
                mapa_atual = "biblioteca"
        
                boneco_jogo.rect.x = 340
                boneco_jogo.rect.y = 780

        elif mapa_atual == "area_privada":

            if boneco_jogo.rect.colliderect(porta_saida_area_privada):
        
                mapa_atual = "principal"
        
                boneco_jogo.rect.x = 1317
                boneco_jogo.rect.y = 300

        elif mapa_atual == "robocin":

            if boneco_jogo.rect.colliderect(porta_saida_robocin):
        
                mapa_atual = "principal"
        
                boneco_jogo.rect.x = 1310
                boneco_jogo.rect.y = 406

        elif mapa_atual == "sala_de_musica":
            pass

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
