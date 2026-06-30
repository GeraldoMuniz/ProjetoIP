import pygame

paredes_biblioteca = [
  
    #PAREDES EXTERNAS
  
    #topo
    pygame.Rect(20, 20, 1620, 20),

    #esquerda
    pygame.Rect(20, 20, 20, 800),

    #direita
    pygame.Rect(1620, 20, 20, 800),

    #base esquerda da porta
    pygame.Rect(20, 800, 640, 20),

    #base direita da porta
    pygame.Rect(760, 800, 880, 20),

    #ESTANTES SUPERIORES
  
    pygame.Rect(340, 65, 120, 45),
    pygame.Rect(500, 65, 250, 45),
    pygame.Rect(940, 65, 250, 45),
    pygame.Rect(1250, 65, 180, 45),

    #CANTO SUPERIOR ESQUERDO
  
    pygame.Rect(45, 85, 70, 170),
    pygame.Rect(120, 40, 170, 120),

    #CANTO SUPERIOR DIREITO
  
    pygame.Rect(1370, 45, 180, 120),

    #MESAS GRANDES

    pygame.Rect(120, 320, 130, 110),
    pygame.Rect(520, 170, 180, 70),
    pygame.Rect(860, 170, 120, 70),
    pygame.Rect(1070, 180, 150, 80),
    pygame.Rect(1450, 180, 90, 90),
  
    #ESTANTES ESQUERDA

    pygame.Rect(250, 250, 120, 70),
    pygame.Rect(260, 520, 140, 70),
    pygame.Rect(90, 610, 140, 70),

    #ESTANTES CENTRAIS

    pygame.Rect(470, 250, 55, 120),
    pygame.Rect(620, 250, 55, 140),

    pygame.Rect(620, 550, 140, 70),

    pygame.Rect(450, 640, 70, 120),
    pygame.Rect(540, 640, 120, 120),

    # GLOBO CENTRAL

    pygame.Rect(740, 290, 120, 120),

    # ESTANTES DIREITA DO GLOBO

    pygame.Rect(920, 250, 55, 140),
    pygame.Rect(1090, 260, 55, 150),
    pygame.Rect(1110, 350, 150, 70),
  
    # REGIÃO INFERIOR CENTRAL

    pygame.Rect(860, 560, 60, 120),
    pygame.Rect(1060, 600, 160, 70),

    # ESTANTES DIREITA

    pygame.Rect(1370, 260, 60, 160),
    pygame.Rect(1370, 420, 60, 120),

    pygame.Rect(1450, 500, 110, 80),

    pygame.Rect(1290, 600, 120, 90),
  
    pygame.Rect(1440, 700, 120, 80),

    # REGIÃO DA PORTA SUL

    pygame.Rect(180, 710, 90, 90),
    pygame.Rect(360, 700, 90, 100),

]
