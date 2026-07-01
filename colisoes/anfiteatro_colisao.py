import pygame
#OK
paredes_anfiteatro = [

    pygame.Rect (200, 140, 100, 190),
    pygame.Rect(70, 0, 1530, 60),       
    pygame.Rect(70, 60, 80, 1000),       
    pygame.Rect(1320, 60, 100, 240),    
    pygame.Rect (1420, 490, 1, 400),

    #PALCO
    pygame.Rect(0, 60, 1530, 200),      #telao e parede do telao
    pygame.Rect(440, 340, 60, 100),    #Caixa de som esquerda
    pygame.Rect(1110, 340, 50, 100),   #Caixa de som direita
    

    #PAREDES LATERAIS
    pygame.Rect(0, 0, 70, 941),         
    pygame.Rect(70, 910, 1532, 31),     

    #CADEIRAS PLATEIA
    pygame.Rect(355, 510, 410, 345),    
    pygame.Rect(845, 510, 410, 345),
    
]