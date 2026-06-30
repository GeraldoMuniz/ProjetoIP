import pygame

paredes_principal = [
   #lago-parte superior
    pygame.Rect(560, 330, 520, 120),

    #centro
    pygame.Rect(500, 400, 650, 170),

    #inferior
    pygame.Rect(550, 560, 550, 90),

    #Limites mapa-topo
    pygame.Rect(0, 0, 1672, 20),
    
    #esquerda
    pygame.Rect(0, 0, 20, 941),
    
    #direita
    pygame.Rect(1652, 0, 20, 941),
    
    #baixo
    pygame.Rect(0, 921, 1672, 20),

    #biblioteca topo
    pygame.Rect(75, 20, 520, 25),
    
    #esquerda
    pygame.Rect(75, 20, 25, 260),
    
    #direita
    pygame.Rect(570, 20, 25, 260),
    
    #base esquerda da porta
    pygame.Rect(75, 255, 220, 25),
    
    #base direita da porta
    pygame.Rect(375, 255, 220, 25),

]
