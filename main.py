import pygame
from todas_telas import tela, menu
from todas_telas.telas_finais import mostrar_derrota
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
from colisoes.banheiro_colisao import paredes_banheiro
from colisoes.anfiteatro_colisao import paredes_anfiteatro
from colisoes.area_privada_colisao import paredes_area_privada
from colisoes.hardware_colisao import paredes_hardware
from colisoes.helpdesk_colisao import paredes_helpdesk
from colisoes.laboratorio_colisao import paredes_laboratorio
from colisoes.mesanino_colisao import paredes_mesanino
from colisoes.robocin_colisao import paredes_robocin
from colisoes.sala_de_musica_colisao import paredes_sala_de_musica


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

    chaves_coletadas = []

    historico_dicas = []

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


        if boneco_jogo.vida <= 0:
            mostrar_derrota(tela_jogo)
            flag_rodar = False      #CASO O BONECO FIQUE COM A VIDA IGUAL A 0 OU INFERIOR A 0: EM DESENVOLVIMENTO
                                    #PRECISA PREPARAR TELA DE DERROTA
                

        #MOVIMENTO DO BONECO
        if mapa_atual == "principal":
            boneco_jogo.movimento(paredes_principal)
        elif mapa_atual == "biblioteca":
            boneco_jogo.movimento(paredes_biblioteca)
        elif mapa_atual == "anfiteatro":
            boneco_jogo.movimento (paredes_anfiteatro)
        elif mapa_atual == "area_privada":
            boneco_jogo.movimento (paredes_area_privada)
        elif mapa_atual == "banheiro":
            boneco_jogo.movimento (paredes_banheiro)
        elif mapa_atual == "hardware":
            boneco_jogo.movimento (paredes_hardware)
        elif mapa_atual == "helpdesk":
            boneco_jogo.movimento (paredes_helpdesk)
        elif mapa_atual == "laboratorio":
            boneco_jogo.movimento (paredes_laboratorio)
        elif mapa_atual == "mesanino":
            boneco_jogo.movimento (paredes_mesanino)
        elif mapa_atual == "robocin":
            boneco_jogo.movimento (paredes_robocin)
        elif mapa_atual == "sala_musica":
            boneco_jogo.movimento (paredes_sala_de_musica)
        else:
            boneco_jogo.movimento([])
        
            #MAPAS
        if mapa_atual == "principal":
            if boneco_jogo.rect.colliderect(porta_biblioteca):
                mapa_atual = "biblioteca"

                #personagem aparece dentro da biblioteca
                boneco_jogo.rect.x = 1120
                boneco_jogo.rect.y = 760

            elif boneco_jogo.rect.colliderect(porta_area_privada) and "Chave Mestra" in chaves_coletadas:
                mapa_atual = "area_privada"
            
                boneco_jogo.rect.x = 339
                boneco_jogo.rect.y = 798

            elif boneco_jogo.rect.colliderect(porta_robocin) and "Chave Vermelha" in chaves_coletadas:
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

            elif boneco_jogo.rect.colliderect(porta_hardware) and "Chave Azul" in chaves_coletadas:
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
                chaves_coletadas.append (ch.nome)

        for kt in kit_medico.lista_kits:
            if kt.mapa == mapa_atual and kt.verificar_colisao(boneco_jogo.rect):
                inventario.adicionar_kit(kt)
                boneco_jogo.vida += 1
                if (boneco_jogo.vida > 3):
                    boneco_jogo.vida = 3

        for dc in dica.lista_dicas:
            if dc.mapa == mapa_atual and dc.verificar_colisao(boneco_jogo.rect):
                inventario.adicionar_dica(dc)
                texto_dica_atual = dc.nome

        #pinta a tela
        mapas[mapa_atual](tela_jogo)
        
        #desenha os objetos (filtrado pelo mapa atual)
        chave.desenhar_chaves(tela_jogo, mapa_atual)
        kit_medico.desenhar_kits(tela_jogo, mapa_atual)
        dica.desenhar_dicas(tela_jogo, mapa_atual)

        #desenhar personagens
        tela_jogo.blit(
            boneco_jogo.sprite,
            (
                boneco_jogo.rect.x - 4,
                boneco_jogo.rect.y - 24
            )
        )
        tela_jogo.blit(
            inimigo_jogo.sprite,
            (
                inimigo_jogo.rect.x - 4,
                inimigo_jogo.rect.y - 16
            )
        )

        desenhar_coracoes (tela_jogo, boneco_jogo.vida)     #vida do personagem
        desenhar_hud (tela_jogo, fonte, inventario)          #contador de coletaveis

        # desenha a ultima dica pega no topo da tela
        if texto_dica_atual != "":
            superficie_dica = fonte.render(texto_dica_atual, True, (255, 255, 0)) # Amarelo
            rect_dica = superficie_dica.get_rect(center=(1672 // 2, 30))
            tela_jogo.blit(superficie_dica, rect_dica)
            if (texto_dica_atual not in historico_dicas):
                historico_dicas.append (texto_dica_atual)
        
        if (len(historico_dicas) > 0):
            posicao_y = 700
            for dicas_coletadas in historico_dicas:
                superficie_hist = fonte.render(dicas_coletadas, True, (255, 255, 255))   #DEIXAR DICAS SALVAS NA TELA
                tela_jogo.blit(superficie_hist, (20, posicao_y))
                posicao_y += 30



        if (boneco_jogo.rect.colliderect (porta_area_privada) and "Chave Mestra" not in chaves_coletadas and mapa_atual == "principal"):
            texto_chave_mestra = ("Você precisa da Chave Mestra para abrir.")
            imagem_texto = fonte.render (texto_chave_mestra, True, (255, 255, 255))
            tela_jogo.blit (imagem_texto, (650, 80))
            teclas = pygame.key.get_pressed()
            if teclas[pygame.K_LEFT] or teclas[pygame.K_a]:
                boneco_jogo.rect.x += boneco_jogo.velocidade
            if teclas[pygame.K_RIGHT] or teclas[pygame.K_d]:                #LÓGICA PARA NAO PASSAR DAS 3 PAREDES
                boneco_jogo.rect.x -= boneco_jogo.velocidade
            if teclas[pygame.K_UP] or teclas[pygame.K_w]:
                boneco_jogo.rect.y += boneco_jogo.velocidade
            if teclas[pygame.K_DOWN] or teclas[pygame.K_s]:
                boneco_jogo.rect.y -= boneco_jogo.velocidade

        elif (boneco_jogo.rect.colliderect (porta_robocin) and "Chave Vermelha" not in chaves_coletadas and mapa_atual == "principal"):
            texto_chave_vermelha = ("Você precisa da Chave Vermelha para abrir.")
            imagem_texto = fonte.render (texto_chave_vermelha, True, (255, 255, 255))
            tela_jogo.blit (imagem_texto, (650, 80))
            teclas = pygame.key.get_pressed()
            if teclas[pygame.K_LEFT] or teclas[pygame.K_a]:
                boneco_jogo.rect.x += boneco_jogo.velocidade                
            if teclas[pygame.K_RIGHT] or teclas[pygame.K_d]:
                boneco_jogo.rect.x -= boneco_jogo.velocidade
            if teclas[pygame.K_UP] or teclas[pygame.K_w]:
                boneco_jogo.rect.y += boneco_jogo.velocidade
            if teclas[pygame.K_DOWN] or teclas[pygame.K_s]:
                boneco_jogo.rect.y -= boneco_jogo.velocidade

        elif (boneco_jogo.rect.colliderect (porta_hardware) and "Chave Azul" not in chaves_coletadas and mapa_atual == "biblioteca"):
            texto_chave_azul = ("Você precisa da Chave Azul para abrir.")
            imagem_texto = fonte.render (texto_chave_azul, True, (255, 255, 255))
            tela_jogo.blit (imagem_texto, (650, 80))
            teclas = pygame.key.get_pressed()
            if teclas[pygame.K_LEFT] or teclas[pygame.K_a]:
                boneco_jogo.rect.x += boneco_jogo.velocidade
            if teclas[pygame.K_RIGHT] or teclas[pygame.K_d]:
                boneco_jogo.rect.x -= boneco_jogo.velocidade
            if teclas[pygame.K_UP] or teclas[pygame.K_w]:
                boneco_jogo.rect.y += boneco_jogo.velocidade
            if teclas[pygame.K_DOWN] or teclas[pygame.K_s]:
                boneco_jogo.rect.y -= boneco_jogo.velocidade
            
            

            

        
        """mx, my = pygame.mouse.get_pos()
        print(mx, my)
        texto = fonte.render(            #ESSA PARTE SERVE CASO SEJA NECESSÁRIO VERIFICAR COORDENADAS
            f"Mouse: ({mx}, {my})",
            True,
            (255,255,255)
        )

        
        tela_jogo.blit(texto, (10,10))
"""

        """for parede in paredes_hardware:              #ESSA PARA VER A COORDENADA DO MOUSE SE PRECISAR
            pygame.draw.rect (tela_jogo, (255,0,255), parede, 2)"""



        #atualiza a tela
        pygame.display.flip ()
    #encerra o programa
    pygame.quit ()
main ()
