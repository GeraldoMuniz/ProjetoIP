import pygame

paredes_principal = [
   
    #topo do lago
    pygame.Rect(620, 350, 330, 70),

    #centro esquerdo
    pygame.Rect(540, 420, 220, 130),

    #centro
    pygame.Rect(760, 420, 180, 180),

    #centro direito
    pygame.Rect(940, 430, 140, 120),

    #parte inferior
    pygame.Rect(650, 560, 320, 50),

    #limites mapa-topo
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
