import pygame

paredes_laboratorio = [
    
    #EXTERNOS

    #topo
    pygame.Rect(20, 20, 1620, 20),

    #esquerda
    pygame.Rect(20, 20, 20, 820),

    #direita
    pygame.Rect(1620, 20, 20, 820),

    #base esquerda da porta
    pygame.Rect(20, 820, 730, 20),

    #base direita da porta
    pygame.Rect(900, 820, 740, 20),

    #parte da esquerda

    pygame.Rect(60, 420, 185, 120),
    pygame.Rect(60, 600, 330, 195),


    #mesa grande central

    pygame.Rect(560, 470, 460, 185),           #ok

    #mesa direita

    pygame.Rect(1220, 345, 185, 120),

    #maquina direita grande

    pygame.Rect(1280, 540, 320, 270),

    #parte superior

    pygame.Rect(60, 70, 300, 280),
    pygame.Rect(515, 220, 170, 100),
    pygame.Rect(740, 220, 160, 100),
    pygame.Rect(955, 220, 135, 100),
    pygame.Rect(1200, 45, 240, 270),
    pygame.Rect(1475, 170, 180, 150),
]
