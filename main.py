import pygame
import tela
from personagens.boneco import Boneco
from personagens.vilao import Inimigo
from objetos import chave
from objetos import kit_medico
from objetos import dica
from objetos.inventario import Inventario

from mapas import mapa
import mapas.biblioteca as biblioteca
import mapas.hardware as hardware
import mapas.area_privada as area_privada
import mapas.robocin as robocin
import mapas.sala_de_musica as sala_de_musica
import mapas.mesanino as mesanino
import mapas.anfiteatro as anfiteatro
import mapas.banheiro as banheiro
import mapas.helpdesk as helpdesk
import mapas.laboratorio as laboratorio 
from colisoes.principal import paredes_principal
from colisoes.biblioteca_colisao import paredes_biblioteca


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

def desenhar_hud(tela_jogo, fonte, inventario):
    textos = [
        f"Chaves: {len(inventario.chaves)}/3",
        f"Kits: {len(inventario.kits)}",
        f"Dicas: {len(inventario.dicas)}/3",
    ]
    for i, txt in enumerate(textos):
        superficie = fonte.render(txt, True, (255, 255, 255))
        tela_jogo.blit(superficie, (20, 50 + i * 30))

def main ():
    pygame.init ()
    #cria a tela
    tela_jogo = tela.criar_tela ()
    #cria o personagem
    boneco_jogo = Boneco (vida = 3)
    inimigo_jogo = Inimigo (x = 200, y = 200, velocidade = 0.8) #cria o vilao

    inventario = Inventario()
    texto_dica_atual = ""
    
    mapa_atual = "principal"

    mapas = {
    "principal": mapa.desenhar,
    "biblioteca": biblioteca.desenhar,
    "hardware": hardware.desenhar,
    "area_privada": area_privada.desenhar,
    "robocin": robocin.desenhar,
    "sala_musica": sala_de_musica.desenhar,
    "mesanino": mesanino.desenhar,
    "anfiteatro": anfiteatro.desenhar,
    "banheiro": banheiro.desenhar,
    "helpdesk": helpdesk.desenhar,
    "laboratorio": laboratorio.desenhar
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

        porta_saida_sala_musica = pygame.Rect(
                826,
                100,
                60,
                60
            )

        porta_mesanino = pygame.Rect(
                1082,
                630,
                60,
                60
            )
            
        porta_saida_mesanino = pygame.Rect(
                829,
                90,
                60,
                60
            )

        porta_anfiteatro = pygame.Rect(
                526,
                620,
                60,
                60
            )

        porta_saida_anfiteatro = pygame.Rect(
                1485,
                409,
                60,
                60
            )

        porta_banheiro = pygame.Rect(
                1108,
                172,
                60,
                60
            )

        porta_saida_banheiro = pygame.Rect(
                834,
                772,
                60,
                60
            )

        porta_helpdesk = pygame.Rect(
                510,
                794,
                60,
                60
            )

        porta_saida_helpdesk = pygame.Rect(
                1550,
                712,
                60,
                60
            )

        porta_laboratorio = pygame.Rect(
                826,
                212,
                60,
                60
            )

        porta_saida_laboratorio = pygame.Rect(
                794,
                845,
                60,
                60
            )
        
        for ocorrencia in pygame.event.get ():
            #se apertar no botão de sair, sai.
            if (ocorrencia.type == pygame.QUIT):
                flag_rodar = False
                
        #MOVIMENTO DO BONECO
        if mapa_atual == "principal":
            boneco_jogo.movimento(paredes_principal)
        elif mapa_atual == "biblioteca":
            boneco_jogo.movimento(paredes_biblioteca)
        else:
            boneco_jogo.movimento([])
            
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
        
                #posicao que o personagem aparece
                boneco_jogo.rect.x = 825
                boneco_jogo.rect.y = 240

            elif boneco_jogo.rect.colliderect(porta_mesanino):
                mapa_atual = "mesanino"
            
                #personagem aparece dentro do mesanino
                boneco_jogo.rect.x = 842
                boneco_jogo.rect.y = 251

            elif boneco_jogo.rect.colliderect(porta_anfiteatro):
                mapa_atual = "anfiteatro"
            
                boneco_jogo.rect.x = 1326
                boneco_jogo.rect.y = 418

            elif boneco_jogo.rect.colliderect(porta_banheiro):
                mapa_atual = "banheiro"
            
                boneco_jogo.rect.x = 841
                boneco_jogo.rect.y = 605

            elif boneco_jogo.rect.colliderect(porta_helpdesk):
                mapa_atual = "helpdesk"
            
                boneco_jogo.rect.x = 1394
                boneco_jogo.rect.y = 778

            elif boneco_jogo.rect.colliderect(porta_laboratorio):
                mapa_atual = "laboratorio"
            
                boneco_jogo.rect.x = 823
                boneco_jogo.rect.y = 720

        elif mapa_atual == "biblioteca":

            if boneco_jogo.rect.colliderect(porta_saida_biblioteca):
                mapa_atual = "principal"

                #personagem volta para o corredor
                boneco_jogo.rect.x = 340
                boneco_jogo.rect.y = 340

            elif boneco_jogo.rect.colliderect(porta_hardware):
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

        elif mapa_atual == "sala_musica":
            
            if boneco_jogo.rect.colliderect(porta_saida_sala_musica):

                mapa_atual = "principal"
        
                #personagem volta para o corredor
                boneco_jogo.rect.x = 1326
                boneco_jogo.rect.y = 520

        elif mapa_atual == "mesanino":

            if boneco_jogo.rect.colliderect(porta_saida_mesanino):
        
                mapa_atual = "principal"
        
                #personagem volta para o corredor
                boneco_jogo.rect.x = 1084
                boneco_jogo.rect.y = 577

        elif mapa_atual == "anfiteatro":

            if boneco_jogo.rect.colliderect(porta_saida_anfiteatro):
        
                mapa_atual = "principal"
        
                boneco_jogo.rect.x = 632
                boneco_jogo.rect.y = 637

        elif mapa_atual == "banheiro":

            if boneco_jogo.rect.colliderect(porta_saida_banheiro):
        
                mapa_atual = "principal"
        
                boneco_jogo.rect.x = 1111
                boneco_jogo.rect.y = 273

        elif mapa_atual == "helpdesk":

            if boneco_jogo.rect.colliderect(porta_saida_helpdesk):
        
                mapa_atual = "principal"
        
                boneco_jogo.rect.x = 607
                boneco_jogo.rect.y = 760

        elif mapa_atual == "laboratorio":

            if boneco_jogo.rect.colliderect(porta_saida_laboratorio):
        
                mapa_atual = "principal"
        
                boneco_jogo.rect.x = 812
                boneco_jogo.rect.y = 300

        inimigo_jogo.perseguir (boneco_jogo)        #interações do vilao
        inimigo_jogo.verificar_colisao (boneco_jogo)

        #logica de coleta
        for ch in chave.lista_chaves:
            if ch.mapa == mapa_atual and ch.verificar_colisao(boneco_jogo.rect):
                inventario.adicionar_chave(ch)

        for kt in kit_medico.lista_kits:
            if kt.mapa == mapa_atual and kt.verificar_colisao(boneco_jogo.rect):
                inventario.adicionar_kit(kt)

        for dc in dica.lista_dicas:
            if dc.mapa == mapa_atual and dc.verificar_colisao(boneco_jogo.rect):
                inventario.adicionar_dica(dc)
                texto_dica_atual = dc.nome

        #pinta a tela
        mapas[mapa_atual](tela_jogo)

        #TESTE PARA VERIFICAR COLISOES AN BIBLIOTECA
        if mapa_atual == "biblioteca":
            for parede in paredes_biblioteca:
                pygame.draw.rect(
                    tela_jogo,
                    (255, 0, 255),
                    parede,
                    2
                )
        
        #desenha os objetos (filtrado pelo mapa atual)
        chave.desenhar_chaves(tela_jogo, mapa_atual)
        kit_medico.desenhar_kits(tela_jogo, mapa_atual)
        dica.desenhar_dicas(tela_jogo, mapa_atual)

        #desenhar personagens
        pygame.draw.rect (tela_jogo, (50, 205, 50), boneco_jogo.rect)
        pygame.draw.rect (tela_jogo, (255, 0, 0), inimigo_jogo.rect)

        desenhar_coracoes (tela_jogo, boneco_jogo.vida)     #vida do personagem
        desenhar_hud(tela_jogo, fonte, inventario)          #contador de coletaveis

        # desenha a ultima dica pega no topo da tela
        if texto_dica_atual != "":
            superficie_dica = fonte.render(texto_dica_atual, True, (255, 255, 0)) # Amarelo
            rect_dica = superficie_dica.get_rect(center=(1672 // 2, 30))
            tela_jogo.blit(superficie_dica, rect_dica)

        
        
        """mx, my = pygame.mouse.get_pos()
        print(mx, my)
        texto = fonte.render(            #ESSA PARTE SERVE CASO SEJA NECESSÁRIO VERIFICAR COORDENADAS
            f"Mouse: ({mx}, {my})",
            True,
            (255,255,255)
        )

        
        tela_jogo.blit(texto, (10,10))"""

        #atualiza a tela
        pygame.display.flip ()
    #encerra o programa
    pygame.quit ()

main ()
