import pygame

paredes_principal = [
   
    # topo do lago
    pygame.Rect(650, 350, 280, 60),

    # esquerda superior
    pygame.Rect(620, 410, 80, 70),

    # centro
    pygame.Rect(720, 430, 180, 120),

    # direita
    pygame.Rect(920, 430, 130, 100),

    # parte inferior
    pygame.Rect(700, 500, 260, 50),

    #limites mapa-topo
    pygame.Rect(0, 0, 1672, 20),
    
    #esquerda
    pygame.Rect(0, 0, 20, 941),
    
    #direita
    pygame.Rect(1652, 0, 20, 941),
    
    #baixo
    pygame.Rect(0, 921, 1672, 20),

    #BIBLIOTECA 

    #topo
    pygame.Rect(75, 20, 520, 25),
    
    #esquerda
    pygame.Rect(75, 20, 25, 260),
    
    #direita
    pygame.Rect(570, 20, 25, 260),
    
    #base esquerda da porta
    pygame.Rect(75, 255, 220, 25),
    
    #base direita da porta
    pygame.Rect(385, 255, 220, 25),

    #LABORATÓRIOS

    #topo
    pygame.Rect(640, 15, 400, 20),

    #esquerda
    pygame.Rect(640, 15, 20, 250),

    #direita
    pygame.Rect(1020, 15, 20, 250),

    #base esquerda da porta
    pygame.Rect(640, 245, 150, 20),

    #base direita da porta
    pygame.Rect(870, 245, 170, 20),

    #BANHEIRO

    #topo
    pygame.Rect(1045, 15, 180, 20),

    #esquerda
    pygame.Rect(1045, 15, 20, 180),

    #direita
    pygame.Rect(1205, 15, 20, 180),

    #base esquerda da porta
    pygame.Rect(1045, 175, 45, 20),

    #base direita da porta
    pygame.Rect(1165, 175, 60, 20),

    #ÁREA PRIVADA

    #topo
    pygame.Rect(1170, 15, 470, 20),

    #esquerda
    pygame.Rect(1170, 15, 20, 240),

    #direita
    pygame.Rect(1620, 15, 20, 240),

    #base esquerda da porta
    pygame.Rect(1170, 235, 120, 20),

    #base direita da porta
    pygame.Rect(1375, 235, 265, 20),

    #ROBOCIN

    #topo
    pygame.Rect(1360, 300, 250, 20),

    #esquerda acima da porta
    pygame.Rect(1360, 300, 20, 90),

    #esquerda abaixo da porta
    pygame.Rect(1368, 470, 20, 100),

    #direita
    pygame.Rect(1590, 300, 20, 330),

    #base
    pygame.Rect(1360, 610, 250, 20),

    #MESANINO

    #topo esquerdo
    pygame.Rect(970, 610, 80, 20),

    #topo direito
    pygame.Rect(1125, 610, 80, 20),

    #parede oeste
    pygame.Rect(970, 610, 12, 300),

    #base
    pygame.Rect(970, 790, 230, 20),

    #SALA DE MÚSICA

    #topo esquerdo
    pygame.Rect(1190, 610, 90, 20),

    #topo direito
    pygame.Rect(1410, 590, 50, 20),

    #esquerda acima da porta
    pygame.Rect(1220, 610, 20, 40),

    #esquerda abaixo da porta
    pygame.Rect(1220, 690, 20, 120),

    #direita
    pygame.Rect(1440, 590, 20, 220),

    #base
    pygame.Rect(1220, 790, 240, 20),

    #ANFITEATRO

    #topo
    pygame.Rect(240, 515, 300, 20),

    #esquerda
    pygame.Rect(320, 500, 20, 260),

    #direita acima da porta
    pygame.Rect(555, 540, 12, 70),

    #direita abaixo da porta
    pygame.Rect(555, 690, 12, 70),

    #base
    pygame.Rect(320, 740, 230, 20),

    #HELPDESK

    #topo
    pygame.Rect(160, 690, 320, 20),

    #esquerda
    pygame.Rect(160, 690, 20, 170),

    #direita acima da porta
    pygame.Rect(460, 690, 20, 90),

    #direita abaixo da porta
    pygame.Rect(460, 850, 20, 10),

    #base
    pygame.Rect(160, 840, 320, 20),

    #HARDWARE - parede direita
    pygame.Rect(285, 275, 20, 300),

    #muro sul da portaria
    pygame.Rect(600, 850, 520, 20),

    #canto esquerdo
    pygame.Rect(600, 830, 20, 85),

    #canto direito
    pygame.Rect(1100, 830, 20, 85),

]
