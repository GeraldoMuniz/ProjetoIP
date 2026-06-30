import pygame

paredes_biblioteca = [
  
    #PAREDES EXTERNAS

    #topo
    pygame.Rect(20, 20, 1620, 20),

    #esquerda
    pygame.Rect(20, 20, 20, 800),

    #direita
    pygame.Rect(1620, 20, 20, 800),

    #base esquerda
    pygame.Rect(60, 820, 220, 20),

    #entre as portas
    pygame.Rect(390, 820, 830, 20),

    #base direita
    pygame.Rect(1330, 820, 310, 20),

    #SETOR SUPERIOR

    #mesa superior esquerda
    pygame.Rect(75, 77, 170, 120),

    #estante superior esquerda
    pygame.Rect(350, 75, 100, 100),

    #estante superior central
    pygame.Rect(490, 55, 300, 100),

    #mesa central superior
    pygame.Rect(495, 195, 260, 70),

    #mesa pequena superior                  #aq
    pygame.Rect(865, 205, 120, 70),

    #estante superior direita          #ok
    pygame.Rect(930, 55, 240, 100),

    #estante horizontal direita
    pygame.Rect(1060, 215, 175, 90),

    #mesa superior direita       #ok
    pygame.Rect(1380, 140, 100, 65),

    #estante superior extrema direita
    pygame.Rect(1220, 50, 240, 100),

    #globo central
    pygame.Rect(790, 400, 90, 90),

    #estante vertical esquerda
    pygame.Rect(495, 320, 70, 150),

    #estante vertical central
    pygame.Rect(630, 350, 70, 170),

    #estante vertical direita
    pygame.Rect(960, 350, 55, 150),             #OKOKOKOK

    #SETOR ESQUERDO

    #mesa grande esquerda
    pygame.Rect(150, 360, 90, 160),             #ok

    #estante horizontal esquerda                     #ok
    pygame.Rect(240, 250, 130, 70),

    #estante horizontal meio-esquerda
    pygame.Rect(300, 520, 160, 70),

    #estante vertical inferior esquerda
    pygame.Rect(50, 540, 90, 130),

    #estante ao lado da porta do Hardware
    pygame.Rect(200, 650, 110, 180),

    #estante à direita da porta do Hardware
    pygame.Rect(380, 690, 200, 180),

    #CENTRO INFERIOR

    #estante horizontal central
    pygame.Rect(640, 580, 160, 100),

    #estante vertical pequena
    pygame.Rect(930, 580, 60, 120),

    #SETOR DIREITO

    #estante vertical superior direita              #ok
    pygame.Rect(1360, 250, 70, 120),

    #estante vertical central direita             #ok
    pygame.Rect(1390, 420, 70, 150),

    #estante horizontal centro-direita        #ok
    pygame.Rect(1110, 390, 155, 70),

    #mesa da direita                #
    pygame.Rect(1500, 230, 120, 100),

    #estante em "L" (parte vertical)       #ok
    pygame.Rect(1100, 400, 60, 150),

    #estante horizontal inferior direita            #ok
    pygame.Rect(1060, 630, 170, 110),

    #estante inferior extrema direita                  #ok
    pygame.Rect(1320, 650, 120, 90),

    #estante ao lado da parede direita           #ok
    pygame.Rect(1500, 500, 110, 130),

    #estante inferior canto direito        #ok
    pygame.Rect(1450, 760, 100, 50),

]
